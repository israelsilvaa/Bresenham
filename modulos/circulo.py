# from modulos.bresenham import Bresenham

class Circulo:

    def __init__(self, xCirculo, yCirculo, raio, matriz):
        self.objMtraiz = matriz
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
    
    def desenha8(self, x, y, xc, yc):
        self.listaQ1.append([x + xc, y + yc])
        self.listaQ2.append([y + xc, x + yc])
        self.listaQ3.append([y + xc, -x + yc])
        self.listaQ4.append([x + xc, -y + yc])
        self.listaQ5.append([-x + xc, -y + yc])
        self.listaQ6.append([-y + xc, -x + yc])
        self.listaQ7.append([-y + xc, x + yc])
        self.listaQ8.append([-x + xc, y + yc])

    def desenhaCirculo(self):
        for x in range(len(self.objMtraiz.matriz)):
                for y in range(len(self.objMtraiz.matriz)):

                    for i in range(len(self.listaQ1)):
                        if self.objMtraiz.matriz[x][y][1] == self.listaQ1[i][0] and self.objMtraiz.matriz[x][y][0] == self.listaQ1[i][1]:
                            self.objMtraiz.matrizDePontos[x][y] = "  \033[31m X\033[m"

                    for i in range(len(self.listaQ2)):
                        if self.objMtraiz.matriz[x][y][1] == self.listaQ2[i][0] and self.objMtraiz.matriz[x][y][0] == self.listaQ2[i][1]:
                            self.objMtraiz.matrizDePontos[x][y] = "  \033[31m X\033[m"

                    for i in range(len(self.listaQ3)):
                        if self.objMtraiz.matriz[x][y][1] == self.listaQ3[i][0] and self.objMtraiz.matriz[x][y][0] == self.listaQ3[i][1]:
                            self.objMtraiz.matrizDePontos[x][y] = "  \033[31m X\033[m"

                    for i in range(len(self.listaQ4)):
                        if self.objMtraiz.matriz[x][y][1] == self.listaQ4[i][0] and self.objMtraiz.matriz[x][y][0] == self.listaQ4[i][1]:
                            self.objMtraiz.matrizDePontos[x][y] = "  \033[31m X\033[m"

                    for i in range(len(self.listaQ5)):
                        if self.objMtraiz.matriz[x][y][1] == self.listaQ5[i][0] and self.objMtraiz.matriz[x][y][0] == self.listaQ5[i][1]:
                            self.objMtraiz.matrizDePontos[x][y] = "  \033[31m X\033[m"

                    for i in range(len(self.listaQ6)):
                        if self.objMtraiz.matriz[x][y][1] == self.listaQ6[i][0] and self.objMtraiz.matriz[x][y][0] == self.listaQ6[i][1]:
                            self.objMtraiz.matrizDePontos[x][y] = "  \033[31m X\033[m"

                    for i in range(len(self.listaQ7)):
                        if self.objMtraiz.matriz[x][y][1] == self.listaQ7[i][0] and self.objMtraiz.matriz[x][y][0] == self.listaQ7[i][1]:
                            self.objMtraiz.matrizDePontos[x][y] = "  \033[31m X\033[m"

                    for i in range(len(self.listaQ8)):
                        if self.objMtraiz.matriz[x][y][1] == self.listaQ8[i][0] and self.objMtraiz.matriz[x][y][0] == self.listaQ8[i][1]:
                            self.objMtraiz.matrizDePontos[x][y] = "  \033[31m X\033[m"
                    #       x: 1      y: 0   r: 3
                    #             ( 0, r) 
                    
                    #   ( -r, 0)             ( r, 0)
                    
                    #             ( 0, -r)
                    
                    if self.objMtraiz.matriz[x][y][1] == self.xc and self.objMtraiz.matriz[x][y][0] == self.raio + self.yc:
                         self.objMtraiz.matrizDePontos[x][y] = "  \033[31m X\033[m" #amarelo
                    if self.objMtraiz.matriz[x][y][1] == self.raio + self.xc and self.objMtraiz.matriz[x][y][0] == self.yc:
                         self.objMtraiz.matrizDePontos[x][y] = "  \033[31m X\033[m"
                    if self.objMtraiz.matriz[x][y][1] == self.xc and self.objMtraiz.matriz[x][y][0] == self.raio*(-1) + self.yc:
                         self.objMtraiz.matrizDePontos[x][y] = "  \033[31m X\033[m" #amarelo
                    if self.objMtraiz.matriz[x][y][1] == self.raio*(-1) + self.xc and self.objMtraiz.matriz[x][y][0] == self.yc:
                         self.objMtraiz.matrizDePontos[x][y] = "  \033[31m X\033[m"
