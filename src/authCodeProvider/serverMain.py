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

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)

import SocketServer
from SocketServer import StreamRequestHandler
import logging
logging.basicConfig(level=logging.DEBUG,\
                    format='%(asctime)s %(levelname)s %(message)s',\
                    filename='log.txt',\
                    filemode='a+')


LOCAL_SERVER_ADDR='127.0.0.1'
LOCAL_SERVER_PORT='8889'


print BASE_DIR

print LOCAL_SERVER_ADDR,':',LOCAL_SERVER_PORT

class MyHandler(StreamRequestHandler):
    def handle(self):
        recv_cnt = 0
        rx_buf=self.request.recv(1024)
#         rx_buf=self.request.recv_bytes()
        len_buf = len(rx_buf)  
       
        if recv_cnt == 0:  
            data_len_total = struct.unpack('<I',rx_buf[0:8])  
#             buf = buffer(rx_buf, 8, len_buf - 8)             
        else:  
            buf = buffer(rx_buf)  
            
        recv_cnt = recv_cnt +1 

if __name__=='__main__': 
   
    my_server=SocketServer.ThreadingTCPServer((LOCAL_SERVER_ADDR,int(LOCAL_SERVER_PORT)),MyHandler)
    my_server.serve_forever()
   
