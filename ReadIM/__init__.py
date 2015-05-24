from . import core
from . import extra

# collect buffer fommats together
BUFFER_FORMATS = {}
for s in dir(core):
    if s.find('BUFFER_FORMAT') == 0:
        BUFFER_FORMATS[getattr(core, s)] = s

# collect error codes
ERROR_CODES = {}
for s in dir(core):
    if s.find('IMREAD_ERR') == 0:
        ERROR_CODES[getattr(core,s)] = s


from .core import   (BufferType, BufferScaleType, AttributeList,
                    CreateBuffer, DestroyBuffer, DestroyAttributeList,
                    ReadIM7, WriteIM7, GetVectorComponents, SetBufferScale,
                    SetAttribute)
