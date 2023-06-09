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
        self.pivo = []
        self.matrizPivo = []
        self.matrizAngulo = []
        self.matrizPontos = []
        self.matrizPivoVezesPontos = []
        self.matrizAnguloVezesPontos = []
        self.matrizPontosRotacionada = []
        self.matrizFinal = []
        
        self.quantidadePontos = None
        self.listaParesOrdenados = None

    def fazerTranslacao(self, listaParesOrdenados:list, eixoX, eixoY):
       
        print("Pontos:",listaParesOrdenados)
        for i in range(len(listaParesOrdenados)):
            listaParesOrdenados[i][0] = listaParesOrdenados[i][0] + eixoX 
            listaParesOrdenados[i][1] = listaParesOrdenados[i][1] + eixoY 
       
        print("Pontos transladados:", listaParesOrdenados)

        pause = input("DEBUG...")

        self.escreverPontos(listaParesOrdenados)
        self.listaParesOrdenados = listaParesOrdenados
        
        return self.planoCartesiano
    

    def atualizarEscala(self, listaParesOrdenados: list, Ex, Ey, pontoFixo):
        self.quantidadePontos = len(listaParesOrdenados)

        self.criarMatrizPivo(listaParesOrdenados, pontoFixo)
        self.criarMatrizPonto(listaParesOrdenados)

        self.printMatrizPivo()
        self.printMatrizPontos()

        self.matrizPivoVezesPontos = self.multiplicaMatriz(self.matrizPivo, self.matrizPontos, self.matrizPivoVezesPontos)
        self.printMatrizPivoVezesPontos()

        listaParesOrdenados = self.pegarPontosMultiplicados(self.matrizPivoVezesPontos)

        for i in range(len(listaParesOrdenados)):
            listaParesOrdenados[i][0] = int(listaParesOrdenados[i][0] * Ex) 
            listaParesOrdenados[i][1] = int(listaParesOrdenados[i][1] * Ey)
        
        print("Pontos escalados(x * Ex  e  y *Ey):\n",listaParesOrdenados)

        for i in range(len(listaParesOrdenados)):
            listaParesOrdenados[i][0] = int(listaParesOrdenados[i][0] + self.pivo[0]) 
            listaParesOrdenados[i][1] = int(listaParesOrdenados[i][1] + self.pivo[1])
       
        print("\nPontos escalados + pivo(voltar poligono p/ o pivo):\n", listaParesOrdenados)
       
        pause = input("DEBUG...")

        self.listaParesOrdenados = listaParesOrdenados
        self.escreverPontos(listaParesOrdenados)

        return self.planoCartesiano
    
    def multiplicaMatriz(self, matrizA, matrizB, matrizR):
        m = 3
        p = self.quantidadePontos
        for linha in range(m):
            linhaCabinetPontos = []
            for coluna in range(p):
                linhaCabinetPontos.append(0)
            matrizR.append(linhaCabinetPontos)
              
        for linha in range(m):
            for coluna in range(p):
                for k in range(3):
                    matrizR[linha][coluna] = round(matrizR[linha][coluna] + matrizA[linha][k]*matrizB[k][coluna] + 0.1)
        
        return matrizR
       
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
        
        self.criarMatrizPivo(listaParesOrdenados, indicePivo)
        self.criaMatrizAngulo(angulo)
        self.criarMatrizPonto(listaParesOrdenados)
        
        self.printMatrizPivo()
        self.printMatrizAngulo()
        self.printMatrizPontos()
        
        # matrizPivo x matrizPontos 
        self.multiplicaMatriz(self.matrizPivo, self.matrizPontos, self.matrizPivoVezesPontos)
        self.printMatrizPivoVezesPontos()

        # matrizAngulo x matrizPontos 
        self.multiplicaMatriz(self.matrizAngulo, self.matrizPivoVezesPontos, self.matrizPontosRotacionada)
        self.printMatrizAnguloVezesPontos()
        
        # Pivo inverso
        self.matrizPivo[0][2] = self.pivo[0] 
        self.matrizPivo[1][2] = self.pivo[1] 
        self.printMatrizPivo()
        
        # matrizPivoInverso x matrizPontosRotacionados 
        self.multiplicaMatriz(self.matrizPivo, self.matrizPontosRotacionada, self.matrizFinal)
        self.printMatrizFinal()

        self.listaParesOrdenados = self.pegarPontosMultiplicados(self.matrizFinal)
        
        self.escreverPontos(self.listaParesOrdenados)

        pause = input("DEBUG...")
        return self.planoCartesiano
    
    def criarMatrizPivo(self, listaParesOrdenados, pontoFixo):
        self.pivo = listaParesOrdenados[pontoFixo].copy()
        
        #cria matriz de Pivo
        linhaPivo = [1, 0, self.pivo[0]*(-1)]    
        self.matrizPivo.append(linhaPivo)        
        linhaPivo = [0, 1, self.pivo[1]*(-1)]    
        self.matrizPivo.append(linhaPivo)
        linhaPivo = [0, 0, 1]
        self.matrizPivo.append(linhaPivo)
            #                   1  0  -px
            # MatrizPonto =     0  1  -py
            #                   0  0  1

    def criaMatrizAngulo(self, angulo): 
        self.getSenCos(angulo)
        
        #cria matriz de angulos seno e cosseno
        linhaMatriz = [float(self.cosAng), float(self.senAng)*(-1), 0]
        self.matrizAngulo.append(linhaMatriz)
        linhaMatriz = [float(self.senAng), float(self.cosAng), 0]
        self.matrizAngulo.append(linhaMatriz)
        linhaMatriz = [0, 0, 1]
        self.matrizAngulo.append(linhaMatriz)

        #                   cos  -sen  0
        # Ang   =           sen  cos   0
        #                   0    0    1

    def criarMatrizPonto(self, listaParesOrdenados): 
        #cria matriz de Pontos X e Y
        for linha in range(3):
            linhaPontos = []
            for coluna in range(len(listaParesOrdenados)):
                if linha != 2:
                    linhaPontos.append(listaParesOrdenados[coluna][linha])
                else:
                    linhaPontos.append(1)
            self.matrizPontos.append(linhaPontos)
            # a(2,3)   b(5,7)  c(0,3)
            #                   2  5  0
            # MatrizPonto =     3  7  3
            #                   1  1  1
    def pegarPontosMultiplicados(self, matriz):
        listaPontos = []

        for linha in range(self.quantidadePontos):
            linhaLista = []
            for coluna in range(2):
                linhaLista = [round(matriz[0][linha] + 0.1), round(matriz[1][linha] + 0.1)]
            listaPontos.append(linhaLista)

        return listaPontos
    
    def printMatrizPivo(self):
        print(Icone.COR_VERDE.value +"\n      Matriz de Pivo"+ Icone.FIM_COR.value)
        for i in range(3):
            for x in range(3):
                print(Icone.COR_VERDE.value + f"{self.matrizPivo[i][x]}" + Icone.FIM_COR.value, end="          ") 
            print("\n")
       
    def printMatrizAngulo(self):
        print("\nAngulo:"+str(self.angulo)+"°" ," ____  Sen:", self.senAng, "     Cos:", self.cosAng)
        print(Icone.COR_VERMELHO.value +"\n      Matriz de angulos"+ Icone.FIM_COR.value)
        for i in range(3):
            for x in range(3):
                if i != 2:
                    print(Icone.COR_VERMELHO.value + f"{self.matrizAngulo[i][x]}" + Icone.FIM_COR.value, end="          ")
                else:
                    print(Icone.COR_VERMELHO.value + f"{self.matrizAngulo[i][x]}" + Icone.FIM_COR.value, end="            ")
            print("\n")

    def printMatrizPontos(self):
        print(Icone.COR_AMARELO.value +"\n      Matriz de pontos"+ Icone.FIM_COR.value)
        for i in range(3):
            for x in range(self.quantidadePontos):
                print(Icone.COR_AMARELO.value + f"{self.matrizPontos[i][x]}" + Icone.FIM_COR.value, end="    ")
            print("\n")

    def printMatrizPivoVezesPontos(self):
        print(Icone.COR_AMARELO.value +"\n      pivo x pontos"+ Icone.FIM_COR.value)
        for i in range(3):
            for x in range(self.quantidadePontos):
                print(Icone.COR_AMARELO.value + f"{self.matrizPivoVezesPontos[i][x]}" + Icone.FIM_COR.value, end="    ")
            print("\n")
       
    def printMatrizAnguloVezesPontos(self):
        print(Icone.COR_AMARELO.value +"\n      Angulo x pontos(rotacionada)"+ Icone.FIM_COR.value)
        for i in range(3):
            for x in range(self.quantidadePontos):
                print(Icone.COR_AMARELO.value + f"{self.matrizPontosRotacionada[i][x]}" + Icone.FIM_COR.value, end="    ")
            print("\n")

    def printMatrizFinal(self):
        print(Icone.COR_AMARELO.value +"\n      Matriz de final"+ Icone.FIM_COR.value)
        for i in range(3):
            for x in range(self.quantidadePontos):
                print(Icone.COR_AMARELO.value + f"{self.matrizFinal[i][x]}" + Icone.FIM_COR.value, end="    ")
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

        elif angulo == 90:
            self.senAng = 1
            self.cosAng = 0
        elif angulo == -90:
            self.senAng = -1
            self.cosAng = 0
        
        else : # 30°
            self.senAng = 0.50 
            self.cosAng = 0.87

        senCos = [self.senAng,  self.cosAng, self.angulo]

        return senCos