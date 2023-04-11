from modulos.bresenham import Bresenham
from modulos.tela import Tela

tela = Tela()
tela.limparTela()

v = 4
x = -4 ; y = -2; xf = 1; yf = 5

teste = Bresenham(x, y, xf, yf, v)
teste.criarMatriz()
teste.matrizAtual()


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