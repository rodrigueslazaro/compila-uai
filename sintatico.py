comentario = True

def main(self):
    if comentario: print('Atual: main')
    consome( tt.main )
    consome( tt.pipe )
    declaracoes()
    comandos()
    consome( tt.pipe )

def declaracoes():
	if comentario: print('Atual: declaracoes')
	if atualIgual( tt.inteiro, tt.texto ):
		consomeAtual()
		consome( tt.id )
		consome( tt.espaco )
		consome( tt.endlinha )
		declaracoes()
	else:
		pass

def comandos ():
	if comentario: print('Atual: comandos')
	if atualIgual( tt.atrib, tt.caso, tt.faiz, tt.cout , tt.cin  ):
		consomeAtual()
		comandos()
	else:
		pass


def LISTDECLS(self):
if comentario: print('Atual: LISTDECLS')
self.DECLSTIPO()
self.D()

def D(self):
if self.atualIgual( tt.ID ):
	self.LISTDECLS()
else:
	pass

def DECLSTIPO(self):
if comentario: print('Atual: DECLSTIPO')
self.LISTID()
self.consome( tt.DPONTOS )
self.TIPO()
self.consome( tt.PVIRG )

def LISTID(self):
if comentario: print('Atual: LISTID')
self.consome( tt.ID )
self.E()

def E(self):
if comentario: print('Atual: E')
if self.atualIgual( tt.VIRG ):
	self.consome( tt.VIRG )
	self.LISTID()
else:
	pass

def TIPO(self):
if comentario: print('Atual: TIPO')
if self.atualIgual( tt.CARACTER ):
	self.consome( tt.CARACTER )
elif self.atualIgual( tt.INTEIRO ):
	self.consome( tt.INTEIRO )
elif self.atualIgual( tt.LOGICO ):
	self.consome( tt.LOGICO )
else:
	self.consome( tt.REAL )

def CCOMP(self):
if comentario: print('Atual: CCOMP')
self.consome( tt.ABRECH )
self.LISTACOMANDOS()
self.consome( tt.FECHACH )

def LISTACOMANDOS(self):
if comentario: print('Atual: LISTACOMANDOS')
self.COMANDOS()
self.G()

def G(self):
if comentario: print('Atual: G')
if self.atualIgual( tt.ENQUANTO ) or self.atualIgual( tt.ESCREVA ) or self.atualIgual( tt.ID ) or self.atualIgual( tt.LEIA ) or self.atualIgual( tt.SE ):
	self.LISTACOMANDOS()
else:
	pass

def COMANDOS(self):
if comentario: print('Atual: COMANDOS')
if self.atualIgual( tt.ENQUANTO ):
	self.WHILE()
elif self.atualIgual( tt.ESCREVA ):
	self.WRITE()
elif self.atualIgual( tt.ID ):
	self.ATRIB()
elif self.atualIgual( tt.LEIA ):
	self.READ()
elif self.atualIgual( tt.SE ):
	self.IF()

def IF(self):
if comentario: print('Atual: SE')
self.consome( tt.SE )
self.consome( tt.ABREPAR )
self.EXPR()
self.consome( tt.FECHAPAR )
self.CCOMP()
self.H()

def H(self):
if comentario: print('Atual: SENAO')
if self.atualIgual( tt.SENAO ):
	self.consome( tt.SENAO )
	self.CCOMP()
else:
	pass

def WHILE(self):
if comentario: print('Atual: ENQUANTO')
self.consome( tt.ENQUANTO )
self.consome( tt.ABREPAR )
self.EXPR()
self.consome( tt.FECHAPAR )
self.CCOMP()

def READ(self):
if comentario: print('Atual: LEIA')
self.consome( tt.LEIA )
self.consome( tt.ABREPAR )
self.LISTID()
self.consome( tt.FECHAPAR )
self.consome( tt.PVIRG )

def ATRIB(self):
if comentario: print('Atual: ATRIB')
self.consome( tt.ID )
self.consome( tt.ATRIB )
self.EXPR()
self.consome( tt.PVIRG )

def WRITE(self):
if comentario: print('Atual: ESCREVA')
self.consome( tt.ESCREVA )
self.consome( tt.ABREPAR )
self.LISTW()
self.consome( tt.FECHAPAR )
self.consome( tt.PVIRG )

def LISTW(self):
if comentario: print('Atual: LISTW')
self.ELEMW()
self.L()

def L(self):
if comentario: print('Atual: L')
if self.atualIgual( tt.VIRG ):
	self.consome( tt.VIRG )
	self.LISTW()
else:
	pass

def ELEMW(self):
if comentario: print('Atual: ELEMW')
if self.atualIgual( tt.EXPR ):
	self.EXPR()
else:
	self.consome( tt.CADEIA )

def EXPR(self):
if comentario: print('Atual: EXPR')
self.SIMPLES()
self.P()

def P(self):
if comentario: print('Atual: P')
if self.atualIgual( tt.OPREL ):
	self.consome( tt.OPREL )
	self.SIMPLES()
else:
	pass

def SIMPLES(self):
if comentario: print('Atual: SIMPLES')
self.TERMO()
self.R()

def R(self):
if comentario: print('Atual: R')
if self.atualIgual( tt.OPAD ):
	self.consome( tt.OPAD )
	self.SIMPLES()
else:
	pass

def TERMO(self):
if comentario: print('Atual: TERMO')
self.FAT()
self.S()

def S(self):
if comentario: print('Atual: S')
if self.atualIgual( tt.OPMUL ):
	self.consome( tt.OPMUL )
	self.TERMO()
else:
	pass

def FAT(self):
if comentario: print('Atual: FAT')
if self.atualIgual( tt.ABREPAR ):
	self.consome( tt.ABREPAR )
	self.EXPR()
	self.consome( tt.FECHAPAR )
elif self.atualIgual( tt.CTE ):
	self.consome( tt.CTE )
elif self.atualIgual( tt.FALSO ):
	self.consome( tt.FALSO )
elif self.atualIgual( tt.ID ):
	self.consome( tt.ID )
elif self.atualIgual( tt.OPNEG ):
	self.consome( tt.OPNEG )
	self.FAT()
elif self.atualIgual( tt.VERDADEIRO ):
	self.consome( tt.VERDADEIRO )
		
if __name__== "__main__":
	if (len(sys.argv) != 2) and (len(sys.argv) != 4): 
		print('USAGE: python3 sintatico.py <nome-arquivo.txt> // Execução normal.')
		print('USAGE: python3 sintatico.py -t <nome-arquivo-teste.txt> <nome-arquivo-tabela.txt>'
			+ '// Gera arquivo da tabela de símbolos.')
		sys.exit()
	
	
	if len(sys.argv) == 2:
		nome = sys.argv[1]

	if len(sys.argv) == 4:
		tabela = sys.argv[1]
		nome = sys.argv[2]
		arquivo = sys.argv[3]

		arquivo_tabela = open(arquivo, 'w')

	parser = Sintatico()
	parser.interprete(nome)

	if arquivo_tabela: arquivo_tabela.close()
