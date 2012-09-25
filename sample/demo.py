# Assumes that sample files B00001.im7 and B00001.VC7 are in the same folder as this file.

import glob
import ReadIMextra
import ReadIM
import os

vecfile = glob.glob('*.vc7')[0]
imfile = glob.glob('*.im7')[0]


# vector demo (two components)

vbuff, vatts=  ReadIMextra.get_Buffer_andAttributeList(vecfile)
v_array, vbuff = ReadIMextra.buffer_as_array(vbuff)


print 'attributes in %s\n' %vecfile,'-'*100,'\n',ReadIMextra.att2dict(vatts, False),'\n'*10

# image demo (two frames)

imbuff, imatts  =  ReadIMextra.get_Buffer_andAttributeList(imfile)
i_array, ibuff     = ReadIMextra.buffer_as_array(imbuff)

print 'attributes in %s\n' %imfile,'_'*100,'\n', ReadIMextra.att2dict(imatts, False)


# display all of buffer available.
from pylab import *

for i in range(v_array.shape[0]/2):
    figure()
    quiver(v_array[i], v_array[i+1])

for i in range(i_array.shape[0]):
    figure()
    imshow(i_array[i])


# to write new files

dst_v = os.path.abspath('new.vc7')
dst_im = os.path.abspath('new.im7')

res = ReadIM.WriteIM7(dst_v, True, vbuff, vatts.next)
res1 = ReadIM.WriteIM7(dst_im, True, imbuff, imatts.next)


# note you will have to destroy the buffers when you are done using: But you need to make sure they have not already been destroyed
##ReadIMextra.ReadIM.DestroyBuffer(vbuff)
##ReadIMextra.ReadIM.DestroyBuffer(imbuff)


