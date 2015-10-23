#!/bin/env python 
#-*- coding: UTF-8 -*-
'''
Created on 2015-5-4

@author: yw
'''

import Image
import getCaptcha

filePath='D:/workspace/android_workspace/AuthCodeProvider/src/testdata/2.jpg'

def TestOCRByFilePath():
    res=getCaptcha.OCRByFilePath(filePath)
    print 'TestOCRByFilePath='+res

def TestOCRByImage():
    image=Image.open(filePath)
    res=getCaptcha.OCRByImage(image)
    print 'TestOCRByFilePath='+res
    
def TestOCRByStream():
    imageStream=open(filePath,'rb').read()#文件流可以来自任意地方，请使用jpg图片
    res=getCaptcha.OCRByStream(imageStream)
    print 'TestOCRByStream='+res
    

# TestOCRByFilePath()
TestOCRByImage()
# TestOCRByStream()