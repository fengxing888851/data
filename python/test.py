import socket as sk

host= ''
port = 12345

s =sk.socket(sk.AF_INET,sk.SOCK_STREAM)
s.setsockopt(sk.SOL_SOCKET,sk.SO_REUSEADDR,1)
s.bind((host,port))
s.listen(1)

print "Server running on port %d" %port

while True:
    clientsock, clientaddr = s.accept()
    clientfile = clientsock.makefile('rw',0)
    clientfile.write("Welcome," + str(clientaddr) + "\n")
    clientfile.write("Please enter a string:")
    line = clientfile.readline().strip()
    clientfile.write("You entered %d characters. \n" %len(line))
    clientfile.close()
    clientsock.close()
