# automatically generated by the FlatBuffers compiler, do not modify

# namespace: io

import flatbuffers

class FileSystemBlazingTable(object):
    __slots__ = ['_tab']

    @classmethod
    def GetRootAsFileSystemBlazingTable(cls, buf, offset):
        n = flatbuffers.encode.Get(flatbuffers.packer.uoffset, buf, offset)
        x = FileSystemBlazingTable()
        x.Init(buf, n + offset)
        return x

    # FileSystemBlazingTable
    def Init(self, buf, pos):
        self._tab = flatbuffers.table.Table(buf, pos)

    # FileSystemBlazingTable
    def Name(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None

    # FileSystemBlazingTable
    def SchemaType(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(6))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int8Flags, o + self._tab.Pos)
        return 0

    # FileSystemBlazingTable
    def Csv(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(8))
        if o != 0:
            x = self._tab.Indirect(o + self._tab.Pos)
            from .CsvFile import CsvFile
            obj = CsvFile()
            obj.Init(self._tab.Bytes, x)
            return obj
        return None

    # FileSystemBlazingTable
    def Parquet(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(10))
        if o != 0:
            x = self._tab.Indirect(o + self._tab.Pos)
            from .ParquetFile import ParquetFile
            obj = ParquetFile()
            obj.Init(self._tab.Bytes, x)
            return obj
        return None

    # FileSystemBlazingTable
    def Files(self, j):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(12))
        if o != 0:
            a = self._tab.Vector(o)
            return self._tab.String(a + flatbuffers.number_types.UOffsetTFlags.py_type(j * 4))
        return ""

    # FileSystemBlazingTable
    def FilesLength(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(12))
        if o != 0:
            return self._tab.VectorLen(o)
        return 0

    # FileSystemBlazingTable
    def ColumnNames(self, j):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(14))
        if o != 0:
            a = self._tab.Vector(o)
            return self._tab.String(a + flatbuffers.number_types.UOffsetTFlags.py_type(j * 4))
        return ""

    # FileSystemBlazingTable
    def ColumnNamesLength(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(14))
        if o != 0:
            return self._tab.VectorLen(o)
        return 0

def FileSystemBlazingTableStart(builder): builder.StartObject(6)
def FileSystemBlazingTableAddName(builder, name): builder.PrependUOffsetTRelativeSlot(0, flatbuffers.number_types.UOffsetTFlags.py_type(name), 0)
def FileSystemBlazingTableAddSchemaType(builder, schemaType): builder.PrependInt8Slot(1, schemaType, 0)
def FileSystemBlazingTableAddCsv(builder, csv): builder.PrependUOffsetTRelativeSlot(2, flatbuffers.number_types.UOffsetTFlags.py_type(csv), 0)
def FileSystemBlazingTableAddParquet(builder, parquet): builder.PrependUOffsetTRelativeSlot(3, flatbuffers.number_types.UOffsetTFlags.py_type(parquet), 0)
def FileSystemBlazingTableAddFiles(builder, files): builder.PrependUOffsetTRelativeSlot(4, flatbuffers.number_types.UOffsetTFlags.py_type(files), 0)
def FileSystemBlazingTableStartFilesVector(builder, numElems): return builder.StartVector(4, numElems, 4)
def FileSystemBlazingTableAddColumnNames(builder, columnNames): builder.PrependUOffsetTRelativeSlot(5, flatbuffers.number_types.UOffsetTFlags.py_type(columnNames), 0)
def FileSystemBlazingTableStartColumnNamesVector(builder, numElems): return builder.StartVector(4, numElems, 4)
def FileSystemBlazingTableEnd(builder): return builder.EndObject()