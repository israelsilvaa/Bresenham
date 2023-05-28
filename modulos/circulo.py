from modulos.bresenham import Bresenham

class Circulo:

    def __init__(self, xCirculo, yCirculo, raio, matriz:Bresenham):
        self.planoCartesiano = matriz
        self.xc = xCirculo
        self.yc = yCirculo
        self.raio = raio
        self.listaQ1 = []
        self.listaQ2 = []
        self.listaQ3 = []
        self.listaQ4 = []
        self.listaQ5 = []
        self.listaQ6 = []
        self.listaQ7 = []
        self.listaQ8 = []

    def calcPontosCirculo(self):
        print("X:", self.xc,"Y:", self.yc," -- Raio:", self.raio,)
        x  = 0 
        y = self.raio
        erro = self.raio*(-1)   # -raio

        while x <= y:
            erro = erro + 2*x + 1
            x = x + 1
            if erro >= 0:
                erro = erro + 2 - 2*y
                y = y - 1
            self.desenha8(x, y, self.xc, self.yc)
        
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

        self.planoCartesiano.marcaPonto(self.xc, self.raio + self.yc)
        self.planoCartesiano.marcaPonto(self.raio + self.xc, self.yc)
        self.planoCartesiano.marcaPonto(self.xc , self.raio*(-1) + self.yc )
        self.planoCartesiano.marcaPonto(self.raio*(-1) + self.xc, self.yc)


        self.planoCartesiano.marcaPonto(self.xc, self.yc, 2)
