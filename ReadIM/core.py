# This file was automatically generated by SWIG (http://www.swig.org).
# Version 3.0.5
#
# Do not make changes to this file unless you know what you are doing--modify
# the SWIG interface file instead.





from sys import version_info
if version_info >= (2, 6, 0):
    def swig_import_helper():
        from os.path import dirname
        import imp
        fp = None
        try:
            fp, pathname, description = imp.find_module('_core', [dirname(__file__)])
        except ImportError:
            import _core
            return _core
        if fp is not None:
            try:
                _mod = imp.load_module('_core', fp, pathname, description)
            finally:
                fp.close()
            return _mod
    _core = swig_import_helper()
    del swig_import_helper
else:
    import _core
del version_info
try:
    _swig_property = property
except NameError:
    pass  # Python < 2.2 doesn't have 'property'.


def _swig_setattr_nondynamic(self, class_type, name, value, static=1):
    if (name == "thisown"):
        return self.this.own(value)
    if (name == "this"):
        if type(value).__name__ == 'SwigPyObject':
            self.__dict__[name] = value
            return
    method = class_type.__swig_setmethods__.get(name, None)
    if method:
        return method(self, value)
    if (not static):
        if _newclass:
            object.__setattr__(self, name, value)
        else:
            self.__dict__[name] = value
    else:
        raise AttributeError("You cannot add attributes to %s" % self)


def _swig_setattr(self, class_type, name, value):
    return _swig_setattr_nondynamic(self, class_type, name, value, 0)


def _swig_getattr_nondynamic(self, class_type, name, static=1):
    if (name == "thisown"):
        return self.this.own()
    method = class_type.__swig_getmethods__.get(name, None)
    if method:
        return method(self)
    if (not static):
        return object.__getattr__(self, name)
    else:
        raise AttributeError(name)

def _swig_getattr(self, class_type, name):
    return _swig_getattr_nondynamic(self, class_type, name, 0)


def _swig_repr(self):
    try:
        strthis = "proxy of " + self.this.__repr__()
    except:
        strthis = ""
    return "<%s.%s; %s >" % (self.__class__.__module__, self.__class__.__name__, strthis,)

try:
    _object = object
    _newclass = 1
except AttributeError:
    class _object:
        pass
    _newclass = 0



_core.IMREAD_ERR_NO_swigconstant(_core)
IMREAD_ERR_NO = _core.IMREAD_ERR_NO

_core.IMREAD_ERR_FILEOPEN_swigconstant(_core)
IMREAD_ERR_FILEOPEN = _core.IMREAD_ERR_FILEOPEN

_core.IMREAD_ERR_HEADER_swigconstant(_core)
IMREAD_ERR_HEADER = _core.IMREAD_ERR_HEADER

_core.IMREAD_ERR_FORMAT_swigconstant(_core)
IMREAD_ERR_FORMAT = _core.IMREAD_ERR_FORMAT

_core.IMREAD_ERR_DATA_swigconstant(_core)
IMREAD_ERR_DATA = _core.IMREAD_ERR_DATA

_core.IMREAD_ERR_MEMORY_swigconstant(_core)
IMREAD_ERR_MEMORY = _core.IMREAD_ERR_MEMORY

_core.IMREAD_ERR_ATTRIBUTE_INVALID_TYPE_swigconstant(_core)
IMREAD_ERR_ATTRIBUTE_INVALID_TYPE = _core.IMREAD_ERR_ATTRIBUTE_INVALID_TYPE

_core.IMREAD_ERR_ATTRIBUTE_NO_DATA_swigconstant(_core)
IMREAD_ERR_ATTRIBUTE_NO_DATA = _core.IMREAD_ERR_ATTRIBUTE_NO_DATA
class BufferScaleType(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, BufferScaleType, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, BufferScaleType, name)
    __repr__ = _swig_repr
    __swig_setmethods__["factor"] = _core.BufferScaleType_factor_set
    __swig_getmethods__["factor"] = _core.BufferScaleType_factor_get
    if _newclass:
        factor = _swig_property(_core.BufferScaleType_factor_get, _core.BufferScaleType_factor_set)
    __swig_setmethods__["offset"] = _core.BufferScaleType_offset_set
    __swig_getmethods__["offset"] = _core.BufferScaleType_offset_get
    if _newclass:
        offset = _swig_property(_core.BufferScaleType_offset_get, _core.BufferScaleType_offset_set)
    __swig_setmethods__["description"] = _core.BufferScaleType_description_set
    __swig_getmethods__["description"] = _core.BufferScaleType_description_get
    if _newclass:
        description = _swig_property(_core.BufferScaleType_description_get, _core.BufferScaleType_description_set)
    __swig_setmethods__["unit"] = _core.BufferScaleType_unit_set
    __swig_getmethods__["unit"] = _core.BufferScaleType_unit_get
    if _newclass:
        unit = _swig_property(_core.BufferScaleType_unit_get, _core.BufferScaleType_unit_set)

    def __init__(self):
        this = _core.new_BufferScaleType()
        try:
            self.this.append(this)
        except:
            self.this = this
    __swig_destroy__ = _core.delete_BufferScaleType
    __del__ = lambda self: None
