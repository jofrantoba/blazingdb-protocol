# automatically generated by the FlatBuffers compiler, do not modify

# namespace: protocol

import flatbuffers

class ResponseError(object):
    __slots__ = ['_tab']

    @classmethod
    def GetRootAsResponseError(cls, buf, offset):
        n = flatbuffers.encode.Get(flatbuffers.packer.uoffset, buf, offset)
        x = ResponseError()
        x.Init(buf, n + offset)
        return x

    # ResponseError
    def Init(self, buf, pos):
        self._tab = flatbuffers.table.Table(buf, pos)

    # ResponseError
    def Errors(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None

def ResponseErrorStart(builder): builder.StartObject(1)
def ResponseErrorAddErrors(builder, errors): builder.PrependUOffsetTRelativeSlot(0, flatbuffers.number_types.UOffsetTFlags.py_type(errors), 0)
def ResponseErrorEnd(builder): return builder.EndObject()
