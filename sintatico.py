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
endDeclaracoes = False

arquivo = open("teste.uai", "r")

def atualIgual(token):
    return tokenAtual[0][1] == token[1]

def consome(token):
    global tokenAtual
    if ( token[1] == tokenAtual[0][1] ):
        tokenAtual = getToken(arquivo, linha)
    else:
        print('ERRO DE SINTAXE')

def declaracoes():
    if comentario: print('Atual: declaracoes')
    while(var_type()):
        id()
        endline()

def var_type():
    if (atualIgual(tt['queijo'])):
        consome(tt['queijo'])
        return True
    elif (atualIgual(tt['pamonha'])):
        consome(tt['pamonha'])
        return True
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
    elif atualIgual(tt['caso']):
        caso()
    elif atualIgual(tt['faiz']):
        faiz()
    elif atualIgual(tt['cata']):
        cin()
    elif atualIgual(tt['bota']):
        cout()

def atribuicao():
    consome(tt['id'])
    if atualIgual(tt['<>']):
        consome(tt['<>'])
        conteudo()
        endline()
    else:
        print("Esperava-se um <>")

def endline():
    if atualIgual(tt['~']):
        consome(tt['~'])
    else:
        print("Esperava-se um ~")

def conteudo():
    terminal()
    Elinha()

def terminal():
    if (atualIgual(tt['num'])):
        consome(tt['num'])
    elif (atualIgual(tt['id'])): 
        id()
    else:
        print("Esperava-se um valor")
        return False
    return True

def Elinha():
    if (operador()):
        terminal()
        Elinha()
    else:
        pass

def operador():
    if atualIgual(tt['mais']):
        consome(tt['mais'])
    elif atualIgual(tt['menos']):
        consome(tt['menos'])
    elif atualIgual(tt['veiz']):
        consome(tt['veiz'])
    elif atualIgual(tt['por']):
        consome(tt['por'])
    else:
        return False
    return True

def caso(): #corresponde ao se
    consome(tt['caso'])
    expressao()
    comandos()
    pipe()
    otoscaso()

def otoscaso():
    if atualIgual(tt['otos-caso']):
        consome(tt['otos-caso'])
        pipe()
        comandos()
        pipe()	
    else: 
        if atualIgual(tt['otos-caso-se']):
            consome(tt['otos-caso-se'])
            expressao()
            pipe()
            comandos()
            pipe()
            otoscaso()
        else:
            pass

def pipe():
    if atualIgual(tt['|']):
        consome(tt['|'])
    else:
        print("Esperava-se um |")

def expressao():
    terminalLogico()
    Llinha()

def terminalLogico():
    if (atualIgual(tt['num'])):
        consome(tt['num'])
    elif (atualIgual(tt['id'])):
        id()
    elif (atualIgual(tt['trem-bao'])):
        consome(tt['trem-baum'])
    elif (atualIgual(tt['trem-ruim'])): #verifico se é um terminal logico
        consome(tt['trem-ruim'])
    else:
        print("Esperava-se um símbolo lógico")
        return False
    return True

def Mlinha():
    if (atualIgual(tt['|'])):
        consome(tt['|'])
    elif (operadorEOu()):
        terminal()
        Llinha()
        Mlinha()
    else:
        pass

def operadorEOu():
    if (atualIgual(tt['e'])):
        consome(tt['e'])
    elif (atualIgual(tt['ou'])):
        consome(tt['ou'])
    else:
        print("Esperave-se um E ou OU")
        return False
    return True   

def Llinha():
    if (operadorLogico()):
        terminal()
        if not atualIgual(tt['|']):
            Mlinha()
            Llinha()
    else:
        #print('Esperava-se E ou OU')
        pass

def operadorLogico():
    if (atualIgual(tt['mema-coisa'])):
        consome(tt['mema-coisa'])
    elif (atualIgual(tt['diferente-de'])):
        consome(tt['diferente-de'])
    elif (atualIgual(tt['maior-que'])):
        consome(tt['maior-que'])
    elif (atualIgual(tt['menor-que'])):
        consome(tt['menor-que'])
    elif (atualIgual(tt['maior-que-ou-mema-coisa'])):
        consome(tt['maior-que-ou-mema-coisa'])
    elif (atualIgual(tt['menor-que-ou-mema-coisa'])):
        consome(tt['menor-que-ou-mema-coisa'])
    elif (atualIgual(tt['aneim'])):
        consome(tt['aneim'])
    elif (atualIgual(tt['e'])):
        consome(tt['e'])
    elif (atualIgual(tt['ou'])):
        consome(tt['ou'])
    else:
        return False
    return True

def faiz():
    consome(tt['faiz'])
    if (atualIgual(tt['id'])):
        id()
    elif (atualIgual(tt['num'])):
        consome(tt['num'])
    consome(tt['rodada'])
    pipe()
    comandos()
    pipe()

def cin():
    if atualIgual(tt['cata']):
        consome(tt['cata'])
        id()
        endline()

def id():
    if atualIgual(tt['id']):
        consome(tt['id'])
    else:
        print("Esperava-se um identificador")

def cout():
    consome(tt['bota'])
    if (atualIgual(tt['literal'])):
        consome(tt['literal'])
    elif (atualIgual(tt['id'])):
        consome(tt['id'])
    consome(tt['~'])
        
def uai():
    if atualIgual(tt['uai']):
        consome(tt['uai'])
    else:
        print("Esperava-se um 'uai', uai!")

def main():
    global tokenAtual
    tokenAtual = getToken(arquivo, linha)
    if comentario: print('Atual: main')
    uai()
    pipe()
    declaracoes()
    comandos()
    pipe()

main()
