# automatically generated by the FlatBuffers compiler, do not modify

# namespace: io

import flatbuffers

class CsvFile(object):
    __slots__ = ['_tab']

    @classmethod
    def GetRootAsCsvFile(cls, buf, offset):
        n = flatbuffers.encode.Get(flatbuffers.packer.uoffset, buf, offset)
        x = CsvFile()
        x.Init(buf, n + offset)
        return x

    # CsvFile
    def Init(self, buf, pos):
        self._tab = flatbuffers.table.Table(buf, pos)

    # CsvFile
    def Path(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return ""

    # CsvFile
    def Delimiter(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(6))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return ""

    # CsvFile
    def LineTerminator(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(8))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return ""

    # CsvFile
    def SkipRows(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(10))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0

    # CsvFile
    def Names(self, j):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(12))
        if o != 0:
            a = self._tab.Vector(o)
            return self._tab.String(a + flatbuffers.number_types.UOffsetTFlags.py_type(j * 4))
        return ""

    # CsvFile
    def NamesLength(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(12))
        if o != 0:
            return self._tab.VectorLen(o)
        return 0

    # CsvFile
    def Dtypes(self, j):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(14))
        if o != 0:
            a = self._tab.Vector(o)
            return self._tab.Get(flatbuffers.number_types.Int32Flags, a + flatbuffers.number_types.UOffsetTFlags.py_type(j * 4))
        return 0

    # CsvFile
    def DtypesLength(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(14))
        if o != 0:
            return self._tab.VectorLen(o)
        return 0

def CsvFileStart(builder): builder.StartObject(6)
def CsvFileAddPath(builder, path): builder.PrependUOffsetTRelativeSlot(0, flatbuffers.number_types.UOffsetTFlags.py_type(path), 0)
def CsvFileAddDelimiter(builder, delimiter): builder.PrependUOffsetTRelativeSlot(1, flatbuffers.number_types.UOffsetTFlags.py_type(delimiter), 0)
def CsvFileAddLineTerminator(builder, lineTerminator): builder.PrependUOffsetTRelativeSlot(2, flatbuffers.number_types.UOffsetTFlags.py_type(lineTerminator), 0)
def CsvFileAddSkipRows(builder, skipRows): builder.PrependInt32Slot(3, skipRows, 0)
def CsvFileAddNames(builder, names): builder.PrependUOffsetTRelativeSlot(4, flatbuffers.number_types.UOffsetTFlags.py_type(names), 0)
def CsvFileStartNamesVector(builder, numElems): return builder.StartVector(4, numElems, 4)
def CsvFileAddDtypes(builder, dtypes): builder.PrependUOffsetTRelativeSlot(5, flatbuffers.number_types.UOffsetTFlags.py_type(dtypes), 0)
def CsvFileStartDtypesVector(builder, numElems): return builder.StartVector(4, numElems, 4)
def CsvFileEnd(builder): return builder.EndObject()