BufferScaleType_swigregister = _core.BufferScaleType_swigregister
BufferScaleType_swigregister(BufferScaleType)


_core.BUFFER_FORMAT__NOTUSED_swigconstant(_core)
BUFFER_FORMAT__NOTUSED = _core.BUFFER_FORMAT__NOTUSED

_core.BUFFER_FORMAT_MEMPACKWORD_swigconstant(_core)
BUFFER_FORMAT_MEMPACKWORD = _core.BUFFER_FORMAT_MEMPACKWORD

_core.BUFFER_FORMAT_FLOAT_swigconstant(_core)
BUFFER_FORMAT_FLOAT = _core.BUFFER_FORMAT_FLOAT

_core.BUFFER_FORMAT_WORD_swigconstant(_core)
BUFFER_FORMAT_WORD = _core.BUFFER_FORMAT_WORD

_core.BUFFER_FORMAT_DOUBLE_swigconstant(_core)
BUFFER_FORMAT_DOUBLE = _core.BUFFER_FORMAT_DOUBLE

_core.BUFFER_FORMAT_FLOAT_VALID_swigconstant(_core)
BUFFER_FORMAT_FLOAT_VALID = _core.BUFFER_FORMAT_FLOAT_VALID

_core.BUFFER_FORMAT_IMAGE_swigconstant(_core)
BUFFER_FORMAT_IMAGE = _core.BUFFER_FORMAT_IMAGE

_core.BUFFER_FORMAT_VECTOR_2D_EXTENDED_swigconstant(_core)
BUFFER_FORMAT_VECTOR_2D_EXTENDED = _core.BUFFER_FORMAT_VECTOR_2D_EXTENDED

_core.BUFFER_FORMAT_VECTOR_2D_swigconstant(_core)
BUFFER_FORMAT_VECTOR_2D = _core.BUFFER_FORMAT_VECTOR_2D

_core.BUFFER_FORMAT_VECTOR_2D_EXTENDED_PEAK_swigconstant(_core)
BUFFER_FORMAT_VECTOR_2D_EXTENDED_PEAK = _core.BUFFER_FORMAT_VECTOR_2D_EXTENDED_PEAK

_core.BUFFER_FORMAT_VECTOR_3D_swigconstant(_core)
BUFFER_FORMAT_VECTOR_3D = _core.BUFFER_FORMAT_VECTOR_3D

_core.BUFFER_FORMAT_VECTOR_3D_EXTENDED_PEAK_swigconstant(_core)
BUFFER_FORMAT_VECTOR_3D_EXTENDED_PEAK = _core.BUFFER_FORMAT_VECTOR_3D_EXTENDED_PEAK

_core.BUFFER_FORMAT_COLOR_swigconstant(_core)
BUFFER_FORMAT_COLOR = _core.BUFFER_FORMAT_COLOR

_core.BUFFER_FORMAT_RGB_MATRIX_swigconstant(_core)
BUFFER_FORMAT_RGB_MATRIX = _core.BUFFER_FORMAT_RGB_MATRIX

