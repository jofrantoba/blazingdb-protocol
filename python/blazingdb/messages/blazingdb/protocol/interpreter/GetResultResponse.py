# automatically generated by the FlatBuffers compiler, do not modify

# namespace: interpreter

import flatbuffers

class GetResultResponse(object):
    __slots__ = ['_tab']

    @classmethod
    def GetRootAsGetResultResponse(cls, buf, offset):
        n = flatbuffers.encode.Get(flatbuffers.packer.uoffset, buf, offset)
        x = GetResultResponse()
        x.Init(buf, n + offset)
        return x

    # GetResultResponse
    def Init(self, buf, pos):
        self._tab = flatbuffers.table.Table(buf, pos)

    # GetResultResponse
    def Metadata(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            x = self._tab.Indirect(o + self._tab.Pos)
            from .BlazingMetadata import BlazingMetadata
            obj = BlazingMetadata()
            obj.Init(self._tab.Bytes, x)
            return obj
        return None

    # GetResultResponse
    def Columns(self, j):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(6))
        if o != 0:
            x = self._tab.Vector(o)
            x += flatbuffers.number_types.UOffsetTFlags.py_type(j) * 4
            x = self._tab.Indirect(x)
            from blazingdb.messages.blazingdb.protocol.gdf.gdf_column_handler import gdf_column_handler
            obj = gdf_column_handler()
            obj.Init(self._tab.Bytes, x)
            return obj
        return None

    # GetResultResponse
    def ColumnsLength(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(6))
        if o != 0:
            return self._tab.VectorLen(o)
        return 0

    # GetResultResponse
    def ColumnNames(self, j):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(8))
        if o != 0:
            a = self._tab.Vector(o)
            return self._tab.String(a + flatbuffers.number_types.UOffsetTFlags.py_type(j * 4))
        return ""

    # GetResultResponse
    def ColumnNamesLength(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(8))
        if o != 0:
            return self._tab.VectorLen(o)
        return 0

    # GetResultResponse
    def ColumnTokens(self, j):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(10))
        if o != 0:
            a = self._tab.Vector(o)
            return self._tab.Get(flatbuffers.number_types.Uint64Flags, a + flatbuffers.number_types.UOffsetTFlags.py_type(j * 8))
        return 0

    # GetResultResponse
    def ColumnTokensAsNumpy(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(10))
        if o != 0:
            return self._tab.GetVectorAsNumpy(flatbuffers.number_types.Uint64Flags, o)
        return 0

    # GetResultResponse
    def ColumnTokensLength(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(10))
        if o != 0:
            return self._tab.VectorLen(o)
        return 0

def GetResultResponseStart(builder): builder.StartObject(4)
def GetResultResponseAddMetadata(builder, metadata): builder.PrependUOffsetTRelativeSlot(0, flatbuffers.number_types.UOffsetTFlags.py_type(metadata), 0)
def GetResultResponseAddColumns(builder, columns): builder.PrependUOffsetTRelativeSlot(1, flatbuffers.number_types.UOffsetTFlags.py_type(columns), 0)
def GetResultResponseStartColumnsVector(builder, numElems): return builder.StartVector(4, numElems, 4)
def GetResultResponseAddColumnNames(builder, columnNames): builder.PrependUOffsetTRelativeSlot(2, flatbuffers.number_types.UOffsetTFlags.py_type(columnNames), 0)
def GetResultResponseStartColumnNamesVector(builder, numElems): return builder.StartVector(4, numElems, 4)
def GetResultResponseAddColumnTokens(builder, columnTokens): builder.PrependUOffsetTRelativeSlot(3, flatbuffers.number_types.UOffsetTFlags.py_type(columnTokens), 0)
def GetResultResponseStartColumnTokensVector(builder, numElems): return builder.StartVector(8, numElems, 8)
def GetResultResponseEnd(builder): return builder.EndObject()
