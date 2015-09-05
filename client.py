#!/usr/bin/python2

import  socket,os
s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
s.bind(("",1111))
#here "" indicates all the ip address in the present network it is open for all ip in network
while True :
	rec=s.recvfrom(100)
	print  "data received :  ",rec[0]
	print  "client  IP address is :  ",rec[1][0]
	x=raw_input("type ur mesg to client :  ")
	y=rec[1]
	s.sendto(x,y)
