# This file was automatically generated by SWIG (http://www.swig.org).
# Version 1.3.40
#
# Do not make changes to this file unless you know what you are doing--modify
# the SWIG interface file instead.

from sys import version_info
if version_info >= (2,6,0):
    def swig_import_helper():
        from os.path import dirname
        import imp
        fp = None
        try:
            fp, pathname, description = imp.find_module('_ReadIM', [dirname(__file__)])
        except ImportError:
            import _ReadIM
            return _ReadIM
        if fp is not None:
            try:
                _mod = imp.load_module('_ReadIM', fp, pathname, description)
            finally:
                fp.close()
            return _mod
    _ReadIM = swig_import_helper()
    del swig_import_helper
else:
    import _ReadIM
del version_info
try:
    _swig_property = property
except NameError:
    pass # Python < 2.2 doesn't have 'property'.
def _swig_setattr_nondynamic(self,class_type,name,value,static=1):
    if (name == "thisown"): return self.this.own(value)
    if (name == "this"):
        if type(value).__name__ == 'SwigPyObject':
            self.__dict__[name] = value
            return
    method = class_type.__swig_setmethods__.get(name,None)
    if method: return method(self,value)
    if (not static) or hasattr(self,name):
        self.__dict__[name] = value
    else:
        raise AttributeError("You cannot add attributes to %s" % self)

def _swig_setattr(self,class_type,name,value):
    return _swig_setattr_nondynamic(self,class_type,name,value,0)

def _swig_getattr(self,class_type,name):
    if (name == "thisown"): return self.this.own()
    method = class_type.__swig_getmethods__.get(name,None)
    if method: return method(self)
    raise AttributeError(name)

def _swig_repr(self):
    try: strthis = "proxy of " + self.this.__repr__()
    except: strthis = ""
    return "<%s.%s; %s >" % (self.__class__.__module__, self.__class__.__name__, strthis,)

try:
    _object = object
    _newclass = 1
except AttributeError:
    class _object : pass
    _newclass = 0


def _swig_setattr_nondynamic_method(set):
    def set_attr(self,name,value):
        if (name == "thisown"): return self.this.own(value)
        if hasattr(self,name) or (name == "this"):
            set(self,name,value)
        else:
            raise AttributeError("You cannot add attributes to %s" % self)
    return set_attr


IMREAD_ERR_NO = _ReadIM.IMREAD_ERR_NO
IMREAD_ERR_FILEOPEN = _ReadIM.IMREAD_ERR_FILEOPEN
IMREAD_ERR_HEADER = _ReadIM.IMREAD_ERR_HEADER
IMREAD_ERR_FORMAT = _ReadIM.IMREAD_ERR_FORMAT
IMREAD_ERR_DATA = _ReadIM.IMREAD_ERR_DATA
IMREAD_ERR_MEMORY = _ReadIM.IMREAD_ERR_MEMORY
class BufferScaleType(object):
    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    __repr__ = _swig_repr
    factor = _swig_property(_ReadIM.BufferScaleType_factor_get, _ReadIM.BufferScaleType_factor_set)
    offset = _swig_property(_ReadIM.BufferScaleType_offset_get, _ReadIM.BufferScaleType_offset_set)
    description = _swig_property(_ReadIM.BufferScaleType_description_get, _ReadIM.BufferScaleType_description_set)
    unit = _swig_property(_ReadIM.BufferScaleType_unit_get, _ReadIM.BufferScaleType_unit_set)
    def __init__(self): 
        this = _ReadIM.new_BufferScaleType()
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _ReadIM.delete_BufferScaleType
    __del__ = lambda self : None;
BufferScaleType_swigregister = _ReadIM.BufferScaleType_swigregister
BufferScaleType_swigregister(BufferScaleType)

