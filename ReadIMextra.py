#!/usr/bin/env python
__metaclass__ = type

import ReadIM
import os
import ctypes
import numpy as np

class BunchMappable():
    """
    An object for iterative access to a mappable object. The keys must always
    be alpha_numeric
    """
    def __init__(self, mappable, immutable=False, str2num=None):
        """str2num can be a method for converting strings to numbers.
        val = str2num(val). Not the converter must return values even if it cannot convert.
        """
        self._immutable = immutable
        self._key = None

        super(BunchMappable, self).__setattr__('_mappable',mappable)

        if hasattr(mappable, 'items'):
            for key,val in mappable.items():
                if key.find('_') == 0:
                    continue #Skip intended hidden files
                if hasattr(val, 'items'):
                    self.__dict__[key] = self.__class__(val, immutable=immutable, str2num=str2num)
                else:
                    if str2num is None:
                        self.__dict__[key] = val
                    else:
                        self.__dict__[key] = str2num(val)


    def __repr__(self):
            return repr(self._mappable)

    def __str__(self):
        rep = ''
        for key, val in self.__dict__.items():
            rep = rep + key + '\n'
        return '\n'.join(self.__dict__)

    def __len__(self):
        return len(self.__dict__)

    def __getitem__(self, key):
        if not key in self.__dict__:
            parent = self._mappable
            depth = 1
            while True:
                try:
                    parent = parent._mappable
                    depth += 1
                except AttributeError:
                    break
            raise KeyError, 'Key "{0}" is missing from:"{1}"at depth={2}'.format(key, parent, depth)

        obj = self.__dict__[key]
        try:
            super(obj.__class__, obj).__setattr__('_key', key) #track the key
        except:
            pass
        return obj

    def __iter__(self):
        for key in sorted(self._mappable.keys()):
            yield key

    def __setattr__(self,name, value):
        if name in ['_immutable', '_key']:
            super(BunchMappable, self).__setattr__(name,value)
        elif self._immutable:
            raise AttributeError, 'This Object is immutable'
        else:

            if name in self._mappable:
                self._mappable[name] = value
                try:
                    object.__setattr__(self, name, value)
                except AttributeError:
                    pass

    def get(self, key):
        if key in self:
            return self[key]


class ScaleTypeAlt(BunchMappable):
    def __init__(self, scale):
        if isinstance(scale, BunchMappable):
            mappings = scale.__dict__
        else:
            mappings = dict(
                        description = scale.description,
                        factor      = scale.factor,
                        offset      = scale.offset,
                        unit        = scale.unit,
                        )
        super(ScaleTypeAlt, self).__init__(mappings)

class BufferTypeAlt(BunchMappable):
    """ bufferType designed to replicate davis buffer type so that it is free of swig
    """

    def __init__(self, buff, DestroyBuffer = True, immutable=False, str2num=None):

        if isinstance(buff, ReadIM.BufferType):

            mappings = dict(
                        image_sub_type = buff.image_sub_type,
                        nf = int(buff.nf),
                        nx = int(buff.nx),
                        ny = int(buff.ny),
                        nz = int(buff.nz),
                        isFloat = buff.isFloat,
                        vectorGrid = int(buff.vectorGrid),
                        scaleX = ScaleTypeAlt(buff.scaleX).__dict__,
                        scaleY = ScaleTypeAlt(buff.scaleY).__dict__,
                        scaleI = ScaleTypeAlt(buff.scaleI).__dict__,
                        totalLines = buff.totalLines)

        elif isinstance(buff, BufferTypeAlt):
            # make a copy
            mappings = {}
            mappings.update(buff._mappable)

        elif isinstance(buff, dict):
            mappings= buff

        elif isinstance(buff, BunchMappable):
            mappings = {}
            obj2dict(buff, mappings) # tidy up

        else:
            raise TypeError, 'Type of buffer not recognised!\n%s' % repr(buff)

        super(BufferTypeAlt, self).__init__(mappings, immutable=immutable, str2num=str2num)

        # cleanup
        if (type(buff) == ReadIM.BufferType) and DestroyBuffer:
            ReadIM.DestroyBuffer(buff)

