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

    def cabinet(self, listaParesOrdenados):
        self.quantidadePontos = len(listaParesOrdenados)
        self.criarMatrizCabinet()
        self.criarMatrizPontos3d(listaParesOrdenados)

        print("\nCabinet")
        for i in range(4):
            print(self.matrizCabinet[i])

        print("\npontos3d")
        for i in range(4):
            print(self.matrizPontos3d[i])

        self.multiplicaMatriz(self.matrizCabinet, self.matrizPontos3d)

        print("\nCabinet x Pontos3d")
        for i in range(4):
            print(self.matrizCabinetVezesPontos3d[i])
        
        listaParesOrdenados = self.pegarPontosMultiplicados()

        return self.escreverPontos(listaParesOrdenados)
        
    def criarMatrizPontos3d(self, listaParesOrdenados):
       
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

    def multiplicaMatriz(self, matrizA, matrizB):
        m = 4
        p = self.quantidadePontos
        for linha in range(m):
            linhaCabinetPontos = []
            for coluna in range(p):
                linhaCabinetPontos.append(0)

            self.matrizCabinetVezesPontos3d.append(linhaCabinetPontos)
        
        # matrizCabinet x matrizPontos        
        for linha in range(m):
            for coluna in range(p):
                for k in range(4):
                    self.matrizCabinetVezesPontos3d[linha][coluna] = round(self.matrizCabinetVezesPontos3d[linha][coluna] + matrizA[linha][k]*matrizB[k][coluna] + 0.1)
                   
    def pegarPontosMultiplicados(self):
        listaPontos = []

        for linha in range(self.quantidadePontos):
            linhaLista = []
            for coluna in range(3):
                linhaLista = [round(self.matrizCabinetVezesPontos3d[0][linha] + 0.1), round(self.matrizCabinetVezesPontos3d[1][linha] + 0.1)]
            listaPontos.append(linhaLista)

        return listaPontos
    
    def pegarSolido3d(self):
     
        listaParesOrdenados = []
        while True:
            self.tela.limparTela()
            print("\nLista de pares Ordenados:", listaParesOrdenados)
            print("Adicionar pares ordenados")
            print("!!!!    para cancelar apenas de ENTER no X e Y     !!!!")
            x = input("\nX:")
            y = input("\nY:")
            z = input("\nZ:")
            if x == "" or y == "" or z == "":
                break
            par = [int(x), int(y), int(z)]        
            listaParesOrdenados.append(par)
        
        self.listaParesOrdenados = listaParesOrdenados
           
        return self.listaParesOrdenados

    def escreverPontos(self, listaParesOrdenados: list):

        print(listaParesOrdenados)

        self.listaParesOrdenados = listaParesOrdenados

        for i in range(len(self.listaParesOrdenados)):
            self.listaParesOrdenados[i][0] = self.listaParesOrdenados[i][0] + (0) 
            self.listaParesOrdenados[i][1] = self.listaParesOrdenados[i][1] + (-17) 

        s = input("sdsdsdsdsds")
        
        # # A B
        # self.planoCartesiano.reta(listaParesOrdenados[0][0], listaParesOrdenados[0][1],
        #                           listaParesOrdenados[1][0], listaParesOrdenados[1][1])
        # # A D
        # self.planoCartesiano.reta(listaParesOrdenados[0][0], listaParesOrdenados[0][1],
        #                           listaParesOrdenados[3][0], listaParesOrdenados[3][1])
        # A E
        # self.planoCartesiano.reta(listaParesOrdenados[0][0], listaParesOrdenados[0][1],
        #                           listaParesOrdenados[4][0], listaParesOrdenados[4][1])
        # B C
        self.planoCartesiano.reta(listaParesOrdenados[1][0], listaParesOrdenados[1][1],
                                  listaParesOrdenados[2][0], listaParesOrdenados[2][1])
        # B F
        self.planoCartesiano.reta(listaParesOrdenados[1][0], listaParesOrdenados[1][1],
                                  listaParesOrdenados[5][0], listaParesOrdenados[5][1])
        # C D
        self.planoCartesiano.reta(listaParesOrdenados[2][0], listaParesOrdenados[2][1],
                                  listaParesOrdenados[3][0], listaParesOrdenados[3][1])
        
        # C G
        self.planoCartesiano.reta(listaParesOrdenados[2][0], listaParesOrdenados[2][1],
                                  listaParesOrdenados[6][0], listaParesOrdenados[6][1])
        # D H
        self.planoCartesiano.reta(listaParesOrdenados[3][0], listaParesOrdenados[3][1],
                                  listaParesOrdenados[7][0], listaParesOrdenados[7][1])
        
        # H E
        self.planoCartesiano.reta(listaParesOrdenados[7][0], listaParesOrdenados[7][1],
                                  listaParesOrdenados[4][0], listaParesOrdenados[4][1])
        # H G
        self.planoCartesiano.reta(listaParesOrdenados[7][0], listaParesOrdenados[7][1],
                                  listaParesOrdenados[6][0], listaParesOrdenados[6][1])
        # F G
        self.planoCartesiano.reta(listaParesOrdenados[5][0], listaParesOrdenados[5][1],
                                  listaParesOrdenados[6][0], listaParesOrdenados[6][1])
        # F E
        self.planoCartesiano.reta(listaParesOrdenados[5][0], listaParesOrdenados[5][1],
                                  listaParesOrdenados[4][0], listaParesOrdenados[4][1])
        
        return self.planoCartesiano

    