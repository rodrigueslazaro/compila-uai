from lexico import tipo_token as tt
from lexico import getToken
from os import path
import sys

tabelaSimbolos = {}
arquivo_tabela = None
comentario = True
tokenAtual = None
arquivo = None
buffer = ''
linha = [0]

arquivo = open("teste.uai", "r")
def abrir_lexico(nomeArquivo):
	if path.exists(nomeArquivo):
		arquivo = open(nomeArquivo, "r")
		buffer = ''
		linha = 1
	else:
		print('ERRO: Arquivo "%s" inexistente.' % nomeArquivo)


def atualIgual(token):
	return tokenAtual[1] == token[1]

def interprete(nomeArquivo):
	lex = abrir_lexico(nomeArquivo)
	tokenAtual = getToken()

	main()
	consome( tt['end'] )
	print('Atual: end')

def consome(token):
	global tokenAtual
	if ( token[1] == tokenAtual[0][1] ):
		tokenAtual = getToken(arquivo, linha)
	else:
		print('ERRO DE SINTAXE')

		# while self.tokenAtual.lexema != ';':
		# 	self.tokenAtual = self.lex.getToken() 
		
		#quit()

def declaracoes():
	if comentario: print('Atual: declaracoes')
	if (var_type()):
		consome(tt['id'])
		consome(tt['espaco'])
		consome(tt['endlinha'])
		declaracoes()
	else:
		pass

def var_type():
	if (atualIgual(tokenAtual[0][1])) or (atualIgual(tokenAtual[0][1])):
		consome()
		return True
	else:
		return False

def comandos():
	if comentario: print('Atual: comandos')
	if (atualIgual(tt['id']) or
	    atualIgual(tt['caso']) or
		atualIgual(tt['faiz']) or
		atualIgual(tt['cata']) or
		atualIgual(tt['bota'])):
		comando()
		comandos()
	else:
		pass

def comando():
	if atualIgual(tt['id']): #id e não atribuição pq estamos falando do processo inteiro de atrib, não apenas o símbolo
		atribuicao()
	if atualIgual(tt['caso']):
		caso()
	if atualIgual(tt['faiz']):
		faiz()
	if atualIgual(tt['cata']):
		cin()
	if atualIgual(tt['bota']):
		cout()

def atribuicao():
	consome(tt['id'])
	if atualIgual(tt['atrib']):
		consome(tt['atrib'])
		conteudo()
		endline()
	else:
		print("Esperava-se um <>")

def endline():
	if atualIgual(tt['endline']):
		consome(tt['endline'])
	else:
		print("Esperava-se um ~")

def conteudo():
	terminal()
	Elinha()

def terminal():
	if atualIgual(tt['numero'], tt['id']): #verifico se é um terminal
		consome()
	else:
		print("Esperava-se um valor")

def Elinha():
	if atualIgual(tt['soma'], tt['sub'], tt['vezes'], tt['divisao']):
		operador()
		terminal()
		Elinha()
	else:
		pass

def operador():
	#if atualIgual(tt.soma): #id e não atribuição pq estamos falando do processo inteiro de atrib, não apenas o símbolo
	#	consome(tt.soma)
	#if atualIgual(tt.sub):
	#	consome(tt.sub)
	#if atualIgual(tt.vezes):
	#	consome(tt.vezes)
	#if atualIgual(tt.divisao):
	#	consome(tt.divisao)
	consome()

def caso(): #corresponde ao se
	if atualIgual(tt['caso']):
		consome(tt['caso'])
		expressao()
		pipe()
		comandos()
		otoscaso()
		pipe()

def otoscaso():
	if atualIgual(tt['senao']):
		consome(tt['senao'])
		pipe()
		comandos()
		pipe()	
	else: 
		if atualIgual(tt['senaose']):
			consome(tt['senaose'])
			expressao()
			pipe()
			comandos()
			pipe()
			otoscaso()
		else:
			pass

def pipe():
	if atualIgual(tt['pipe']):
		consome(tt['pipe'])
	else:
		print("Esperava-se um |")


def expressao():
	terminalLogico()
	Llinha()

def terminalLogico():
	if atualIgual(tt['numero'], tt['id'], tt['verdadeiro'], tt['falso']): #verifico se é um terminal logico
		consome()
	else:
		print("Esperava-se um símbolo lógico")

def Llinha():
	if (operadorLogico()):
		terminal()
		Llinha()
	else:
		pass

def operadorLogico():
	if atualIgual(tt['mema-coisa'], tt['diferente-de'], tt['maior-que'], tt['menor-que'], 
			   tt['maior-que-ou-mema-coisa'], tt['menor-que-ou-mema-coisa'], tt['nao'], tt['e'], tt['ou']):
		consome()
		return True
	else:
		return False

def faiz():
	if atualIgual(tt['faiz']):
		consome(tt['faiz'])
		expressao()
		pipe()
		comandos()
		pipe()

def cin():
	if atualIgual(tt['cin']):
		consome(tt['cin'])
		id()
		endline()

def id():
	if atualIgual(tt['id']):
		consome(tt['id'])
	else:
		print("Esperava-se um identificador")

def cout():
	if atualIgual(tt['cout']):
		consome(tt['cout'])
		#???
		
def main():
    global tokenAtual
    tokenAtual = getToken(arquivo, linha)
    if comentario: print('Atual: main')
    consome(tt['uai']) #acho q tem q testar se tem o pipe para ser consumido
    consome(tt['|'])
    declaracoes()
    comandos()
    consome(tt['|'])

main()