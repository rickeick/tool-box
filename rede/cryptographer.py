from sys import argv
from random import seed, randint

indices = [c for c in 'abcdefghijklmnopqrstuvwxyz']
letras = {c:i for i,c in enumerate('abcdefghijklmnopqrstuvwxyz')}

indice = int()
string = str()

if argv[1] == '--table':
	for key,value in letras.items():
		print(f'{key}:{value}', end=' ')
	print()

elif argv[1] == '--encode':
	seed(argv[2])
	for palavra in argv[3].split():
		for letra in palavra:
			indice = letras[letra] + randint(1,9)
			if indice > 25: indice -= 26
			string += indices[indice]
		string += ' '
	print(string)

elif argv[1] == '--decode':
	seed(argv[2])
	for palavra in argv[3].split():
		for letra in palavra:
			indice = letras[letra] - randint(1,9)
			string += indices[indice]
		string += ' '
	print(string)
