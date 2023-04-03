from modulos.bresenham import Bresenham

v = 10
x = 2 ; y = 0; xf = 5; yf = 3

teste = Bresenham(x, y, xf, yf , v)

teste.reta()

#teste.reta(x, y, xf, yf )
teste.matrizAtual()   


"""
passo 1: 
    calcular o M 

    PIV�, levar pra horigem

passo2:
    (rota��o de -30�)
    Xlinha: x.coss_Ang - y.sen_Ang
    Xlinha: x.sen_Ang + y.coss_Ang

passo3:
    x': sx.x
    x': 2.2,87 =5,74
    y: 1.2,98= 2,98

passo4:
    x': x +Tx = 5,74 - 1 = 4,74
"""