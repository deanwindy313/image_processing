# -*- coding: utf-8 -*-
"""
Created on Thu Sep 28 14:55:05 2023

@author: deanw
"""
import skimage 
from skimage import io
import numpy as np
import matplotlib.pyplot as plt

class Exception1(BaseException):
    
    pass
class Exception2(BaseException):
    pass

def scanLine4e(f,loc,L='column'):
   try:
        r,c=f.shape 
        if L=='column':
            if loc<c:
                l=f[:,loc]
                return l
            raise Exception1
            
        elif L=='row':
            if loc<r:
               l=f[loc,:] 
               return l
            raise Exception1
            
        else:
            raise Exception2

   except Exception1:
        print('the value of loc must be less than the dimension of the Image')
   except Exception2:
       print('the value of L must be "colum" or "row"')
       


im=io.imread('cameraman.tif')
print(im[0,:])
'''
r,c = im.shape
l=scanLine4e(im,L='colu',loc=255)
fig=plt.figure(figsize=(15,15))

plt.plot(l)
plt.ylabel('the curve of the 12th column')

fig.savefig('1.jpg',dpi=800)
plt.show()'''


