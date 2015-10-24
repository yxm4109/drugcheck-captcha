#!/usr/bin/env python 
#-*- coding: UTF-8 -*-

'''

  //=======\\//=======\\
  ||        ||         ||
  ||        ||         ||
  ||        ||         || //======   ||         /=====\     ||
  ||        ||         || ||         ||        ||     ||    ||
  ||        ||         || ||         ||        ||     ||    ||====\\
  ||        ||         || ||         ||        ||     ||    ||    ||
  ||        ||         || \\======   \\=====    \======\\   \\====//
  ------------------------------------------------------------------
                 仔细认真  沉着稳重  你会消除所有bug的。   

'''

'''
Created on 2015-5-7

@author: yw
'''

import socket
import threading
import sys
import time
import os
import struct
import Image
import getCaptcha

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)

import SocketServer
from SocketServer import StreamRequestHandler
import logging
logging.basicConfig(level=logging.DEBUG,\
                    format='%(asctime)s %(levelname)s %(message)s',\
                    filename='log.txt',\
                    filemode='a+')


LOCAL_SERVER_ADDR='192.168.31.160'
LOCAL_SERVER_PORT='8889'


print BASE_DIR

print LOCAL_SERVER_ADDR,':',LOCAL_SERVER_PORT

class MyHandler(StreamRequestHandler):
    def handle(self):
        recv_cnt = 0
        rx_buf=self.request.recv(4096)
#         rx_buf=self.request.recv_bytes()
        len_buf = len(rx_buf)  
        print len_buf
       
        res=getCaptcha.OCRByStream(rx_buf)
        self.request.send(res+"\n")

if __name__=='__main__': 
   
    my_server=SocketServer.ThreadingTCPServer((LOCAL_SERVER_ADDR,int(LOCAL_SERVER_PORT)),MyHandler)
    my_server.serve_forever()
   
