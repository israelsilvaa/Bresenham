# import random
from modulos.bresenham import Bresenham
from modulos.tela import Tela

class Projecao:

    def __init__(self, inicioMatriz, fimMatriz):
        self.tela = Tela()
        self.planoCartesiano = Bresenham(inicioMatriz, fimMatriz)
        self.listaParesOrdenados = []
        self.quantidadePontos = []
        self.matrizCabinet = []
        self.matrizPontos3d = []
        self.matrizCabinetVezesPontos3d = []

        self.matrizOrtogonal = []
        self.matrizOrtogonalVezesPontos3d = []

    def cabinet(self, listaParesOrdenados, listaArestas):
        self.quantidadePontos = len(listaParesOrdenados)
        self.criarMatrizCabinet()
        self.criarMatrizPontos3d(listaParesOrdenados)

        print("\nCabinet")
        for i in range(4):
            print(self.matrizCabinet[i])

        print("\npontos3d")
        for i in range(4):
            print(self.matrizPontos3d[i])

        self.matrizCabinetVezesPontos3d = self.multiplicaMatriz(self.matrizCabinet, self.matrizPontos3d, self.matrizCabinetVezesPontos3d)

        print("\nCabinet x Pontos3d")
        for i in range(4):
            print(self.matrizCabinetVezesPontos3d[i])
        
        listaParesOrdenados = self.pegarPontosMultiplicados(self.matrizCabinetVezesPontos3d)

        return self.escreverPontos(listaParesOrdenados, listaArestas)
    
    def ortogonal(self, listaParesOrdenados, listaArestas):
        self.quantidadePontos = len(listaParesOrdenados)
        self.criarMatrizOrtogonal()
        self.criarMatrizPontos3d(listaParesOrdenados)

        print("\nOrtogonal")
        for i in range(4):
            print(self.matrizOrtogonal[i])

        print("\npontos3d")
        for i in range(4):
            print(self.matrizPontos3d[i])

        self.matrizOrtogonalVezesPontos3d = self.multiplicaMatriz(self.matrizOrtogonal, self.matrizPontos3d, self.matrizOrtogonalVezesPontos3d)

        self.pegarPontosMultiplicados(self.matrizOrtogonalVezesPontos3d)

        print("\nOrtogonal x Pontos3d")
        for i in range(4):
            print(self.matrizOrtogonalVezesPontos3d[i])

        return self.escreverPontos(listaParesOrdenados, listaArestas)
        

    def criarMatrizOrtogonal(self):
        linha = [1, 0, 0, 0]
        self.matrizOrtogonal.append(linha)

        linha = [0, 1, 0, 0]
        self.matrizOrtogonal.append(linha)
        
        linha = [0, 0, 0, 0]
        self.matrizOrtogonal.append(linha)

        linha = [0, 0, 0, 1]
        self.matrizOrtogonal.append(linha)    

    def criarMatrizPontos3d(self, listaParesOrdenados):

        print("DEBUGGGGGG::::::",listaParesOrdenados)

       
        #cria matriz de Pontos X,Y,Z
        for linha in range(4):
            linhaPontos = []
            for coluna in range(len(listaParesOrdenados)):
                if linha != 3:
                    linhaPontos.append(listaParesOrdenados[coluna][linha])
                else:
                    linhaPontos.append(1)
            self.matrizPontos3d.append(linhaPontos)
       
    def criarMatrizCabinet(self):
        linha = [1, 0, 0.86, 0]
        self.matrizCabinet.append(linha)
        linha = [0, 1, 0.5,  0]
        self.matrizCabinet.append(linha)
        linha = [0, 0,   0,  0]
        self.matrizCabinet.append(linha)
        linha = [0, 0,   0,  1]
        self.matrizCabinet.append(linha)

    def multiplicaMatriz(self, matrizA, matrizB, matrizR):
        m = 4
        p = self.quantidadePontos
        for linha in range(m):
            linhaCabinetPontos = []
            for coluna in range(p):
                linhaCabinetPontos.append(0)

            matrizR.append(linhaCabinetPontos)
        
        # matrizCabinet x matrizPontos        
        for linha in range(m):
            for coluna in range(p):
                for k in range(4):
                    matrizR[linha][coluna] = round(matrizR[linha][coluna] + matrizA[linha][k]*matrizB[k][coluna] + 0.1)
        
        return matrizR
    
    def pegarPontosMultiplicados(self, matrizA):
        listaPontos = []

        for linha in range(self.quantidadePontos):
            linhaLista = []
            for coluna in range(3):
                linhaLista = [round(matrizA[0][linha] + 0.1), round(matrizA[1][linha] + 0.1)]
            listaPontos.append(linhaLista)

        return listaPontos
    
    def pegarSolido3d(self, listaPares):
     
        listaParesOrdenados = listaPares
        while True:
            self.tela.limparTela()
            print("\nLista de pares Ordenados:", listaParesOrdenados)
            print("Adicionar pares ordenados")
            print("!!!!    para cancelar apenas de ENTER no X, Y e Z     !!!!")
            x = input("\nX:")
            y = input("\nY:")
            z = input("\nZ:")
            if x == "" or y == "" or z == "":
                break
            par = [int(x), int(y), int(z)]        
            listaParesOrdenados.append(par)
        
        return listaParesOrdenados

    def criarArestas(self, listaParesOrdenados):
        arestas = []

        while True:
            self.tela.limparTela()
            self.planoCartesiano.matrizAtual()
            print("Indicies")
            print(end="     ")
            for indice in range(len(listaParesOrdenados)):
                print(indice, end="           ")
            print("\n")
            for indice in range(len(listaParesOrdenados)):
                print(listaParesOrdenados[indice], end=" ")
            print("\n")
            
            print("Arestas")
            if len(arestas) == 0:
                    print("nenhuma aresta cadastrada", end=" ")
            else:
                for i in range(len(arestas)):
                    print(arestas[i], end=" ")
            print("\n")

            print("!!!!    para cancelar apenas de ENTER no Ponto1 ou Ponto2     !!!!")
            inicio = input("Ponto1(indice):")
            fim = input("Ponto2(indice):")
            if inicio == "" or fim == "":
                break
            pontos = [int(inicio), int(fim)]
            arestas.append(pontos)

            self.planoCartesiano = self.escreverPontos(listaParesOrdenados, arestas)

        return arestas


    def escreverPontos(self, listaParesOrdenados: list, listaArestas:list):

        print(listaParesOrdenados)

        self.listaParesOrdenados = listaParesOrdenados

        for i in range(len(listaArestas)):
            self.planoCartesiano.reta(listaParesOrdenados[listaArestas[i][0]][0], listaParesOrdenados[listaArestas[i][0]][1],
                                    listaParesOrdenados[listaArestas[i][1]][0], listaParesOrdenados[listaArestas[i][1]][1])
       
        
        return self.planoCartesiano
        

        