from enums.icone import Icone

class Rotacao():

    def __init__(self) -> None:
        self.senAng = None
        self.cosAng = None
        self.angulo = None
        self.matrizPivo = []
        self.matrizAngulo = []
        self.matrizPontos = []
        self.matrizPontosRotacionada = []
        self.quantidadePontos = None

    def criarMatrizAnguloPonto(self, listaParesOrdenados, indicePivo):
        self.quantidadePontos = len(listaParesOrdenados)
        
        #cria matriz de Pivo
        linhaPivo = [1, 0, listaParesOrdenados[indicePivo][0]]
        self.matrizPivo.append(linhaPivo)
        linhaPivo = [0, 1, listaParesOrdenados[indicePivo][1]]
        self.matrizPivo.append(linhaPivo)
        linhaPivo = [0, 0, 1]
        self.matrizPivo.append(linhaPivo)
        
        #cria matriz de angulos seno e cosseno
        linhaMatriz = [float(self.cosAng), float(self.senAng), 0]
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

        # multiplicação de matriz
        # for linha in range(self.quantidadePontos):
        #     print(self.matrizAngulo[linha][0]*self.matrizPontos[linha][0])

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