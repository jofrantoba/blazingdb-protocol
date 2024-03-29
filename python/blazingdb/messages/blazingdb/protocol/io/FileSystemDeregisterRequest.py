# automatically generated by the FlatBuffers compiler, do not modify

# namespace: io

import flatbuffers

class FileSystemDeregisterRequest(object):
    __slots__ = ['_tab']

    @classmethod
    def GetRootAsFileSystemDeregisterRequest(cls, buf, offset):
        n = flatbuffers.encode.Get(flatbuffers.packer.uoffset, buf, offset)
        x = FileSystemDeregisterRequest()
        x.Init(buf, n + offset)
        return x

    # FileSystemDeregisterRequest
    def Init(self, buf, pos):
        self._tab = flatbuffers.table.Table(buf, pos)

    # FileSystemDeregisterRequest
    def Authority(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None

def FileSystemDeregisterRequestStart(builder): builder.StartObject(1)
def FileSystemDeregisterRequestAddAuthority(builder, authority): builder.PrependUOffsetTRelativeSlot(0, flatbuffers.number_types.UOffsetTFlags.py_type(authority), 0)
def FileSystemDeregisterRequestEnd(builder): return builder.EndObject()
