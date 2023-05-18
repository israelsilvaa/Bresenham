import math
from enums.icone import Icone

class Rotacao():

    def __init__(self, listaParesOrdenados):
        self.senAng = None
        self.cosAng = None
        self.angulo = None
        self.matrizPivo = []
        self.matrizAngulo = []
        self.matrizPontos = []
        self.matrizPontosRotacionada = []
        self.quantidadePontos = len(listaParesOrdenados)
        self.matrizPivoVezesPontos = []
        self.matrizAnguloVezesPontos = []

    def criarMatrizAnguloPonto(self, listaParesOrdenados, indicePivo):
        
        #cria matriz de Pivo
        linhaPivo = [1, 0, listaParesOrdenados[indicePivo][0]]
        self.matrizPivo.append(linhaPivo)
        linhaPivo = [0, 1, listaParesOrdenados[indicePivo][1]]
        self.matrizPivo.append(linhaPivo)
        linhaPivo = [0, 0, 1]
        self.matrizPivo.append(linhaPivo)
        
        #cria matriz de angulos seno e cosseno
        linhaMatriz = [float(self.cosAng), float(self.senAng)*(-1), 0]
        self.matrizAngulo.append(linhaMatriz)
        linhaMatriz = [float(self.senAng), float(self.cosAng), 0]
        self.matrizAngulo.append(linhaMatriz)
        linhaMatriz = [0, 0, 1]
        self.matrizAngulo.append(linhaMatriz)

        #cria matriz de Pontos X e Y
        for linha in range(3):
            linhaPontos = []
            for coluna in range(len(listaParesOrdenados)):
                if linha != 2:
                    linhaPontos.append(listaParesOrdenados[coluna][linha])
                else:
                    linhaPontos.append(1)
            self.matrizPontos.append(linhaPontos)

    def multiplicarMatrizes(self):

        # multiplicação de matriz
        # matriz resultante de MatPivo x MatPontos
        m = 3
        p = self.quantidadePontos
        for linha in range(m):
            linhaPivoPontos = []
            linhaAnguloPontos = []
            for coluna in range(p):
                linhaPivoPontos.append(0)
                linhaAnguloPontos.append(0)
            self.matrizPivoVezesPontos.append(linhaPivoPontos)
            self.matrizAnguloVezesPontos.append(linhaAnguloPontos)

        # matrizPivo x matrizPontos        
        for linha in range(m):
            for coluna in range(p):
                for k in range(3):
                    self.matrizPivoVezesPontos[linha][coluna] = round((self.matrizPivoVezesPontos[linha][coluna] + self.matrizAngulo[linha][k]*self.matrizPontos[k][coluna])-0.1) 
                    # self.matrizPivoVezesPontos[linha][coluna] = round(float(self.matrizPivoVezesPontos[linha][coluna] + self.matrizAngulo[linha][k]*self.matrizPontos[k][coluna])) 

        print("\n   Angulos x Pontos")
        for linha in range(3):
            for coluna in range(self.quantidadePontos):
                print(self.matrizPivoVezesPontos[linha][coluna], end="  ")
            print("")

    def pegarPontosMultiplicados(self):
        listaPontos = []

        for linha in range(self.quantidadePontos):
            linhaLista = []
            for coluna in range(2):
                linhaLista = [round(self.matrizPivoVezesPontos[0][linha]), round(self.matrizPivoVezesPontos[1][linha])]
            listaPontos.append(linhaLista)

        return listaPontos
    
    def printMatrizAnguloPonto(self):

        print("\nAngulo:"+str(self.angulo)+"°" ," ____  Sen:", self.senAng, "     Cos:", self.cosAng)

        print(Icone.COR_VERMELHO.value +"\n      Matriz de angulos"+ Icone.FIM_COR.value)
        for i in range(3):
            for x in range(3):
                if i != 2:
                    print(Icone.COR_VERMELHO.value + f"{self.matrizAngulo[i][x]}" + Icone.FIM_COR.value, end="          ")
                else:
                    print(Icone.COR_VERMELHO.value + f"{self.matrizAngulo[i][x]}" + Icone.FIM_COR.value, end="            ")
            print("\n")

        print(Icone.COR_VERDE.value +"\n      Matriz de Pivo"+ Icone.FIM_COR.value)
        for i in range(3):
            for x in range(3):
                print(Icone.COR_VERDE.value + f"{self.matrizPivo[i][x]}" + Icone.FIM_COR.value, end="          ") 
            print("\n")

        print(Icone.COR_AMARELO.value +"\n      Matriz de pontos"+ Icone.FIM_COR.value)
        for i in range(3):
            for x in range(self.quantidadePontos):
                print(Icone.COR_AMARELO.value + f"{self.matrizPontos[i][x]}" + Icone.FIM_COR.value, end="    ")
            print("\n")

    def getSenCos(self, angulo):
        self.angulo = angulo

        if angulo == 30:
            self.senAng = 0.50 
            self.cosAng = 0.87
        elif angulo == -30:
            self.senAng = -0.50
            self.cosAng = 0.87

        elif angulo == 45:
            self.senAng = 0.70
            self.cosAng = 0.70
        elif angulo == -45:
            self.senAng = -0.70
            self.cosAng = 0.70

        elif angulo == 60:
            self.senAng = 0.87
            self.cosAng = 0.50
        elif angulo == -60:
            self.senAng = -0.87
            self.cosAng = 0.50

        senCos = [self.senAng,  self.cosAng, self.angulo]
        return senCos