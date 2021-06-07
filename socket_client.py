
#!/usr/bin/env python

# Create a TCP client that prompts user for a message, sends them to the server,
# receives them back from the server with a timestamp prefix, and displays the
# result to the user.

from socket import *

def socket_Client():
#   HOST   = 'localhost'    # or '127.0.0.1'
#   HOST   = '192.168.1.3'
    HOST   = '192.168.1. 3'  # Dell Inspiron N1710
    PORT   = 21567
    BUFSIZ = 1024
    ADDR   = (HOST, PORT)

    tcpCliSock = socket(AF_INET, SOCK_STREAM)
    tcpCliSock.connect(ADDR)

    while True:
        data_ascii = input('> ')
        if not data_ascii:
            break
        data_binary = data_ascii.encode('utf-8')
        tcpCliSock.send(data_binary)
        data_binary = tcpCliSock.recv(BUFSIZ)
        if not data_binary:
            break
        print(data_binary.decode('ascii'))
    tcpCliSock.close()
    print('Exiting socket client')

socket_Client();
