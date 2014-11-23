#! /usr/bin/python

import socket
import sys

#port = 70  #Gopher uses port 70
#host = sys.argv[1]
#filename = sys.argv[2]

#s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#s.connect((host, port))

#s.sendall(filename + '\r\n')
#
#while 1:
#	buf = s.recv(2048)
#	if not len(buf):
#		break
#	sys.stdout.write(buf)
#


print 'welcome.'
print 'Please ener a string:'
sys.stdout.flush()
line = sys.stdin.readline().strip()
print 'You entered %d characters.'% len(line)

