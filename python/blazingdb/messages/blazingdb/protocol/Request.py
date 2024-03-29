# automatically generated by the FlatBuffers compiler, do not modify

# namespace: protocol

import flatbuffers

class Request(object):
    __slots__ = ['_tab']

    @classmethod
    def GetRootAsRequest(cls, buf, offset):
        n = flatbuffers.encode.Get(flatbuffers.packer.uoffset, buf, offset)
        x = Request()
        x.Init(buf, n + offset)
        return x

    # Request
    def Init(self, buf, pos):
        self._tab = flatbuffers.table.Table(buf, pos)

    # Request
    def Header(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            x = o + self._tab.Pos
            from .Header import Header
            obj = Header()
            obj.Init(self._tab.Bytes, x)
            return obj
        return None

    # Request
    def Payload(self, j):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(6))
        if o != 0:
            a = self._tab.Vector(o)
            return self._tab.Get(flatbuffers.number_types.Uint8Flags, a + flatbuffers.number_types.UOffsetTFlags.py_type(j * 1))
        return 0

    # Request
    def PayloadAsNumpy(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(6))
        if o != 0:
            return self._tab.GetVectorAsNumpy(flatbuffers.number_types.Uint8Flags, o)
        return 0

    # Request
    def PayloadLength(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(6))
        if o != 0:
            return self._tab.VectorLen(o)
        return 0

def RequestStart(builder): builder.StartObject(2)
def RequestAddHeader(builder, header): builder.PrependStructSlot(0, flatbuffers.number_types.UOffsetTFlags.py_type(header), 0)
def RequestAddPayload(builder, payload): builder.PrependUOffsetTRelativeSlot(1, flatbuffers.number_types.UOffsetTFlags.py_type(payload), 0)
def RequestStartPayloadVector(builder, numElems): return builder.StartVector(1, numElems, 1)
def RequestEnd(builder): return builder.EndObject()
