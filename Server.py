# -*- coding: utf-8 -*-
"""
Created on Wed Nov  3 22:42:17 2021

@author: iceki
"""
import socket

skt=socket.socket(socket.AF_INET,socket.SOCK_STREAM)   #定义socket类型，网络通信，TCP

host='127.0.0.1'
port=8080


#绑定套接字到本地IP与端口
skt.bind((host,port))

skt.listen(1) 
print ('监听客户端中......')   
#开始TCP监听,监听1个request，等待连接
#while 1:
    #接受TCP连接，并返回新的套接字与IP地址
con,addr=skt.accept()#建立连接
print ('已连接到客户端。IP '+host+':',port)
msg="这是一条来自服务器的消息，请你输入要发送的信息："
con.send(msg.encode('utf-8'))  
msg=con.recv(1024)#接收大小1KB
print('[来自客户端的消息：\t'+msg.decode())
con.close()