_core.BUFFER_FORMAT_RGB_32_swigconstant(_core)
BUFFER_FORMAT_RGB_32 = _core.BUFFER_FORMAT_RGB_32
class BufferType(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, BufferType, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, BufferType, name)
    __repr__ = _swig_repr
    __swig_setmethods__["isFloat"] = _core.BufferType_isFloat_set
    __swig_getmethods__["isFloat"] = _core.BufferType_isFloat_get
    if _newclass:
        isFloat = _swig_property(_core.BufferType_isFloat_get, _core.BufferType_isFloat_set)
    __swig_setmethods__["nx"] = _core.BufferType_nx_set
    __swig_getmethods__["nx"] = _core.BufferType_nx_get
    if _newclass:
        nx = _swig_property(_core.BufferType_nx_get, _core.BufferType_nx_set)
    __swig_setmethods__["ny"] = _core.BufferType_ny_set
    __swig_getmethods__["ny"] = _core.BufferType_ny_get
    if _newclass:
        ny = _swig_property(_core.BufferType_ny_get, _core.BufferType_ny_set)
    __swig_setmethods__["nz"] = _core.BufferType_nz_set
    __swig_getmethods__["nz"] = _core.BufferType_nz_get
    if _newclass:
        nz = _swig_property(_core.BufferType_nz_get, _core.BufferType_nz_set)
    __swig_setmethods__["nf"] = _core.BufferType_nf_set
    __swig_getmethods__["nf"] = _core.BufferType_nf_get
    if _newclass:
        nf = _swig_property(_core.BufferType_nf_get, _core.BufferType_nf_set)
    __swig_setmethods__["totalLines"] = _core.BufferType_totalLines_set
    __swig_getmethods__["totalLines"] = _core.BufferType_totalLines_get
    if _newclass:
        totalLines = _swig_property(_core.BufferType_totalLines_get, _core.BufferType_totalLines_set)
    __swig_setmethods__["vectorGrid"] = _core.BufferType_vectorGrid_set
    __swig_getmethods__["vectorGrid"] = _core.BufferType_vectorGrid_get
    if _newclass:
        vectorGrid = _swig_property(_core.BufferType_vectorGrid_get, _core.BufferType_vectorGrid_set)
    __swig_setmethods__["image_sub_type"] = _core.BufferType_image_sub_type_set
    __swig_getmethods__["image_sub_type"] = _core.BufferType_image_sub_type_get
    if _newclass:
        image_sub_type = _swig_property(_core.BufferType_image_sub_type_get, _core.BufferType_image_sub_type_set)
    __swig_setmethods__["floatArray"] = _core.BufferType_floatArray_set
    __swig_getmethods__["floatArray"] = _core.BufferType_floatArray_get
    if _newclass:
        floatArray = _swig_property(_core.BufferType_floatArray_get, _core.BufferType_floatArray_set)
    __swig_setmethods__["wordArray"] = _core.BufferType_wordArray_set
    __swig_getmethods__["wordArray"] = _core.BufferType_wordArray_get
    if _newclass:
        wordArray = _swig_property(_core.BufferType_wordArray_get, _core.BufferType_wordArray_set)
    __swig_setmethods__["scaleX"] = _core.BufferType_scaleX_set
    __swig_getmethods__["scaleX"] = _core.BufferType_scaleX_get
    if _newclass:
        scaleX = _swig_property(_core.BufferType_scaleX_get, _core.BufferType_scaleX_set)
    __swig_setmethods__["scaleY"] = _core.BufferType_scaleY_set
    __swig_getmethods__["scaleY"] = _core.BufferType_scaleY_get
    if _newclass:
        scaleY = _swig_property(_core.BufferType_scaleY_get, _core.BufferType_scaleY_set)
    __swig_setmethods__["scaleI"] = _core.BufferType_scaleI_set
    __swig_getmethods__["scaleI"] = _core.BufferType_scaleI_get
    if _newclass:
        scaleI = _swig_property(_core.BufferType_scaleI_get, _core.BufferType_scaleI_set)
    __swig_setmethods__["bMaskArray"] = _core.BufferType_bMaskArray_set
    __swig_getmethods__["bMaskArray"] = _core.BufferType_bMaskArray_get
    if _newclass:
        bMaskArray = _swig_property(_core.BufferType_bMaskArray_get, _core.BufferType_bMaskArray_set)

    def __init__(self):
        this = _core.new_BufferType()
        try:
            self.this.append(this)
        except:
            self.this = this
    __swig_destroy__ = _core.delete_BufferType
    __del__ = lambda self: None
BufferType_swigregister = _core.BufferType_swigregister
BufferType_swigregister(BufferType)

