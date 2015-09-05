#!/usr/bin/python2

import  socket,os
s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
#AF:  address family
#INET:  for ipv4
SOCK_DGRAM : udp protocol
while True :
	  se=raw_input("send message to server : ")
	  s.sendto(se,("192.168.0.63",1111))
	  #here   s  is the object through which I call the function sendto()
#here I mention the IP address of the client to whome i want to send the message
# so you can manipulate this according to need
#1111 is the random port number 
	  rec=s.recvfrom(100)
#100 here means only show message upto 100 character which is send by the client
	  print  "    data received :  ",rec[0]
	  print  "server IP address is :  ",rec[1][0]
