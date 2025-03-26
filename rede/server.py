from sys import argv
from socket import socket
from socket import AF_INET
from socket import SOCK_STREAM

server = socket(AF_INET, SOCK_STREAM)
server.bind((argv[2], int(argv[3])))
server.listen(5)
print(f'[*] Listening...')
while True:
	client, info = server.accept()
	print(f'[*] Accepted connection from {info[0]}:{info[1]}')
	while True:
		request = client.recv(1024)
		if request == b'': break
		print(f'[CLINTE] {request}')
		msg = bytes(input(f'[SERVER] '), 'utf-8')
	client.send(msg)
	client.close()