class AttributeList(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, AttributeList, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, AttributeList, name)
    __repr__ = _swig_repr
    __swig_setmethods__["name"] = _core.AttributeList_name_set
    __swig_getmethods__["name"] = _core.AttributeList_name_get
    if _newclass:
        name = _swig_property(_core.AttributeList_name_get, _core.AttributeList_name_set)
    __swig_setmethods__["value"] = _core.AttributeList_value_set
    __swig_getmethods__["value"] = _core.AttributeList_value_get
    if _newclass:
        value = _swig_property(_core.AttributeList_value_get, _core.AttributeList_value_set)
    __swig_setmethods__["next"] = _core.AttributeList_next_set
    __swig_getmethods__["next"] = _core.AttributeList_next_get
    if _newclass:
        next = _swig_property(_core.AttributeList_next_get, _core.AttributeList_next_set)

    def __init__(self):
        this = _core.new_AttributeList()
        try:
            self.this.append(this)
        except:
            self.this = this
    __swig_destroy__ = _core.delete_AttributeList
    __del__ = lambda self: None
AttributeList_swigregister = _core.AttributeList_swigregister
AttributeList_swigregister(AttributeList)


_core.IMAGE_IMG_swigconstant(_core)
IMAGE_IMG = _core.IMAGE_IMG

_core.IMAGE_IMX_swigconstant(_core)
IMAGE_IMX = _core.IMAGE_IMX

_core.IMAGE_FLOAT_swigconstant(_core)
IMAGE_FLOAT = _core.IMAGE_FLOAT

_core.IMAGE_SPARSE_WORD_swigconstant(_core)
IMAGE_SPARSE_WORD = _core.IMAGE_SPARSE_WORD

_core.IMAGE_SPARSE_FLOAT_swigconstant(_core)
IMAGE_SPARSE_FLOAT = _core.IMAGE_SPARSE_FLOAT

_core.IMAGE_PACKED_WORD_swigconstant(_core)
IMAGE_PACKED_WORD = _core.IMAGE_PACKED_WORD

def Buffer_GetRowAddrAndSize(myBuffer, theRow, theRowLength):
    return _core.Buffer_GetRowAddrAndSize(myBuffer, theRow, theRowLength)
Buffer_GetRowAddrAndSize = _core.Buffer_GetRowAddrAndSize

def CreateBuffer(myBuffer, theNX, theNY, theNZ, theNF, isFloat, vectorGrid, imageSubType):
    return _core.CreateBuffer(myBuffer, theNX, theNY, theNZ, theNF, isFloat, vectorGrid, imageSubType)
CreateBuffer = _core.CreateBuffer

def SetBufferScale(theScale, theFactor, theOffset, theDesc, theUnit):
    return _core.SetBufferScale(theScale, theFactor, theOffset, theDesc, theUnit)
SetBufferScale = _core.SetBufferScale

def GetVectorComponents(imageSubType):
    return _core.GetVectorComponents(imageSubType)
GetVectorComponents = _core.GetVectorComponents

def DestroyBuffer(myBuffer):
    return _core.DestroyBuffer(myBuffer)
DestroyBuffer = _core.DestroyBuffer

def DestroyAttributeList(myList):
    return _core.DestroyAttributeList(myList)
DestroyAttributeList = _core.DestroyAttributeList

def SetAttribute(myList, theName, theValue):
    return _core.SetAttribute(myList, theName, theValue)
SetAttribute = _core.SetAttribute

def WriteScalesAsAttributes(theFile, p_pBuffer):
    return _core.WriteScalesAsAttributes(theFile, p_pBuffer)
WriteScalesAsAttributes = _core.WriteScalesAsAttributes

def WriteAttribute_END(theFile):
    return _core.WriteAttribute_END(theFile)
WriteAttribute_END = _core.WriteAttribute_END

def ReadImgAttributes(theFile, myList):
    return _core.ReadImgAttributes(theFile, myList)
ReadImgAttributes = _core.ReadImgAttributes

def WriteImgAttributes(theFile, isIM6, myList):
    return _core.WriteImgAttributes(theFile, isIM6, myList)
WriteImgAttributes = _core.WriteImgAttributes

def SCPackOldIMX_Read(theFile, myBuffer):
    return _core.SCPackOldIMX_Read(theFile, myBuffer)
SCPackOldIMX_Read = _core.SCPackOldIMX_Read

def WriteIMX(theFile, myBuffer):
    return _core.WriteIMX(theFile, myBuffer)
WriteIMX = _core.WriteIMX

def ReadIMX(theFileName, myBuffer, myList):
    return _core.ReadIMX(theFileName, myBuffer, myList)
ReadIMX = _core.ReadIMX

