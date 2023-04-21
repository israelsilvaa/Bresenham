from modulos.bresenham import Bresenham
from modulos.tela import Tela

tela = Tela()

x = 0; y = 5; xf = 5; yf = 5
teste = Bresenham(0,11)
tela.limparTela()
# teste.reta(x, y, xf, yf)
# teste.matrizAtual()
print("(", x, y,")    (", xf, yf,")")

#hexagono

# x = -4; y = -3; xf = -4; yf = 3 # |
# teste.reta(x, y, xf, yf)
# x = -4; y = 3; xf = 0; yf = 7 # /
# teste.reta(x, y, xf, yf)
# x = 0; y = 7; xf = 4; yf = 3 # \
# teste.reta(x, y, xf, yf)
# x = 4; y = -3; xf = 4; yf = 3 # |
# teste.reta(x, y, xf, yf)
# x = 4; y = -3; xf = 4; yf = 3# /
# teste.reta(x, y, xf, yf)
# x = -4; y = -3; xf = 0; yf = -7 #\
# teste.reta(x, y, xf, yf)
# x = 4; y = -3; xf = 0; yf = -7 # /


x = 3; y = 1; xf = 0; yf = 8 # /
teste.reta(x, y, xf, yf)
x = 0; y = 8; xf = 10; yf = 10 # /
teste.reta(x, y, xf, yf)
x = 10; y = 10; xf = 9; yf = 1 # /
teste.reta(x, y, xf, yf)
x = 9; y = 1; xf = 5; yf = 6 # /
teste.reta(x, y, xf, yf)
x = 5; y = 6; xf = 3; yf = 1 # /
teste.reta(x, y, xf, yf)

tela.limparTela()
teste.matrizAtual()

teste.tabelaVarredura()

# teste.matrizCoordenada()

"""
passo 1: 
    PIVÔ, levar pra horigem

passo2:
    (rotação de -30°)
    Xlinha: x.coss_Ang - y.sen_Ang
    Xlinha: x.sen_Ang + y.coss_Ang

passo3:
    x': sx.x
    x': 2.2,87 =5,74
    y: 1.2,98= 2,98

passo4:
    x': x +Tx = 5,74 - 1 = 4,74
"""