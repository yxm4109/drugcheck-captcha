#!/bin/python
# -*- coding: UTF-8 -*-
import numpy as np

import Image

RGB2GRAY_R = 0.299
RGB2GRAY_G = 0.587
RGB2GRAY_B = 0.114

RATE=1.3

def imageClean(img):
    imrgb = np.array(img.convert('RGB'))
    imgray=threshhold(rgb2gray(imrgb) )
    r=threshhold(imrgb[:,:,0])
    g=threshhold(imrgb[:,:,1])
    b=threshhold(imrgb[:,:,2])
    return array2im(r),array2im(g),array2im(b),array2im(imgray)
    
def rgb2gray(imrgb):
    return imrgb[:,:,0]*RGB2GRAY_R+imrgb[:,:,1]*RGB2GRAY_G+imrgb[:,:,2]*RGB2GRAY_B

def threshhold(bwIm):
    svals=np.sum(bwIm[:])
    svals=svals/bwIm.size/RATE
    return (bwIm > svals)*1

def array2im(bwIm):
    ele={1:(255, 255, 255),0:(0 ,0, 0)}
    w,h =bwIm.shape
    vals = bwIm.reshape(1,w*h)[0]
    data = [ele[item] for item in vals]    
    img = Image.new('RGB',(h,w),'white')
    img.putdata(data)    
    return img
    
# def save2dIm(im,impath):
#     w,h = im.shape
#     im3d =np.zeros([w,h,3],'float')
#     im3d[:,:,0]=im
#     im3d[:,:,1]=im
#     im3d[:,:,2]=im
#     
#     
#     img = Image.fromarray(im3d)
#     img.show()
    
    
# def test():
#    
#     srcpath ='images/'
#     dstpath ='results/'
#     imagefiles = os.listdir(srcpath)
#     
#     for f in imagefiles:
#         imPath = srcpath+f
#         im=Image.open(imPath)
# 
#         r,g,b,gray=imageClean(im)
#         
#         r.save(dstpath+'r'+f,'jpeg')
# 
#         
#     
# test()

    
    
    

