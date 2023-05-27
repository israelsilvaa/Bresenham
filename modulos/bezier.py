from modulos.bresenham import Bresenham
from enums.icone import Icone
from modulos.tela import Tela

class Bezier:

    def __init__(self, inicioMatriz, fimMatriz):
        self.tela = Tela()
        self.inicioMatriz = inicioMatriz
        self.fimMatriz = fimMatriz
        self.planoCartesiano = Bresenham(self.inicioMatriz, self.fimMatriz)

        self.pontosDeControle = []


    def fazerCurva(self, pontosIncialFinal, pontosDeControle):
        t = 0.1
        while t <= 1:
            ponto = self.pontoBezier(pontosDeControle, t)
            self.planoCartesiano.marcaPonto(round(ponto[0]), round(ponto[1]), 2)
            t += t
        return self.planoCartesiano

    def pontoBezier(self, pontosDeControle, t):
        r = 1
        n = len(pontosDeControle)
        pontos = []
        pontos = pontosDeControle.copy()
    
        for k in range(r, n+1):
            for i in range(0, n-k):
                pontos[i] = [round((1-t)*pontos[i][0] + t*pontos[i][0]), round((1-t)*pontos[i+1][1]+t*pontos[i+1][1] )] 


        print("debug pontos:", pontos)
        # s = input("DEBUG: DEF PONTOBEZIER")
        return pontos[0]

    def pegarPontosDecontrole(self):
        pontosDeControle = []
        while True:
            self.tela.limparTela()
            self.planoCartesiano.matrizAtual()
            print("Lista de pontos de controle:", pontosDeControle)
            print("!! enter vazio para cancelar !!")
            x = input("Novo ponto de controle(x):")
            y = input("Novo ponto de controle(y):")
            if x == "" or y =="":
                break
            else:
                pontosDeControle.append([int(x), int(y)])
                self.planoCartesiano.marcaPonto(int(x), int(y), 3)
        return pontosDeControle

    def pegarPontosIncialFinal(self):
        self.tela.limparTela()
        print("Bézier - Inserir pontos inicial e final da curva")
        self.planoCartesiano.matrizAtual()
    
        x = int(input("Ponto Inicial(x):"))
        y = int(input("Ponto Inicial(y):"))
        self.planoCartesiano.marcaPonto(x, y)

        self.tela.limparTela()
        self.planoCartesiano.matrizAtual()
        x_f = int(input("Ponto Final(x):"))
        y_f = int(input("Ponto Final(y):"))
        self.planoCartesiano.marcaPonto(x_f, y_f)

        return [x, y, x_f, y_f]


        