def obj2dict(obj, d):
    """ return a nested dictionary of all non hidden attributes
        of the obj as a nested dictionary of the same structure
    """
    for key, val in obj.__dict__.items():
        if hasattr(val, '__dict__'):
            d[key] = {}
            obj2dict(val,d[key])
        # no hidden objects
        elif not key.find('_') == 0:
            d[key]=val


def createBuffer(b):
    """ creates a buffer in memory for an existing ReadIm.BufferType
        using the ReadIM.CreatBuffer() method
    b must be an instance of a buffer ie. b = ReadIM.BufferType()
    attributes assigned are:  b, b.nx ,b.ny, b.nz, b.nf,
                              b.isFloat, b.vectorGrid, b.image_sub_type
    return error_code
    """
    return ReadIM.CreateBuffer(b, b.nx ,b.ny, b.nz, b.nf,
                        b.isFloat, b.vectorGrid, b.image_sub_type)

def createBuffer_davis(buff):
    """
    creates
    return b, error_code
    """
    b = ReadIM.BufferType()
    b.nx = buff.nx
    b.ny = buff.ny
    b.nz = buff.nz
    b.nf = buff.nf
    b.isFloat = buff.isFloat
    b.vectorGrid = buff.vectorGrid
    b.image_sub_type = buff.image_sub_type
    error_code = ReadIM.CreateBuffer(b, b.nx ,b.ny, b.nz, b.nf,
                        b.isFloat, b.vectorGrid, b.image_sub_type)

    #transfer buffer info from v. Useful for writing files.
    for a in buff.__dict__:
        if a.find('scale') == 0:
            for aa in ['description','unit','factor','offset']:
                exec('b.%s.%s=buff.%s.%s'%tuple([a,aa]*2))

    return b, error_code

def get_Buffer_andAttributeList(filename, buff=None,atts=None):
    """ return the buffer and attributes for the file, returns an active buffer
        and attribute_list
        Both of which which need to eventually be destroyed (otherwise memory leaks)

        ReadIM.DestroyBuffer(buff)
        ReadIM.DestroyAttributeList2(atttributes.next)
    """
    if not os.path.isfile(filename): raise IOError, 'file not found %s' %filename

    if buff is None: buff = ReadIM.BufferType()
    if atts is None: atts = ReadIM.AttributeList()

    try:
        err = ReadIM.ReadSpec2(filename, buff, atts)
    except:
        ReadIM.DestroyBuffer(buffer)

    if True:
        if err == ReadIM.IMREAD_ERR_FILEOPEN: raise IOError, 'File not found'
        elif err == ReadIM.IMREAD_ERR_HEADER: raise IOError,'Error in header'
        elif err == ReadIM.IMREAD_ERR_FORMAT: raise IOError, 'Error in format'
        elif err == ReadIM.IMREAD_ERR_DATA:   raise IOError, 'Error while reading data'
        elif err == ReadIM.IMREAD_ERR_MEMORY: raise IOError, 'Error out of memory'
        elif err > 0: raise IOError, 'Unkown Error code: %s' % err

    return buff, atts

def __newBuffer__(window ,nx=None, ny=None, vectorGrid=24,
                     image_sub_type=ReadIM.BUFFER_FORMAT_VECTOR_2D,
                     frames=1,scaleIoffset=0, scaleIfactor=1, alternate_buff=False):

    """ window [(x,y),(x,y)] --> [top left, bottom right]
    """

    if not nx:
        nx = window[1][0] - window[0][0]
    if not ny:
        ny = window[0][1] - window[1][1]

    buff = ReadIM.BufferType()

    buff.image_sub_type = int(image_sub_type)
    buff.nx = int(nx)
    buff.ny = int(ny) # * compN[buff.image_sub_type]
    buff.nz = 1
    buff.nf = int(frames)
    buff.isFloat = 1
    buff.vectorGrid = int(vectorGrid)

    buff.scaleX.offset = float(window[0][0])
    buff.scaleY.offset = float(window[0][1])
    buff.scaleX.factor = float(window[1][0] - buff.scaleX.offset)/nx/vectorGrid
    buff.scaleY.factor = float(window[1][1] - buff.scaleY.offset)/ny/vectorGrid
    buff.scaleI.offset = float(scaleIoffset)
    buff.scaleI.factor = float(scaleIfactor)

    if alternate_buff:
        buff = BufferTypeAlt(buff)

    return buff

