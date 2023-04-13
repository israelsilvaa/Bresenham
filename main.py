from modulos.bresenham import Bresenham
from modulos.tela import Tela

tela = Tela()

x = -2; y = 3; xf = 3; yf = 9

teste = Bresenham(x, y, xf, yf)
teste.criarMatriz()
tela.limparTela()
teste.matrizAtual()
# teste.matrizCoordenada()
# teste.reta()
# teste.matrizAtual()



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