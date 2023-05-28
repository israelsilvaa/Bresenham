from modulos.bresenham import Bresenham
from modulos.tela import Tela
class Circulo:

    def __init__(self, inicioMatriz, fimMatriz):
        self.tela = Tela()
        self.inicioMatriz = inicioMatriz
        self.fimMatriz = fimMatriz
        self.planoCartesiano = Bresenham(inicioMatriz, fimMatriz)

        self.xcirculo = None
        self.ycirculo = None
        self.raio = None
        self.listaQ1 = []
        self.listaQ2 = []
        self.listaQ3 = []
        self.listaQ4 = []
        self.listaQ5 = []
        self.listaQ6 = []
        self.listaQ7 = []
        self.listaQ8 = []

    def calcPontosCirculo(self):
        print("X:", self.xcirculo,"Y:", self.ycirculo," -- Raio:", self.raio,)
        x  = 0 
        y = self.raio
        erro = self.raio*(-1)   # -raio

        while x <= y:
            erro = erro + 2*x + 1
            x = x + 1
            if erro >= 0:
                erro = erro + 2 - 2*y
                y = y - 1
            self.desenha8(x, y, self.xcirculo, self.ycirculo)
        
        return self.planoCartesiano
    
    def desenha8(self, x, y, xc, yc):
        self.planoCartesiano.marcaPonto(x + xc, y + yc)
        self.planoCartesiano.marcaPonto(y + xc, x + yc)
        self.planoCartesiano.marcaPonto(y + xc, -x + yc)
        self.planoCartesiano.marcaPonto(x + xc, -y + yc)
        self.planoCartesiano.marcaPonto(-x + xc, -y + yc)
        self.planoCartesiano.marcaPonto(-y + xc, -x + yc)
        self.planoCartesiano.marcaPonto(-y + xc, x + yc)
        self.planoCartesiano.marcaPonto(-x + xc, y + yc)

        self.planoCartesiano.marcaPonto(self.xcirculo, self.raio + self.ycirculo)
        self.planoCartesiano.marcaPonto(self.raio + self.xcirculo, self.ycirculo)
        self.planoCartesiano.marcaPonto(self.xcirculo , self.raio*(-1) + self.ycirculo )
        self.planoCartesiano.marcaPonto(self.raio*(-1) + self.xcirculo, self.ycirculo)

        self.planoCartesiano.marcaPonto(self.xcirculo, self.ycirculo, 2)

    def execute(self):
        # xCirculo, yCirculo, raio, matriz:Bresenham
        while True:
            self.tela.limparTela()
            print("Circulo\n")
            self.planoCartesiano.matrizAtual()
            
            xc = input("\nXc inicial:")
            yc = input("\nYc inicial:")
            r = input("\nRaio(R>1):")

            if xc == "" or yc == "" or r == "":
                break

            self.xcirculo = int(xc)
            self.ycirculo = int(yc)
            self.raio = int(r)

            self.planoCartesiano = self.calcPontosCirculo()