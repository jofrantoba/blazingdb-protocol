"""Transport layer to map Flatbuffers modules with user schema classes."""

__author__ = 'BlazingDB Team'

import abc
import inspect
import re

import flatbuffers

from blazingdb.messages.blazingdb.protocol import Header, Request, Response


__all__ = ('schema', 'Schema')


def schema(module):
  """Shortcut to create concrete schema classes.

  Args:
    module: A Flatbuffers module for message

  Useful to have a simple way to define schemas.

  class ConcreteSchema(schema(FlatBuffersModule)):
    field_str = StringSegment()
    field_int = NumberSegment()
  """
  return type(module.__name__ + 'SchemaBase', (Schema,), dict(_module=module))


class MetaSchema(type):
  """Metaclass for Schema.

  To fix up segment members of the concrete schema.
  """

  def __init__(cls, name, bases, classdict):
    super().__init__(name, bases, classdict)
    cls._fix_up_segments()


class SchemaAttribute(abc.ABC):
  """A base class to identify schema members."""

  @abc.abstractmethod
  def _fix_up(self, cls, name):
    return NotImplemented


class Schema(metaclass=MetaSchema):
  """A class describing Flatbuffers schema.

  All classes inheriting from Schema have MetaSchema, so that segments
  are fixed up after class definition.

  class ConcreteSchema(Schema):
    _module = flatbuffer.user.message.module

    field_str = StringSegment()
    field_int = NumberSegment()

  The related flatbuffers module is `None` by default. You must override
  in parent scope in order to have working `ToBuffer` and `From` methods. See
  `schema` function as a tool to create concrete schema classes.
  """

  _segments = None
  _module = None
  _values = None
  _nested = None
  _inline = None

  def ToBuffer(self):
    builder = flatbuffers.Builder(0)
    self._allocate_segments(builder)
    return builder.Output()

  def __init__(self, **kargs):
    self._values = {}
    self._set_attributes(kargs)

  def _set_attributes(self, kargs):
    cls = self.__class__
    for name, value in kargs.items():
      segment = getattr(cls, name)
      if not isinstance(segment, Segment):
        raise TypeError('Non segment %s' % name)
      segment._set_value(self, value)

  @classmethod
  def From(cls, buffer, position=0):
    name = cls._module_name()
    _object = getattr(getattr(cls._module, name),
                      'GetRootAs' + name)(buffer, position)
    members = {name: segment._from(_object)
               for name, segment in cls._segments.items()}
    name = cls._module_name()
    return type(lowerCamelCase(name), (), members)

  @classmethod
  def _module_name(cls):
    return _name_of(cls._module)

  @classmethod
  def _fix_up_segments(cls):
    if __name__ == cls.__module__:
      return
    cls._segments = {}
    cls._nested = []
    cls._inline = []
    for name in set(dir(cls)):
      attr = getattr(cls, name, None)
      if isinstance(attr, SchemaAttribute):
        attr._fix_up(cls, name)
        if isinstance(attr, Segment):
          cls._segments[name] = attr
          if isinstance(attr, Nested):
            cls._nested.append(attr)
          elif isinstance(attr, Inline):
            cls._inline.append(attr)
          else:
            raise TypeError('Bad `%s` segment type' % name)

  def _allocate_segments(self, builder):
    _object = self._set_segments(builder)
    builder.Finish(_object)
    return _object

  def _set_segments(self, builder):

    pairs = [(segment._name, segment._bytes(builder, self))
             for segment in self._nested]

    name = self._module_name()
    getattr(self._module, name + 'Start')(builder)

    for segment in self._inline:
      pairs.append((segment._name, segment._bytes(builder, self)))

    for member, value in reversed(pairs):
      member = upperCamelCase(member)
      getattr(self._module, '%sAdd%s' % (name, member))(builder, value)

    return getattr(self._module, name + 'End')(builder)


