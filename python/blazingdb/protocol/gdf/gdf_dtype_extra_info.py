# automatically generated by the FlatBuffers compiler, do not modify

# namespace: gdf

import flatbuffers

class gdf_dtype_extra_info(object):
    __slots__ = ['_tab']

    @classmethod
    def GetRootAsgdf_dtype_extra_info(cls, buf, offset):
        n = flatbuffers.encode.Get(flatbuffers.packer.uoffset, buf, offset)
        x = gdf_dtype_extra_info()
        x.Init(buf, n + offset)
        return x

    # gdf_dtype_extra_info
    def Init(self, buf, pos):
        self._tab = flatbuffers.table.Table(buf, pos)

    # gdf_dtype_extra_info
    def TimeUnit(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int8Flags, o + self._tab.Pos)
        return 0

    # gdf_dtype_extra_info
    def CustringsViews(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(6))
        if o != 0:
            x = self._tab.Indirect(o + self._tab.Pos)
            from .cudaIpcMemHandle_t import cudaIpcMemHandle_t
            obj = cudaIpcMemHandle_t()
            obj.Init(self._tab.Bytes, x)
            return obj
        return None

    # gdf_dtype_extra_info
    def CustringsViewscount(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(8))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Uint32Flags, o + self._tab.Pos)
        return 0

    # gdf_dtype_extra_info
    def CustringsMembuffer(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(10))
        if o != 0:
            x = self._tab.Indirect(o + self._tab.Pos)
            from .cudaIpcMemHandle_t import cudaIpcMemHandle_t
            obj = cudaIpcMemHandle_t()
            obj.Init(self._tab.Bytes, x)
            return obj
        return None

    # gdf_dtype_extra_info
    def CustringsMembuffersize(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(12))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Uint64Flags, o + self._tab.Pos)
        return 0

    # gdf_dtype_extra_info
    def CustringsBaseptr(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(14))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Uint64Flags, o + self._tab.Pos)
        return 0

def gdf_dtype_extra_infoStart(builder): builder.StartObject(6)
def gdf_dtype_extra_infoAddTimeUnit(builder, timeUnit): builder.PrependInt8Slot(0, timeUnit, 0)
def gdf_dtype_extra_infoAddCustringsViews(builder, custringsViews): builder.PrependUOffsetTRelativeSlot(1, flatbuffers.number_types.UOffsetTFlags.py_type(custringsViews), 0)
def gdf_dtype_extra_infoAddCustringsViewscount(builder, custringsViewscount): builder.PrependUint32Slot(2, custringsViewscount, 0)
def gdf_dtype_extra_infoAddCustringsMembuffer(builder, custringsMembuffer): builder.PrependUOffsetTRelativeSlot(3, flatbuffers.number_types.UOffsetTFlags.py_type(custringsMembuffer), 0)
def gdf_dtype_extra_infoAddCustringsMembuffersize(builder, custringsMembuffersize): builder.PrependUint64Slot(4, custringsMembuffersize, 0)
def gdf_dtype_extra_infoAddCustringsBaseptr(builder, custringsBaseptr): builder.PrependUint64Slot(5, custringsBaseptr, 0)
def gdf_dtype_extra_infoEnd(builder): return builder.EndObject()
