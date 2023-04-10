from modulos.bresenham import Bresenham

v = 4
x = -1 ; y = -1; xf = 1; yf = 1

# na declaração do objeto são iniciadas as variaveis
# e calculado o M por exemplo
teste = Bresenham(x, y, xf, yf, v)
teste.matrizAtual()


#essa função do objeto calculas os pontos e despois
# marca esses pontos na matriz
teste.reta()

# função para printar a matriz atual do objeto
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