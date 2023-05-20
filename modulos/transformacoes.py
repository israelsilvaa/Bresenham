from enums.icone import Icone
from modulos.bresenham import Bresenham
from modulos.tela import Tela

class Transformacoes:

    def __init__(self, inicioMatriz, fimMatriz):
        self.planoCartesiano = Bresenham(inicioMatriz, fimMatriz)
        self.inicioMatriz = inicioMatriz
        self.fimMatriz = fimMatriz

        # rotação -----------------
        self.senAng = None
        self.cosAng = None
        self.angulo = None
        self.matrizPivo = []
        self.matrizAngulo = []
        self.matrizPontos = []
        self.matrizPontosRotacionada = []
        self.quantidadePontos = None
        self.matrizPivoVezesPontos = []
        self.matrizAnguloVezesPontos = []
        self.listaParesOrdenados = None

    def fazerTranslacao(self, listaParesOrdenados:list, eixoX, eixoY):
        for i in range(len(listaParesOrdenados)):
            listaParesOrdenados[i][0] = listaParesOrdenados[i][0] + eixoX 
            listaParesOrdenados[i][1] = listaParesOrdenados[i][1] + eixoY 

        self.escreverPontos(listaParesOrdenados)
        
        return self.planoCartesiano
    

    def atualizarEscala(self, listaParesOrdenados: list,Ex, Ey, pontoFixo):

        for i in range(len(listaParesOrdenados)):
            if i != pontoFixo:
                listaParesOrdenados[i][0] = int(listaParesOrdenados[i][0] * Ex) 
                listaParesOrdenados[i][1] = int(listaParesOrdenados[i][1] * Ey)
        
        self.escreverPontos(listaParesOrdenados)
    
        return self.planoCartesiano
                
    def escreverPontos(self, listaParesOrdenados: list):
        if len(listaParesOrdenados) > 1:
            for i in range(0, len(listaParesOrdenados)-1):
                if i < len(listaParesOrdenados):
                    xInicial = listaParesOrdenados[i][0]
                    yInicial = listaParesOrdenados[i][1]
                    xFinal = listaParesOrdenados[i+1][0]
                    yFinal = listaParesOrdenados[i+1][1]
                    self.planoCartesiano.reta(xInicial, yInicial, xFinal, yFinal)

            xFinal = listaParesOrdenados[-1][0]
            yFinal = listaParesOrdenados[-1][1]
            self.planoCartesiano.reta(listaParesOrdenados[0][0], listaParesOrdenados[0][1], xFinal, yFinal)
    
    def pegarPontos(self):
        tela = Tela()
        listaParesOrdenados = []

        while True:
            tela.limparTela()
            self.planoCartesiano.matrizAtual()
            print("\nLista de pares Ordenados:", listaParesOrdenados)
            print("Adicionar pares ordenados")
            print("!!!!    para cancelar apenas de ENTER no X e Y     !!!!")
            x = input("\nX:")
            y = input("\nY:")
            if x == "" or y == "":
                break
            par = [int(x), int(y)]        
            listaParesOrdenados.append(par)

            self.planoCartesiano = Bresenham(self.inicioMatriz, self.fimMatriz)

            if len(listaParesOrdenados) > 1:
                for i in range(0, len(listaParesOrdenados)-1):
                    if i < len(listaParesOrdenados):
                        xInicial = listaParesOrdenados[i][0]
                        yInicial = listaParesOrdenados[i][1]
                        xFinal = listaParesOrdenados[i+1][0]
                        yFinal = listaParesOrdenados[i+1][1]
                        self.planoCartesiano.reta(xInicial, yInicial, xFinal, yFinal)
                xFinal = listaParesOrdenados[-1][0]
                yFinal = listaParesOrdenados[-1][1]
                self.planoCartesiano.reta(listaParesOrdenados[0][0], listaParesOrdenados[0][1], xFinal, yFinal)
        return listaParesOrdenados
    

    #-----------------ROTAÇÂO------------------------#

    def fazerRotacao(self, angulo, indicePivo, listaParesOrdenados):
        self.quantidadePontos = len(listaParesOrdenados)

        angulo = self.getSenCos(angulo)
        
        self.criarMatrizAnguloPonto(listaParesOrdenados, indicePivo)
        
        self.printMatrizAnguloPonto()

        self.multiplicarMatrizes()
        
        self.listaParesOrdenados = self.pegarPontosMultiplicados()
        self.escreverPontos(self.listaParesOrdenados)

        return self.planoCartesiano

    
    def criarMatrizAnguloPonto(self, listaParesOrdenados, indicePivo):
        
        #cria matriz de Pivo
        if self.angulo > 0:
            linhaPivo = [1, 0, listaParesOrdenados[indicePivo][0]]
            self.matrizPivo.append(linhaPivo)
            linhaPivo = [0, 1, listaParesOrdenados[indicePivo][1]]
            self.matrizPivo.append(linhaPivo)
            linhaPivo = [0, 0, 1]
            self.matrizPivo.append(linhaPivo)
        else:
            linhaPivo = [1, 0, listaParesOrdenados[indicePivo][0]*(-1)]
            self.matrizPivo.append(linhaPivo)
            linhaPivo = [0, 1, listaParesOrdenados[indicePivo][1]*(-1)]
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
                    self.matrizAnguloVezesPontos[linha][coluna] = (self.matrizPivoVezesPontos[linha][coluna] + self.matrizAngulo[linha][k]*self.matrizPontos[k][coluna])
                    # self.matrizPivoVezesPontos[linha][coluna] = round(float(self.matrizPivoVezesPontos[linha][coluna] + self.matrizAngulo[linha][k]*self.matrizPontos[k][coluna])) 

        print("\n   Angulos x Pontos")
        for linha in range(3):
            for coluna in range(self.quantidadePontos):
                print(round(self.matrizPivoVezesPontos[linha][coluna]), end="  ")
            print("")

    def pegarPontosMultiplicados(self):
        listaPontos = []

        for linha in range(self.quantidadePontos):
            linhaLista = []
            for coluna in range(2):
                linhaLista = [round(self.matrizAnguloVezesPontos[0][linha]), round(self.matrizAnguloVezesPontos[1][linha])]
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