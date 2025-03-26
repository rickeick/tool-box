from os import system

ssids = list()
system('netsh wlan show profile > temp.txt')
with open('temp.txt') as file:
	for line in file:
		if 'Todos os Perfis:' in line:
			ssids.append(line.split(':')[1].strip())
for ssid in ssids:
	system(f'netsh wlan show profile "{ssid}" key = clear > temp.txt')
	with open('temp.txt') as file:
		for line in file:
			if 'Conte£do da Chave' in line:
				print(f'{ssid} : {line.split(":")[1].strip()}')
	system('del temp.txt')
input("Pressione Enter para encerar...")