def WriteIMG(theFileName, myBuffer):
    return _core.WriteIMG(theFileName, myBuffer)
WriteIMG = _core.WriteIMG

def WriteIMGX(theFileName, isIMX, myBuffer):
    return _core.WriteIMGX(theFileName, isIMX, myBuffer)
WriteIMGX = _core.WriteIMGX

def WriteIMGXAttr(theFileName, isIMX, myBuffer, myList):
    return _core.WriteIMGXAttr(theFileName, isIMX, myBuffer, myList)
WriteIMGXAttr = _core.WriteIMGXAttr

_core.IMAGE_EXTRA_OFFSET_TAIL_swigconstant(_core)
IMAGE_EXTRA_OFFSET_TAIL = _core.IMAGE_EXTRA_OFFSET_TAIL

_core.IMAGE_EXTRA_2_swigconstant(_core)
IMAGE_EXTRA_2 = _core.IMAGE_EXTRA_2

_core.IMAGE_EXTRA_3_swigconstant(_core)
IMAGE_EXTRA_3 = _core.IMAGE_EXTRA_3
class Image_Header_7(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, Image_Header_7, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, Image_Header_7, name)
    __repr__ = _swig_repr
    __swig_setmethods__["version"] = _core.Image_Header_7_version_set
    __swig_getmethods__["version"] = _core.Image_Header_7_version_get
    if _newclass:
        version = _swig_property(_core.Image_Header_7_version_get, _core.Image_Header_7_version_set)
    __swig_setmethods__["pack_type"] = _core.Image_Header_7_pack_type_set
    __swig_getmethods__["pack_type"] = _core.Image_Header_7_pack_type_get
    if _newclass:
        pack_type = _swig_property(_core.Image_Header_7_pack_type_get, _core.Image_Header_7_pack_type_set)
    __swig_setmethods__["buffer_format"] = _core.Image_Header_7_buffer_format_set
    __swig_getmethods__["buffer_format"] = _core.Image_Header_7_buffer_format_get
    if _newclass:
        buffer_format = _swig_property(_core.Image_Header_7_buffer_format_get, _core.Image_Header_7_buffer_format_set)
    __swig_setmethods__["isSparse"] = _core.Image_Header_7_isSparse_set
    __swig_getmethods__["isSparse"] = _core.Image_Header_7_isSparse_get
    if _newclass:
        isSparse = _swig_property(_core.Image_Header_7_isSparse_get, _core.Image_Header_7_isSparse_set)
    __swig_setmethods__["sizeX"] = _core.Image_Header_7_sizeX_set
    __swig_getmethods__["sizeX"] = _core.Image_Header_7_sizeX_get
    if _newclass:
        sizeX = _swig_property(_core.Image_Header_7_sizeX_get, _core.Image_Header_7_sizeX_set)
    __swig_setmethods__["sizeY"] = _core.Image_Header_7_sizeY_set
    __swig_getmethods__["sizeY"] = _core.Image_Header_7_sizeY_get
    if _newclass:
        sizeY = _swig_property(_core.Image_Header_7_sizeY_get, _core.Image_Header_7_sizeY_set)
    __swig_setmethods__["sizeZ"] = _core.Image_Header_7_sizeZ_set
    __swig_getmethods__["sizeZ"] = _core.Image_Header_7_sizeZ_get
    if _newclass:
        sizeZ = _swig_property(_core.Image_Header_7_sizeZ_get, _core.Image_Header_7_sizeZ_set)
    __swig_setmethods__["sizeF"] = _core.Image_Header_7_sizeF_set
    __swig_getmethods__["sizeF"] = _core.Image_Header_7_sizeF_get
    if _newclass:
        sizeF = _swig_property(_core.Image_Header_7_sizeF_get, _core.Image_Header_7_sizeF_set)
    __swig_setmethods__["scalarN"] = _core.Image_Header_7_scalarN_set
    __swig_getmethods__["scalarN"] = _core.Image_Header_7_scalarN_get
    if _newclass:
        scalarN = _swig_property(_core.Image_Header_7_scalarN_get, _core.Image_Header_7_scalarN_set)
    __swig_setmethods__["vector_grid"] = _core.Image_Header_7_vector_grid_set
    __swig_getmethods__["vector_grid"] = _core.Image_Header_7_vector_grid_get
    if _newclass:
        vector_grid = _swig_property(_core.Image_Header_7_vector_grid_get, _core.Image_Header_7_vector_grid_set)
    __swig_setmethods__["extraFlags"] = _core.Image_Header_7_extraFlags_set
    __swig_getmethods__["extraFlags"] = _core.Image_Header_7_extraFlags_get
    if _newclass:
        extraFlags = _swig_property(_core.Image_Header_7_extraFlags_get, _core.Image_Header_7_extraFlags_set)
    __swig_setmethods__["reserved"] = _core.Image_Header_7_reserved_set
    __swig_getmethods__["reserved"] = _core.Image_Header_7_reserved_get
    if _newclass:
        reserved = _swig_property(_core.Image_Header_7_reserved_get, _core.Image_Header_7_reserved_set)

    def __init__(self):
        this = _core.new_Image_Header_7()
        try:
            self.this.append(this)
        except:
            self.this = this
    __swig_destroy__ = _core.delete_Image_Header_7
    __del__ = lambda self: None
