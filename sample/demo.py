import glob
import ReadIMextra

vecfile = glob.glob('*.vc7')[0]
imfile = glob.glob('*.im7')[0]


# vector demo (two components)

vbuff, vatts=  ReadIMextra.get_Buffer_andAttributeList(vecfile)
v_array, vbuff = ReadIMextra.buffer_as_array(vbuff)


print 'attributes in %s\n' %vecfile,'-'*100,'\n',ReadIMextra.att2dict(vatts),'\n'*10

# image demo (two frames)

imbuff, imatts  =  ReadIMextra.get_Buffer_andAttributeList(imfile)
i_array, ibuff     = ReadIMextra.buffer_as_array(imbuff)

print 'attributes in %s\n' %imfile,'_'*100,'\n', ReadIMextra.att2dict(imatts)


# display all of buffer available.
from pylab import *

for i in range(v_array.shape[0]/2):
    figure()
    quiver(v_array[i], v_array[i+1])

for i in range(i_array.shape[0]):
    figure()
    imshow(i_array[i])


# note you will have to destroy the buffers when you are done.
ReadIMextra.ReadIM.DestroyBuffer(vbuff)
ReadIMextra.ReadIM.DestroyBuffer(ibuff)
