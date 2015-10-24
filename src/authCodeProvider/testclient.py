#!/usr/bin/env python 
#-*- coding: UTF-8 -*-
import socket
import struct

filePath='D:/workspace/android_workspace/AuthCodeProvider/src/testdata/2.jpg'
# 
# fp = open(filePath, 'wb+')  
imageStream=open(filePath,'rb').read()
for i in range(1):
    b = b"4" 
    s=socket.socket()
    s.connect(("127.0.0.1",8889))

#     s.sendall(b)
    s.sendall(imageStream)
#     data=s.recv(1024)
#     print data
    s.close()