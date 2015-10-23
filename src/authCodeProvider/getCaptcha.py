#!/bin/python
# -*- coding: UTF-8 -*-

import tesseract
import io
import cStringIO
from StringIO import StringIO
import urllib2

import Image
from myImage import imageClean
from tessApi import tessApi

api=tessApi().get()

def tessRun(img):
    output = StringIO()
    img.save(output, format='JPEG')
    mBuffer=output.getvalue()
    return tesseract.ProcessPagesBuffer(mBuffer,len(mBuffer),api)
#     return result.strip().replace("\t","").replace("\r\n","").replace("	","").replace(" ","")
'''
图片文件数据流，比如（resHeader,response=httpClient.request('a url',"POST",params,headers=reqHeader))
'''
def OCRByStream(imgStream):
    imageFile = cStringIO.StringIO(imgStream)
    img = Image.open(imageFile)
    return OCRByImage(img)

'''
根据文件路径识别验证码，请使用jpg图片
'''
def OCRByFilePath(mImgFile):
    mBuffer=open(mImgFile,'rb').read()
    return tesseract.ProcessPagesBuffer(mBuffer,len(mBuffer),api)

'''
根据image对象（比如PIL中 Image.open()打开的对象）
'''
def OCRByImage(img):
    output = StringIO()
    img.save(output, format='JPEG')
    mBuffer=output.getvalue()
    return tesseract.ProcessPagesBuffer(mBuffer,len(mBuffer),api)

def calResult(imgFile):
    try:
        [r,g,b,gray]=imageClean(imgFile)
    except Exception,ex:
        print str(Exception)+":"+str(ex) 
        return None
    
    strR = tessRun(r).strip().replace("\t","").replace("\r\n","").replace(" ","")
    strG = tessRun(g).strip().replace("\t","").replace("\r\n","").replace(" ","")
    strB = tessRun(b).strip().replace("\t","").replace("\r\n","").replace(" ","")
    strGRAY = tessRun(gray).strip().replace("\t","").replace("\r\n","").replace(" ","")
    
    strMatrix=[]
    
    if len(strR)>3:
        strMatrix.append(strR)
    if len(strG)>3:
        strMatrix.append(strG)
    if len(strB)>3:
        strMatrix.append(strB)
    if len(strGRAY)>3:
        strMatrix.append(strGRAY)
   
    c=[]
    
    for s in strMatrix:
        c.append(s[0])
    firstNum=calMostBelChar(c)
    
    c=[]
    for s in strMatrix:
        c.append(s[1])
    oper=calMostBelChar(c)
    
    c=[]
    for s in strMatrix:
        c.append(s[2])
    secondNum=calMostBelChar(c)
   
    if oper=='-':
        return str(int(firstNum)-int(secondNum))
    elif oper=='X':
        return str(int(firstNum)*int(secondNum))    
    elif oper=='+':
        return str(int(firstNum)+int(secondNum))
    else:
        return '0'
    
def calMostBelChar(s):
    a=0
    j=0    
    for i in range(len(s)):
        if a<s.count(i):
            a=s.count(i)
            j=i
    return s[j]

def test():
    img=Image.open('a.jpg')
    output = io.BytesIO()
    img.save(output, format='JPEG')
    mBuffer=output.getvalue()

    print tesseract.ProcessPagesBuffer(mBuffer,len(mBuffer),api)
    