BUFFER_FORMAT__NOTUSED = _ReadIM.BUFFER_FORMAT__NOTUSED
BUFFER_FORMAT_MEMPACKWORD = _ReadIM.BUFFER_FORMAT_MEMPACKWORD
BUFFER_FORMAT_FLOAT = _ReadIM.BUFFER_FORMAT_FLOAT
BUFFER_FORMAT_WORD = _ReadIM.BUFFER_FORMAT_WORD
BUFFER_FORMAT_DOUBLE = _ReadIM.BUFFER_FORMAT_DOUBLE
BUFFER_FORMAT_FLOAT_VALID = _ReadIM.BUFFER_FORMAT_FLOAT_VALID
BUFFER_FORMAT_IMAGE = _ReadIM.BUFFER_FORMAT_IMAGE
BUFFER_FORMAT_VECTOR_2D_EXTENDED = _ReadIM.BUFFER_FORMAT_VECTOR_2D_EXTENDED
BUFFER_FORMAT_VECTOR_2D = _ReadIM.BUFFER_FORMAT_VECTOR_2D
BUFFER_FORMAT_VECTOR_2D_EXTENDED_PEAK = _ReadIM.BUFFER_FORMAT_VECTOR_2D_EXTENDED_PEAK
BUFFER_FORMAT_VECTOR_3D = _ReadIM.BUFFER_FORMAT_VECTOR_3D
BUFFER_FORMAT_VECTOR_3D_EXTENDED_PEAK = _ReadIM.BUFFER_FORMAT_VECTOR_3D_EXTENDED_PEAK
BUFFER_FORMAT_COLOR = _ReadIM.BUFFER_FORMAT_COLOR
BUFFER_FORMAT_RGB_MATRIX = _ReadIM.BUFFER_FORMAT_RGB_MATRIX
BUFFER_FORMAT_RGB_32 = _ReadIM.BUFFER_FORMAT_RGB_32
class BufferType(object):
    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    __repr__ = _swig_repr
    isFloat = _swig_property(_ReadIM.BufferType_isFloat_get, _ReadIM.BufferType_isFloat_set)
    nx = _swig_property(_ReadIM.BufferType_nx_get, _ReadIM.BufferType_nx_set)
    ny = _swig_property(_ReadIM.BufferType_ny_get, _ReadIM.BufferType_ny_set)
    nz = _swig_property(_ReadIM.BufferType_nz_get, _ReadIM.BufferType_nz_set)
    nf = _swig_property(_ReadIM.BufferType_nf_get, _ReadIM.BufferType_nf_set)
    totalLines = _swig_property(_ReadIM.BufferType_totalLines_get, _ReadIM.BufferType_totalLines_set)
    vectorGrid = _swig_property(_ReadIM.BufferType_vectorGrid_get, _ReadIM.BufferType_vectorGrid_set)
    image_sub_type = _swig_property(_ReadIM.BufferType_image_sub_type_get, _ReadIM.BufferType_image_sub_type_set)
    floatArray = _swig_property(_ReadIM.BufferType_floatArray_get, _ReadIM.BufferType_floatArray_set)
    wordArray = _swig_property(_ReadIM.BufferType_wordArray_get, _ReadIM.BufferType_wordArray_set)
    scaleX = _swig_property(_ReadIM.BufferType_scaleX_get, _ReadIM.BufferType_scaleX_set)
    scaleY = _swig_property(_ReadIM.BufferType_scaleY_get, _ReadIM.BufferType_scaleY_set)
    scaleI = _swig_property(_ReadIM.BufferType_scaleI_get, _ReadIM.BufferType_scaleI_set)
    bMaskArray = _swig_property(_ReadIM.BufferType_bMaskArray_get, _ReadIM.BufferType_bMaskArray_set)
    def __init__(self): 
        this = _ReadIM.new_BufferType()
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _ReadIM.delete_BufferType
    __del__ = lambda self : None;
BufferType_swigregister = _ReadIM.BufferType_swigregister
BufferType_swigregister(BufferType)

class AttributeList(object):
    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    __repr__ = _swig_repr
    name = _swig_property(_ReadIM.AttributeList_name_get, _ReadIM.AttributeList_name_set)
    value = _swig_property(_ReadIM.AttributeList_value_get, _ReadIM.AttributeList_value_set)
    next = _swig_property(_ReadIM.AttributeList_next_get, _ReadIM.AttributeList_next_set)
    def __init__(self): 
        this = _ReadIM.new_AttributeList()
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _ReadIM.delete_AttributeList
    __del__ = lambda self : None;