Image_Header_7_swigregister = _core.Image_Header_7_swigregister
Image_Header_7_swigregister(Image_Header_7)

class Image_Tail_7(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, Image_Tail_7, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, Image_Tail_7, name)
    __repr__ = _swig_repr
    __swig_setmethods__["offset"] = _core.Image_Tail_7_offset_set
    __swig_getmethods__["offset"] = _core.Image_Tail_7_offset_get
    if _newclass:
        offset = _swig_property(_core.Image_Tail_7_offset_get, _core.Image_Tail_7_offset_set)

    def __init__(self):
        this = _core.new_Image_Tail_7()
        try:
            self.this.append(this)
        except:
            self.this = this
    __swig_destroy__ = _core.delete_Image_Tail_7
    __del__ = lambda self: None
Image_Tail_7_swigregister = _core.Image_Tail_7_swigregister
Image_Tail_7_swigregister(Image_Tail_7)


def ReadIM7(theFileName, myBuffer, myList):
    return _core.ReadIM7(theFileName, myBuffer, myList)
ReadIM7 = _core.ReadIM7

def WriteIM7(theFileName, isPackedIMX, myBuffer, myList):
    return _core.WriteIM7(theFileName, isPackedIMX, myBuffer, myList)
WriteIM7 = _core.WriteIM7

def ReadSpec(theFileName, myBuffer, allAtts):
    return _core.ReadSpec(theFileName, myBuffer, allAtts)
ReadSpec = _core.ReadSpec

def ReadSpec2(theFileName, myBuffer, myListin):
    return _core.ReadSpec2(theFileName, myBuffer, myListin)
ReadSpec2 = _core.ReadSpec2

def DestroyAttributeList2(myListin):
    return _core.DestroyAttributeList2(myListin)
DestroyAttributeList2 = _core.DestroyAttributeList2

def new_intp():
    return _core.new_intp()
new_intp = _core.new_intp

def copy_intp(value):
    return _core.copy_intp(value)
copy_intp = _core.copy_intp

def delete_intp(obj):
    return _core.delete_intp(obj)
delete_intp = _core.delete_intp

def intp_assign(obj, value):
    return _core.intp_assign(obj, value)
intp_assign = _core.intp_assign

def intp_value(obj):
    return _core.intp_value(obj)
intp_value = _core.intp_value

def new_floatp():
    return _core.new_floatp()
new_floatp = _core.new_floatp

def copy_floatp(value):
    return _core.copy_floatp(value)
copy_floatp = _core.copy_floatp

def delete_floatp(obj):
    return _core.delete_floatp(obj)
delete_floatp = _core.delete_floatp

def floatp_assign(obj, value):
    return _core.floatp_assign(obj, value)
floatp_assign = _core.floatp_assign

def floatp_value(obj):
    return _core.floatp_value(obj)
floatp_value = _core.floatp_value
class dPtr(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, dPtr, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, dPtr, name)
    __repr__ = _swig_repr

    def __init__(self):
        this = _core.new_dPtr()
        try:
            self.this.append(this)
        except:
            self.this = this
    __swig_destroy__ = _core.delete_dPtr
    __del__ = lambda self: None

    def assign(self, value):
        return _core.dPtr_assign(self, value)

    def value(self):
        return _core.dPtr_value(self)

    def cast(self):
        return _core.dPtr_cast(self)
    __swig_getmethods__["frompointer"] = lambda x: _core.dPtr_frompointer
    if _newclass:
        frompointer = staticmethod(_core.dPtr_frompointer)