def newBuffer(window ,nx=None, ny=None, vectorGrid=24, image_sub_type=ReadIM.BUFFER_FORMAT_VECTOR_2D, frames=1, alternate_buff=True):
    """
    window [(x,y),(x,y)] --> [top left, bottom right]
    Returns a compliant buffertype with alternate format
    """

    buff = __newBuffer__(window, nx , ny, vectorGrid, image_sub_type, frames, alternate_buff)
    altbuff =  BufferTypeAlt(buff)

    return altbuff

def load_AttributeList(atts={}):
    """
    load the dictionary into a ReadIM.AttributeList
    AttributeList = loadAttributeList(dict)

     AttributeList needs to eventually be destroyed (otherwise memory leaks)
     ReadIM.DestroyAttributeList2(Attatttributesxt)
    """
    attlist = ReadIM.AttributeList()
    a = attlist

    for key in atts:
        a.next  = ReadIM.AttributeList()
        a       = a.next
        a.name  = key
        a.value = str(atts[key])

    return attlist

def buffer_as_array(buff):

    """
    returns the entire buffer as an array
    first axis is like a frame (sometimes there are multiple frames)
    [offset::dims] will return all the components for an axis

    a, buff = np.array([components*nf,nx,ny]), ReadIM.BufferType
    where: components = ReadIM.GetVectorComponents(buff.image_sub_type) * buff.nf

    you must destroy buff manually with ReadIM.DestroyBuffer(buff) also del(a) is necessary

    suitable for BufferTypeAlt objects and writing data.
    """

    if type(buff) is BufferTypeAlt:
        buff, err = createBuffer_davis(buff)

    if buff.wordArray:
        pA = ctypes.cast( buff.wordArray.__long__(), ctypes.POINTER( ctypes.c_ushort) )
    elif buff.floatArray:
        pA = ctypes.cast( buff.floatArray.__long__(), ctypes.POINTER( ctypes.c_float) )
    else:
        raise MemoryError, 'No buffer available'

    if buff.image_sub_type > 0:
        components = ReadIM.GetVectorComponents(buff.image_sub_type)
    else:
        components = 1 # for images at the moment
    components *= buff.nf
    a = np.ctypeslib.as_array(pA,(components,buff.ny,buff.nx)) #updated 22/5/11
    return a, buff

def buffer_mask_as_array(buff):

    """
    returns the buffer mask (DaVis V8 files) as an array
    first axis is like a frame (sometimes there are multiple frames)
    [offset::dims] will return all the components for an axis

    a, buff = np.array([components*nf,nx,ny]), ReadIM.BufferType
    where: components = ReadIM.GetVectorComponents(buff.image_sub_type) * buff.nf

    you must destroy buff manually with ReadIM.DestroyBuffer(buff) also del(a) is necessary

    suitable for BufferTypeAlt objects and writing data.
    """

    if type(buff) is BufferTypeAlt:
        buff, err = createBuffer_davis(buff)

    if buff.bMaskArray:
        pA = ctypes.cast( buff.bMaskArray.__long__(), ctypes.POINTER( ctypes.c_bool))
        a = np.ctypeslib.as_array(pA,(buff.nf,buff.ny,buff.nx)) #updated 22/5/11
    else:
        a = None
    return a, buff

def att2dict(att, destroy=True):
    """ Convert an Attribute list to a dictionary
    """
    out = {}
    attn = att.next
    while attn:
        out[attn.name] = attn.value
        attn = attn.next
    if att.next and destroy:
        ReadIM.DestroyAttributeList2(att.next)
    return out