AttributeList_swigregister = _ReadIM.AttributeList_swigregister
AttributeList_swigregister(AttributeList)

IMAGE_IMG = _ReadIM.IMAGE_IMG
IMAGE_IMX = _ReadIM.IMAGE_IMX
IMAGE_FLOAT = _ReadIM.IMAGE_FLOAT
IMAGE_SPARSE_WORD = _ReadIM.IMAGE_SPARSE_WORD
IMAGE_SPARSE_FLOAT = _ReadIM.IMAGE_SPARSE_FLOAT
IMAGE_PACKED_WORD = _ReadIM.IMAGE_PACKED_WORD

def Buffer_GetRowAddrAndSize(*args):
  return _ReadIM.Buffer_GetRowAddrAndSize(*args)
Buffer_GetRowAddrAndSize = _ReadIM.Buffer_GetRowAddrAndSize

def CreateBuffer(*args):
  return _ReadIM.CreateBuffer(*args)
CreateBuffer = _ReadIM.CreateBuffer

def SetBufferScale(*args):
  return _ReadIM.SetBufferScale(*args)
SetBufferScale = _ReadIM.SetBufferScale

def GetVectorComponents(*args):
  return _ReadIM.GetVectorComponents(*args)
GetVectorComponents = _ReadIM.GetVectorComponents

def DestroyBuffer(*args):
  return _ReadIM.DestroyBuffer(*args)
DestroyBuffer = _ReadIM.DestroyBuffer

def DestroyAttributeList(*args):
  return _ReadIM.DestroyAttributeList(*args)
DestroyAttributeList = _ReadIM.DestroyAttributeList

def SetAttribute(*args):
  return _ReadIM.SetAttribute(*args)
SetAttribute = _ReadIM.SetAttribute

def WriteScalesAsAttributes(*args):
  return _ReadIM.WriteScalesAsAttributes(*args)
WriteScalesAsAttributes = _ReadIM.WriteScalesAsAttributes

def WriteAttribute_END(*args):
  return _ReadIM.WriteAttribute_END(*args)
WriteAttribute_END = _ReadIM.WriteAttribute_END

def ReadImgAttributes(*args):
  return _ReadIM.ReadImgAttributes(*args)
ReadImgAttributes = _ReadIM.ReadImgAttributes

def WriteImgAttributes(*args):
  return _ReadIM.WriteImgAttributes(*args)
WriteImgAttributes = _ReadIM.WriteImgAttributes

def SCPackOldIMX_Read(*args):
  return _ReadIM.SCPackOldIMX_Read(*args)
SCPackOldIMX_Read = _ReadIM.SCPackOldIMX_Read

def WriteIMX(*args):
  return _ReadIM.WriteIMX(*args)
WriteIMX = _ReadIM.WriteIMX

def ReadIMX(*args):
  return _ReadIM.ReadIMX(*args)
ReadIMX = _ReadIM.ReadIMX

def WriteIMG(*args):
  return _ReadIM.WriteIMG(*args)
WriteIMG = _ReadIM.WriteIMG

def WriteIMGX(*args):
  return _ReadIM.WriteIMGX(*args)
WriteIMGX = _ReadIM.WriteIMGX

def WriteIMGXAttr(*args):
  return _ReadIM.WriteIMGXAttr(*args)