dPtr_swigregister = _core.dPtr_swigregister
dPtr_swigregister(dPtr)

def dPtr_frompointer(t):
    return _core.dPtr_frompointer(t)
dPtr_frompointer = _core.dPtr_frompointer

class cPtr(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, cPtr, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, cPtr, name)
    __repr__ = _swig_repr

    def __init__(self):
        this = _core.new_cPtr()
        try:
            self.this.append(this)
        except:
            self.this = this
    __swig_destroy__ = _core.delete_cPtr
    __del__ = lambda self: None

    def assign(self, value):
        return _core.cPtr_assign(self, value)

    def value(self):
        return _core.cPtr_value(self)

    def cast(self):
        return _core.cPtr_cast(self)
    __swig_getmethods__["frompointer"] = lambda x: _core.cPtr_frompointer
    if _newclass:
        frompointer = staticmethod(_core.cPtr_frompointer)
cPtr_swigregister = _core.cPtr_swigregister
cPtr_swigregister(cPtr)

def cPtr_frompointer(t):
    return _core.cPtr_frompointer(t)
cPtr_frompointer = _core.cPtr_frompointer

class useintArray(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, useintArray, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, useintArray, name)
    __repr__ = _swig_repr

    def __init__(self, nelements):
        this = _core.new_useintArray(nelements)
        try:
            self.this.append(this)
        except:
            self.this = this
    __swig_destroy__ = _core.delete_useintArray
    __del__ = lambda self: None

    def __getitem__(self, index):
        return _core.useintArray___getitem__(self, index)

    def __setitem__(self, index, value):
        return _core.useintArray___setitem__(self, index, value)

    def cast(self):
        return _core.useintArray_cast(self)
    __swig_getmethods__["frompointer"] = lambda x: _core.useintArray_frompointer
    if _newclass:
        frompointer = staticmethod(_core.useintArray_frompointer)
useintArray_swigregister = _core.useintArray_swigregister
useintArray_swigregister(useintArray)

def useintArray_frompointer(t):
    return _core.useintArray_frompointer(t)
useintArray_frompointer = _core.useintArray_frompointer

class usefloatArray(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, usefloatArray, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, usefloatArray, name)
    __repr__ = _swig_repr

    def __init__(self, nelements):
        this = _core.new_usefloatArray(nelements)
        try:
            self.this.append(this)
        except:
            self.this = this
    __swig_destroy__ = _core.delete_usefloatArray
    __del__ = lambda self: None

    def __getitem__(self, index):
        return _core.usefloatArray___getitem__(self, index)

    def __setitem__(self, index, value):
        return _core.usefloatArray___setitem__(self, index, value)

    def cast(self):
        return _core.usefloatArray_cast(self)
    __swig_getmethods__["frompointer"] = lambda x: _core.usefloatArray_frompointer
    if _newclass:
        frompointer = staticmethod(_core.usefloatArray_frompointer)
usefloatArray_swigregister = _core.usefloatArray_swigregister
usefloatArray_swigregister(usefloatArray)

def usefloatArray_frompointer(t):
    return _core.usefloatArray_frompointer(t)
usefloatArray_frompointer = _core.usefloatArray_frompointer

class usedoubleArray(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, usedoubleArray, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, usedoubleArray, name)
    __repr__ = _swig_repr

    def __init__(self, nelements):
        this = _core.new_usedoubleArray(nelements)
        try:
            self.this.append(this)
        except:
            self.this = this
    __swig_destroy__ = _core.delete_usedoubleArray
    __del__ = lambda self: None

    def __getitem__(self, index):
        return _core.usedoubleArray___getitem__(self, index)

    def __setitem__(self, index, value):
        return _core.usedoubleArray___setitem__(self, index, value)

    def cast(self):
        return _core.usedoubleArray_cast(self)
    __swig_getmethods__["frompointer"] = lambda x: _core.usedoubleArray_frompointer
    if _newclass:
        frompointer = staticmethod(_core.usedoubleArray_frompointer)
usedoubleArray_swigregister = _core.usedoubleArray_swigregister
usedoubleArray_swigregister(usedoubleArray)

def usedoubleArray_frompointer(t):
    return _core.usedoubleArray_frompointer(t)
usedoubleArray_frompointer = _core.usedoubleArray_frompointer

# This file is compatible with both classic and new-style classes.


