# -*- coding: utf-8 -*-
"""
Created on Wed Nov  3 22:50:48 2021

@author: iceki
"""
import socket

skt=socket.socket(socket.AF_INET,socket.SOCK_STREAM)   #定义socket类型，网络通信，TCP

host='127.0.0.1'
port=8080


#绑定套接字到本地IP与端口
print('尝试连接中......')
skt.connect((host,port))
print('已连接到服务器，IP '+host+':',port)
msg=skt.recv(1024)
print(msg.decode())
msg=input();
skt.send(msg.encode('utf-8'))
skt.close();