WriteIMGXAttr = _ReadIM.WriteIMGXAttr
IMAGE_EXTRA_OFFSET_TAIL = _ReadIM.IMAGE_EXTRA_OFFSET_TAIL
IMAGE_EXTRA_2 = _ReadIM.IMAGE_EXTRA_2
IMAGE_EXTRA_3 = _ReadIM.IMAGE_EXTRA_3
class Image_Header_7(object):
    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    __repr__ = _swig_repr
    version = _swig_property(_ReadIM.Image_Header_7_version_get, _ReadIM.Image_Header_7_version_set)
    pack_type = _swig_property(_ReadIM.Image_Header_7_pack_type_get, _ReadIM.Image_Header_7_pack_type_set)
    buffer_format = _swig_property(_ReadIM.Image_Header_7_buffer_format_get, _ReadIM.Image_Header_7_buffer_format_set)
    isSparse = _swig_property(_ReadIM.Image_Header_7_isSparse_get, _ReadIM.Image_Header_7_isSparse_set)
    sizeX = _swig_property(_ReadIM.Image_Header_7_sizeX_get, _ReadIM.Image_Header_7_sizeX_set)
    sizeY = _swig_property(_ReadIM.Image_Header_7_sizeY_get, _ReadIM.Image_Header_7_sizeY_set)
    sizeZ = _swig_property(_ReadIM.Image_Header_7_sizeZ_get, _ReadIM.Image_Header_7_sizeZ_set)
    sizeF = _swig_property(_ReadIM.Image_Header_7_sizeF_get, _ReadIM.Image_Header_7_sizeF_set)
    scalarN = _swig_property(_ReadIM.Image_Header_7_scalarN_get, _ReadIM.Image_Header_7_scalarN_set)
    vector_grid = _swig_property(_ReadIM.Image_Header_7_vector_grid_get, _ReadIM.Image_Header_7_vector_grid_set)
    extraFlags = _swig_property(_ReadIM.Image_Header_7_extraFlags_get, _ReadIM.Image_Header_7_extraFlags_set)
    reserved = _swig_property(_ReadIM.Image_Header_7_reserved_get, _ReadIM.Image_Header_7_reserved_set)
    def __init__(self): 
        this = _ReadIM.new_Image_Header_7()
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _ReadIM.delete_Image_Header_7
    __del__ = lambda self : None;
Image_Header_7_swigregister = _ReadIM.Image_Header_7_swigregister
Image_Header_7_swigregister(Image_Header_7)

class Image_Tail_7(object):
    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    __repr__ = _swig_repr
    offset = _swig_property(_ReadIM.Image_Tail_7_offset_get, _ReadIM.Image_Tail_7_offset_set)
    def __init__(self): 
        this = _ReadIM.new_Image_Tail_7()
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _ReadIM.delete_Image_Tail_7
    __del__ = lambda self : None;
Image_Tail_7_swigregister = _ReadIM.Image_Tail_7_swigregister
Image_Tail_7_swigregister(Image_Tail_7)


def ReadIM7(*args):
  return _ReadIM.ReadIM7(*args)
ReadIM7 = _ReadIM.ReadIM7

def WriteIM7(*args):
  return _ReadIM.WriteIM7(*args)
WriteIM7 = _ReadIM.WriteIM7

def ReadSpec(*args):
  return _ReadIM.ReadSpec(*args)
ReadSpec = _ReadIM.ReadSpec

def ReadSpec2(*args):
  return _ReadIM.ReadSpec2(*args)
ReadSpec2 = _ReadIM.ReadSpec2

def DestroyAttributeList2(*args):
  return _ReadIM.DestroyAttributeList2(*args)
DestroyAttributeList2 = _ReadIM.DestroyAttributeList2

def new_intp():
  return _ReadIM.new_intp()
new_intp = _ReadIM.new_intp

def copy_intp(*args):
  return _ReadIM.copy_intp(*args)
copy_intp = _ReadIM.copy_intp

def delete_intp(*args):
  return _ReadIM.delete_intp(*args)
delete_intp = _ReadIM.delete_intp

def intp_assign(*args):
  return _ReadIM.intp_assign(*args)
intp_assign = _ReadIM.intp_assign

def intp_value(*args):
  return _ReadIM.intp_value(*args)
intp_value = _ReadIM.intp_value

def new_floatp():
  return _ReadIM.new_floatp()
new_floatp = _ReadIM.new_floatp

def copy_floatp(*args):
  return _ReadIM.copy_floatp(*args)
copy_floatp = _ReadIM.copy_floatp

def delete_floatp(*args):
  return _ReadIM.delete_floatp(*args)
delete_floatp = _ReadIM.delete_floatp

def floatp_assign(*args):
  return _ReadIM.floatp_assign(*args)
floatp_assign = _ReadIM.floatp_assign

def floatp_value(*args):
  return _ReadIM.floatp_value(*args)