class Segment(SchemaAttribute):
  """A class describing a flatbuffers object segment attribute.

  It's just a base class. To set segments for you schemas, there are specific
  subclasses for various kind of flatbuffers object attributes.

  A `Segment` subclass implementing a specific transformation between a `Schema`
  and a flutbuffers object should implement `_bytes()` of member schema and
  `_from()` flatbuffers object to DTO or literal types (like `int` or `str`).
  """

  # TODO(gcca): GenericSegment for dynamic conversion

  _name = None

  def _fix_up(self, cls, name):
    self._name = name

  @abc.abstractmethod
  def _bytes(self, builder, schema):
    return NotImplemented

  @abc.abstractmethod
  def _from(self, _object):
    return NotImplemented

  def _set_value(self, schema, value):
    schema._values[self._name] = value

  def _object_name(self):
    return upperCamelCase(self._name)


class Nested:
  """Mark for segments with data for inside flatbuffers objs."""


class Inline:
  """Mark for segments with inline data for flatbuffers objs."""


class BuiltinSegment(Segment, abc.ABC):

  @abc.abstractmethod
  def _bytes(self, builder, schema):
    return NotImplemented

  def _from(self, _object):
    return getattr(_object, self._object_name())()


class NumberSegment(BuiltinSegment, Inline):
  """A `Segment` whose value is a literal number `int`, `float` or `bool`."""

  def _bytes(self, builder, schema):
    return schema._values[self._name]


class StringSegment(BuiltinSegment, Nested):
  """A `Segment` whose value is a literal string `str`."""

  def _bytes(self, builder, schema):
    return builder.CreateString(schema._values[self._name])


class BytesSegment(Segment, Nested):
  """A `Segment` whose value is a limited sequence of `bytes`."""

  def _bytes(self, builder, schema):
    name = schema._module_name()
    member = self._object_name()
    buffer = schema._values[self._name]
    getattr(schema._module,
            '%sStart%sVector' % (name, member))(builder, len(buffer))
    for byte in reversed(buffer):
      builder.PrependByte(byte)
    return builder.EndVector(len(buffer))

  def _from(self, _object):
    name = self._object_name()
    byte = getattr(_object, name)
    return bytes(byte(i) for i in range(getattr(_object, name + 'Length')()))


class StructSegment(Segment, Inline):
  """A segment whose value is itself a flatbuffers struct as a dict.

  The keys are the flatbuffers object attributes in camelCase.
  """

  def __init__(self, module):
    self._module = module

  def _bytes(self, builder, schema):
    module = self._module
    name = _name_of(module)
    value = schema._values[self._name]
    return getattr(module, 'Create' + name)(builder, **value)

  def _from(self, _object):
    return _dto(getattr(_object, self._object_name())(), self._name, ('Init',))


class Vector(Segment):

  def _make_iterable(self, _object, item):
    return (item(i)
            for i in range(getattr(_object, self._object_name() + 'Length')()))


class _VectorSegment(Vector):

  def __init__(self, segment):
    self._segment = segment

  def _bytes(self, builder, schema):
    items = [self._segment._bytes(
               self,
               builder,
               type(self._name, (), dict(_values={self._name: value})))
             for value in schema._values[self._name]]

    m = getattr(getattr(schema._module, schema._module_name()),
                self._object_name())
    m = inspect.unwrap(m)
    block, base = inspect.findsource(m)
    l = inspect.getblock(block[base:])[4].strip()
    p = r'\._tab\.(?:(String)(?=\()|Get\(flatbuffers\.number_types\.(\w+)(?=,))'
    o = next(value for value in re.search(p, l).groups() if value)
    f = {
      'String': builder.PrependUOffsetTRelative,
      'Int32Flags': builder.PrependUint32,
      'Uint64Flags': builder.PrependUint64
    }[o]

    getattr(schema._module,
            '%sStart%sVector' % (schema._module_name(),
                                 self._object_name()))(builder, len(items))

    for item in reversed(items):
      f(item)

    return builder.EndVector(len(items))

  def _from(self, _object):
    return self._make_iterable(_object, getattr(_object, self._object_name()))


