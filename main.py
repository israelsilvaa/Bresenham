from modulos.bresenham import Bresenham
from modulos.tela import Tela

tela = Tela()

x = 0; y = 5; xf = 5; yf = 5
teste = Bresenham(-4,9)
tela.limparTela()
# teste.reta(x, y, xf, yf)
# teste.matrizAtual()
print("(", x, y,")    (", xf, yf,")")



# x = 0; y = 0; xf = 6; yf = 8
# tela.limparTela()
# teste.reta(x, y, xf, yf)
# teste.matrizAtual()
# print("(", x, y,")    (", xf, yf,")")
# x = 0; y = 0; xf = -4; yf = -4
# # tela.limparTela()
# teste.reta(x, y, xf, yf)
# teste.matrizAtual()
# print("(", x, y,")    (", xf, yf,")")
# x = 0; y = 0; xf = 4; yf = -4
# # tela.limparTela()
# teste.reta(x, y, xf, yf)
# teste.matrizAtual()
# print("(", x, y,")    (", xf, yf,")")
# x = 0; y = 0; xf = -4; yf = 4
# # tela.limparTela()
# teste.reta(x, y, xf, yf)
# teste.matrizAtual()
# print("(", x, y,")    (", xf, yf,")")

x = -4; y = -4; xf = -3; yf = 7
tela.limparTela()
teste.reta(x, y, xf, yf)
teste.matrizAtual()
print("(", x, y,")    (", xf, yf,")")
x = -3; y = 7; xf = 9; yf = 7
# tela.limparTela()
teste.reta(x, y, xf, yf)
teste.matrizAtual()
print("(", x, y,")    (", xf, yf,")")
x = 9; y = 7; xf = 8; yf = -4
# tela.limparTela()
teste.reta(x, y, xf, yf)
teste.matrizAtual()
x = -4; y = -4; xf = 8; yf = -4
# tela.limparTela()
teste.reta(x, y, xf, yf)
teste.matrizAtual()



#teste.matrizCoordenada()

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