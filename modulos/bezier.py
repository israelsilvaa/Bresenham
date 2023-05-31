from modulos.bresenham import Bresenham
from enums.icone import Icone
from modulos.tela import Tela

class Bezier:

    def __init__(self, inicioMatriz, fimMatriz):
        self.tela = Tela()
        self.inicioMatriz = inicioMatriz
        self.fimMatriz = fimMatriz
        self.planoCartesiano = Bresenham(self.inicioMatriz, self.fimMatriz)

        self.listaPontosCurva = []

    def fazerCurva(self, pontosIncialFinalControle):
        t = 0.001
        listaPontosCurva = []
        
        while t <= 1 :
            ponto = self.pontoBezier(pontosIncialFinalControle, t)
            if not(ponto in listaPontosCurva) :
                listaPontosCurva.append( ponto )
            t = t + 0.02

        self.marcarPontosCurva(listaPontosCurva)
        self.planoCartesiano.marcaPonto(pontosIncialFinalControle[0][0], pontosIncialFinalControle[0][1])
        self.listaPontosCurva = listaPontosCurva
        return self.planoCartesiano
    
    def pontoBezier(self, pontosIncialControleFinal, t: float):
        p0_x = (1 - t) ** 2 * pontosIncialControleFinal[0][0]
        p0_y = (1 - t) ** 2 * pontosIncialControleFinal[0][1]
        
        p1_x = 2 * (1 - t) * t * pontosIncialControleFinal[1][0]
        p1_y = 2 * (1 - t) * t * pontosIncialControleFinal[1][1]

        p2_x = t ** 2 * pontosIncialControleFinal[2][0]
        p2_y = t ** 2 * pontosIncialControleFinal[2][1]

        pontoCurva = [ round(p0_x + p1_x + p2_x), round(p0_y + p1_y + p2_y) ]
        return pontoCurva

    def pegarPontosIncialFinalControle(self):
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
        self.tela.limparTela()
        self.planoCartesiano.matrizAtual()

        cx = int(input("ponto de controle(x):"))
        cy = int(input("ponto de controle(y):"))
        self.planoCartesiano.marcaPonto(cx, cy, 2)

        self.tela.limparTela()
        self.planoCartesiano.matrizAtual()
        s = input("aperte enter para continuar")

        return [[x, y], [cx, cy,], [x_f, y_f]]

    def marcarPontosCurva(self, listaPontosCurva:list):
        for i in range(len(listaPontosCurva)):
            self.planoCartesiano.marcaPonto(listaPontosCurva[i][0], listaPontosCurva[i][1], 3)

    def printPontosCurva(self, listaPontosCurva:list):
        print("Pontos calculados da curva:")

        for i in range(len(listaPontosCurva)):
            print(listaPontosCurva[i], end="")
