from os import path
import sys

# arquivo = open("teste.uai", "r")

tipo_token = {
    'uai': (1, 'main'),
    'queijo': (2, 'inteiro'),
    'pamonha': (3, 'texto'),
	'num': (4, 'numero'),
	'id': (5, 'id'),
    'casadinho': (6, 'bool'),
	'otos-caso': (7, 'senao'),
	'otos-caso-se': (8, 'senaose'),
	'ate-que': (9, 'while'),
	'bota': (10, 'cout'),
	'caso': (11, 'caso'), # representa o IF
	'faiz': (12, 'faiz'), #repreta o for
	'cata': (13, 'cin'),
	'xuxa': (14, 'return'),
	'trem-bao': (15, 'verdadeiro'),
	'trem-ruim': (16, 'falso'),
	'e': (17, 'e'),
    'ou': (18, 'ou'),
    'aneim': (19, 'nao'),
    'menor-que': (20, 'menor-que'),
    'maior-que': (21, 'maior-que'),
    'menor-que-ou-mema-coisa': (22, 'menor-que-ou-mema-coisa'),
    'maior-que-ou-mema-coisa': (23, 'maior-que-ou-mema-coisa'),
    'mema-coisa': (24, 'mema-coisa'),
    'diferente-de': (25, 'diferente-de'),
	'mais': (26, 'soma'),
	'menos': (27, 'sub'),
	'veiz': (28, 'vezes'),
	'por': (29, 'divisao'),
    '(': (30, '('),
    ')': (31, ')'),
	'~': (32, 'endlinha'),
	'<>': (33, 'atrib'),
	'|': (34, 'pipe'),  
	'literal': (35, 'literal'),
	'end': (36, 'end'),
	'erro': (37, 'erro'),
	' ': (38, 'espaco'), 
}

def getChar(buffer, arquivo, linha):
	if len(buffer) > 0:
		c = buffer[0]
		buffer = buffer[1:]
		print('MANO')
		if c == '\n':
			linha[0] += 1
		return c
	else:
		c = arquivo.read(1)
		# se nao foi eof, pelo menos um car foi lido
		# senao len(c) == 0
		if len(c) == 0:
			return None
		else:
			if c == '\n':
				linha[0] += 1
			return c

def getToken(arquivo, linha):
		prev = None
		lexema = ''
		buffer = ''
		estado = 1
		car = None
		while (True):
			# O estado 1 verifica quais sao os estados iniciais
			if estado == 1:
				car = getChar(buffer, arquivo, linha)
				# Fim do arquivo
				if car not in {' ', '\n', '\t'}:
					if car is None:
						return [tipo_token['end'], '<eof>', linha]
					# Verifica se sao letras
					elif car.isalpha():
						estado = 2
					# Verifica se sao numeros
					elif car.isdigit():
						estado = 3
					# Verifica se sao tokens primitivos
					elif car in { '~','(', ')', '|'}:
						estado = 4
					# Verifica o comentario
					elif car == '!':
						estado = 5
					# Cadeia
					elif car == '-':
						estado = 6
					elif car == '<':
						estado = 7
					else: return [tipo_token['erro'], '<' + car + '>', linha]
				
			elif estado == 2:
				# Estado que trata nomes (identificadores ou palavras reservadas)
				lexema = lexema + car
				car = getChar(buffer, arquivo, linha)
				if car in {':', '$'}:
					return [tipo_token[lexema], lexema, linha]
				elif car == ' ':
					return [tipo_token['id'], lexema, linha]
				elif car is None:  
					return [tipo_token['erro'], '<' + car + '>', linha]

			elif estado == 3:
				# Estado que trata numeros inteiros
				lexema = lexema + car
				car = getChar(buffer, arquivo, linha)
				if car == ' ':
					return [tipo_token['num'], lexema, linha]
				elif car is (not car.isdigit()):
					return [tipo_token['erro'], '<' + car + '>', linha]

			elif estado == 4:
				# estado que trata outros tokens primitivos comuns
				lexema = lexema + car
				if car == '~':
					return [tipo_token['~'], lexema, linha]
				elif car == '(':
					return [tipo_token['('], lexema, linha]
				elif car == ')':
					return [tipo_token[')'], lexema, linha]
				elif car == '|':
					return [tipo_token['|'], lexema, linha]

			# O estado 5 trata sobre a '/', para saber se e um comentario
			# de linha ou bloco
			elif estado == 5:
				car = getChar(buffer, arquivo, linha)
				if car == '!':
					estado = 1	

			# O estado 6 trata da cadeia entre aspas duplas
			elif estado == 6:
				car = getChar(buffer, arquivo, linha)

				while (not car is None) and (car != '-'):
					lexema = lexema + car
					car = getChar(buffer, arquivo, linha)
				estado = 1
				return [tipo_token['literal'], lexema, linha]
			
			elif estado == 7:
				lexema = lexema + car
				car = getChar(buffer, arquivo, linha)
				if car == '>':
					estado = 8

			elif estado == 8:
				lexema = lexema + car
				car = getChar(buffer, arquivo, linha)
				if car == ' ':
					return [tipo_token['<>'], lexema, linha]

def main():		
	with open("teste.uai", "r") as file:
		linha = [1]
		while(True):
			token = getToken(file, linha)
			if token[0] == tipo_token['end']:
				break
			else: 
				for i in token:
					print(i," ", end='')
				print("")

main()