floatp_value = _ReadIM.floatp_value
class dPtr(object):
    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    __repr__ = _swig_repr
    def __init__(self): 
        this = _ReadIM.new_dPtr()
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _ReadIM.delete_dPtr
    __del__ = lambda self : None;
    def assign(self, *args): return _ReadIM.dPtr_assign(self, *args)
    def value(self): return _ReadIM.dPtr_value(self)
    def cast(self): return _ReadIM.dPtr_cast(self)
    frompointer = staticmethod(_ReadIM.dPtr_frompointer)
dPtr_swigregister = _ReadIM.dPtr_swigregister
dPtr_swigregister(dPtr)

def dPtr_frompointer(*args):
  return _ReadIM.dPtr_frompointer(*args)
dPtr_frompointer = _ReadIM.dPtr_frompointer

class cPtr(object):
    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    __repr__ = _swig_repr
    def __init__(self): 
        this = _ReadIM.new_cPtr()
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _ReadIM.delete_cPtr
    __del__ = lambda self : None;
    def assign(self, *args): return _ReadIM.cPtr_assign(self, *args)
    def value(self): return _ReadIM.cPtr_value(self)
    def cast(self): return _ReadIM.cPtr_cast(self)
    frompointer = staticmethod(_ReadIM.cPtr_frompointer)
cPtr_swigregister = _ReadIM.cPtr_swigregister
cPtr_swigregister(cPtr)

def cPtr_frompointer(*args):
  return _ReadIM.cPtr_frompointer(*args)
cPtr_frompointer = _ReadIM.cPtr_frompointer

class useintArray(object):
    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    __repr__ = _swig_repr
    def __init__(self, *args): 
        this = _ReadIM.new_useintArray(*args)
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _ReadIM.delete_useintArray
    __del__ = lambda self : None;
    def __getitem__(self, *args): return _ReadIM.useintArray___getitem__(self, *args)
    def __setitem__(self, *args): return _ReadIM.useintArray___setitem__(self, *args)
    def cast(self): return _ReadIM.useintArray_cast(self)
    frompointer = staticmethod(_ReadIM.useintArray_frompointer)
useintArray_swigregister = _ReadIM.useintArray_swigregister
useintArray_swigregister(useintArray)

def useintArray_frompointer(*args):
  return _ReadIM.useintArray_frompointer(*args)
useintArray_frompointer = _ReadIM.useintArray_frompointer

class usefloatArray(object):
    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    __repr__ = _swig_repr
    def __init__(self, *args): 
        this = _ReadIM.new_usefloatArray(*args)
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _ReadIM.delete_usefloatArray
    __del__ = lambda self : None;
    def __getitem__(self, *args): return _ReadIM.usefloatArray___getitem__(self, *args)
    def __setitem__(self, *args): return _ReadIM.usefloatArray___setitem__(self, *args)
    def cast(self): return _ReadIM.usefloatArray_cast(self)
    frompointer = staticmethod(_ReadIM.usefloatArray_frompointer)
usefloatArray_swigregister = _ReadIM.usefloatArray_swigregister
usefloatArray_swigregister(usefloatArray)

def usefloatArray_frompointer(*args):
  return _ReadIM.usefloatArray_frompointer(*args)
usefloatArray_frompointer = _ReadIM.usefloatArray_frompointer

class usedoubleArray(object):
    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    __repr__ = _swig_repr
    def __init__(self, *args): 
        this = _ReadIM.new_usedoubleArray(*args)
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _ReadIM.delete_usedoubleArray
    __del__ = lambda self : None;
    def __getitem__(self, *args): return _ReadIM.usedoubleArray___getitem__(self, *args)
    def __setitem__(self, *args): return _ReadIM.usedoubleArray___setitem__(self, *args)
    def cast(self): return _ReadIM.usedoubleArray_cast(self)
    frompointer = staticmethod(_ReadIM.usedoubleArray_frompointer)
usedoubleArray_swigregister = _ReadIM.usedoubleArray_swigregister
usedoubleArray_swigregister(usedoubleArray)

def usedoubleArray_frompointer(*args):
  return _ReadIM.usedoubleArray_frompointer(*args)
usedoubleArray_frompointer = _ReadIM.usedoubleArray_frompointer



