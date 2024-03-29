# automatically generated by the FlatBuffers compiler, do not modify

# namespace: io

import flatbuffers

class ParquetFile(object):
    __slots__ = ['_tab']

    @classmethod
    def GetRootAsParquetFile(cls, buf, offset):
        n = flatbuffers.encode.Get(flatbuffers.packer.uoffset, buf, offset)
        x = ParquetFile()
        x.Init(buf, n + offset)
        return x

    # ParquetFile
    def Init(self, buf, pos):
        self._tab = flatbuffers.table.Table(buf, pos)

    # ParquetFile
    def Path(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None

    # ParquetFile
    def RowGroupIndices(self, j):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(6))
        if o != 0:
            a = self._tab.Vector(o)
            return self._tab.Get(flatbuffers.number_types.Int32Flags, a + flatbuffers.number_types.UOffsetTFlags.py_type(j * 4))
        return 0

    # ParquetFile
    def RowGroupIndicesAsNumpy(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(6))
        if o != 0:
            return self._tab.GetVectorAsNumpy(flatbuffers.number_types.Int32Flags, o)
        return 0

    # ParquetFile
    def RowGroupIndicesLength(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(6))
        if o != 0:
            return self._tab.VectorLen(o)
        return 0

    # ParquetFile
    def ColumnIndices(self, j):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(8))
        if o != 0:
            a = self._tab.Vector(o)
            return self._tab.Get(flatbuffers.number_types.Int32Flags, a + flatbuffers.number_types.UOffsetTFlags.py_type(j * 4))
        return 0

    # ParquetFile
    def ColumnIndicesAsNumpy(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(8))
        if o != 0:
            return self._tab.GetVectorAsNumpy(flatbuffers.number_types.Int32Flags, o)
        return 0

    # ParquetFile
    def ColumnIndicesLength(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(8))
        if o != 0:
            return self._tab.VectorLen(o)
        return 0

def ParquetFileStart(builder): builder.StartObject(3)
def ParquetFileAddPath(builder, path): builder.PrependUOffsetTRelativeSlot(0, flatbuffers.number_types.UOffsetTFlags.py_type(path), 0)
def ParquetFileAddRowGroupIndices(builder, rowGroupIndices): builder.PrependUOffsetTRelativeSlot(1, flatbuffers.number_types.UOffsetTFlags.py_type(rowGroupIndices), 0)
def ParquetFileStartRowGroupIndicesVector(builder, numElems): return builder.StartVector(4, numElems, 4)
def ParquetFileAddColumnIndices(builder, columnIndices): builder.PrependUOffsetTRelativeSlot(2, flatbuffers.number_types.UOffsetTFlags.py_type(columnIndices), 0)
def ParquetFileStartColumnIndicesVector(builder, numElems): return builder.StartVector(4, numElems, 4)
def ParquetFileEnd(builder): return builder.EndObject()
