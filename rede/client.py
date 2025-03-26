from sys import argv
from socket import socket
from socket import AF_INET
from socket import SOCK_STREAM

client = socket(AF_INET, SOCK_STREAM)
client.connect((argv[2], int(argv[3])))
while True:
	msg = bytes(input(f'[CLIENT] '), 'utf-8')
	if msg == b'': break
	client.send(msg)
	response = client.recv(1024)
	print(f'[SERVER] {response}')
client.close()