class VectorSegment(_VectorSegment, Nested):
  """VS"""


class VectorStringSegment(Vector, Nested):

  def __init__(self, segment):
    self._segment = segment

  def _bytes(self, builder, schema):

    name = schema._module_name()
    member = self._object_name()
    buffer = schema._values[self._name]

    offset_list = []
    for string_val in reversed(buffer):
      offset_list.append(builder.CreateString(string_val))

    getattr(schema._module,
            '%sStart%sVector' % (name, member))(builder, len(buffer))

    for offset in offset_list:
      builder.PrependUOffsetTRelative(offset)
    return builder.EndVector(len(buffer))

  def _from(self, _object):
    return self._make_iterable(_object, getattr(_object, self._object_name()))


class VectorSchemaSegment(_VectorSegment, Nested):

  def __init__(self, schema):
    self._schema = schema

  def _bytes(self, builder, schema):
    items = [self._schema._set_segments(value, builder)
             for value in schema._values[self._name]]

    getattr(schema._module,
            '%sStart%sVector' % (schema._module_name(),
                                 self._object_name()))(builder, len(items))
    for item in reversed(items):
      builder.PrependUOffsetTRelative(item)

    return builder.EndVector(len(items))

  def _from(self, _object):
    return (type(lowerCamelCase(self._name), (), {
      name: segment._from(_object)
      for name, segment in self._schema._segments.items()
    }) for _object in super()._from(_object))


class VectorGdfColumnSegment(_VectorSegment, Nested):

  def __init__(self, schema):
    self._schema = schema

  def _bytes(self, builder, schema):
    items = [self._schema._set_segments(value, builder)
             for value in schema._values[self._name]]

    getattr(schema._module,
            '%sStart%sVector' % (schema._module_name(),
                                 self._object_name()))(builder, len(items))
    for item in reversed(items):
      builder.PrependUOffsetTRelative(item)

    return builder.EndVector(len(items))

  def _from(self, _object):
    nomembers = ('Init', 'GetRootAs' + self._schema._module_name())
    return (_dto(member, self._name, nomembers)
            for member in super()._from(_object))


class SchemaSegment(Segment, Nested):

  def __init__(self, schema):
    self._schema = schema

  def _bytes(self, builder, schema):
    return self._schema._allocate_segments(schema._values[self._name], builder)

  def _from(self, _object):
    _object = getattr(_object, self._object_name())()
    members = {name: segment._from(_object)
               for name, segment in self._schema._segments.items()}
    name = self._schema._module_name()
    return type(lowerCamelCase(name), (), members)


class UnionSegment(Segment, Nested):
  def __init__(self, schema):
    self._schema = schema

  def _bytes(self, builder, schema):
    return self._schema._allocate_segments(schema._values[self._name], builder)

  def _from(self, _object):
    _object = getattr(_object, self._object_name())()
    members = {name: segment._from(_object)
               for name, segment in self._schema._segments.items()}
    name = self._schema._module_name()
    return type(lowerCamelCase(name), (), members)



def _name_of(module):
  return module.__name__.split('.')[-1]


def _dto(_object, name, nomembers):
  return type(name, (), {lowerCamelCase(m): getattr(_object, m)()
                         for m in set(dir(_object)) - set(nomembers)
                         if m[0].isalpha()})


def lowerCamelCase(s):
  # //@todo: more than one _
  index = -1
  for i, c in enumerate(s):
    if c.isupper():
      index = i
  if index > 0:
    s = s[:index] + '_' + s[index:].lower()
  return s[0].lower() + s[1:]


def upperCamelCase(s):
  # //@todo: more than one _
  index = s.find('_')
  if index > 0:
    s = s.replace(s[index:index+2], s[index+1].upper())
  return s[0].upper() + s[1:]
