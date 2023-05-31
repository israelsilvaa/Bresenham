from modulos.tela import Tela
from enums.icone import Icone
class Bresenham:
    def __init__(self, inicioMatriz, fimMatriz):
        self.matriz = []
        self.matrizDePontos = []
        self.inicioM = inicioMatriz
        self.fimM = fimMatriz
        self.x=None ; self.y=None; self.xf=None; self.yf=None
        self.xContadorOrigem = 0
        self.yContadorOrigem = 0
        self.trocaxy = False
        self.trocax = False
        self.trocay = False
        self.listaY = []
        self.listaX = []
        self.tela = Tela()
        self.criarMatriz()
            
    def criarMatriz(self):
        #cria matriz de coordenadas e de de pontos
        numeroEixoResumido = "."

        for x in range(self.fimM, self.inicioM-1, -1):
            linha = []
            linhapontos = []
            for y in range(self.inicioM, self.fimM+1):
                x_y_cor = [x, y, 0]   
                linha.append(x_y_cor)
                linhapontos.append("    ")
            self.matriz.append(linha)
            self.matrizDePontos.append(linhapontos)
            
        for x in range(len(self.matriz)):
            for y in range(len(self.matriz)):
                #print eixo x,y
                if self.matriz[x][y][0] == 0 and self.matriz[x][y][1] == 0:
                    self.matrizDePontos[x][y] = "   0"
                # Y
                elif self.matriz[x][y][0] == 0:
                    if self.matriz[x][y][1] > 0:
                        if self.matriz[x][y][1] > 9:
                            self.matrizDePontos[x][y] = "   "+ str(numeroEixoResumido)
                        else:
                            self.matrizDePontos[x][y] = "   "+ str(self.matriz[x][y][1])
                    else:
                        # self.matrizDePontos[x][y] = "   "+ str(self.matriz[x][y][1]*(-1))
                        if self.matriz[x][y][1] < 0:
                            if self.matriz[x][y][1] < -9:
                                self.matrizDePontos[x][y] = "   "+ str(numeroEixoResumido) # -x
                            else:
                                self.matrizDePontos[x][y] = "   "+ str(self.matriz[x][y][1]*(-1)) # -x > -10
               # X
                elif self.matriz[x][y][1] == 0:
                    self.matrizDePontos[x][y] = "   "+ str(self.matriz[x][y][0])

                    if self.matriz[x][y][0] > 0:
                        if self.matriz[x][y][0] > 9:
                            self.matrizDePontos[x][y] = "   "+ str(numeroEixoResumido) # y > 9
                        else:
                            self.matrizDePontos[x][y] = "   "+ str(self.matriz[x][y][0]) # 10 > y > 0  
                    else:
                        if self.matriz[x][y][0] < 0:
                            if self.matriz[x][y][0] > -9:
                                self.matrizDePontos[x][y] = "   "+ str(self.matriz[x][y][0]*(-1)) # -y
                            else:
                                self.matrizDePontos[x][y] = "   "+ str(numeroEixoResumido) # -y
                
    def matrizCoordenada(self):
        #matriz com todas as coordenadas dos pontos 
        corX = Icone.COR_VERMELHO.value
        corY = Icone.COR_VERDE.value
        fim = Icone.FIM_COR.value

        print("0 == Fundo(Transparente)")
        print("1 == Borda(Vermelho)")
        print("2 == Verde")
        print("3 == Amarelo")
        print("4 == Roxo")
        print("\nMatriz de coordenadas (X, Y, cor)")
        for x in range(len(self.matriz)):
            for y in range(len(self.matriz)):
                #   x , y
                print("("+corX+str(self.matriz[x][y][0])+fim+corY+str(self.matriz[x][y][1])+fim ,str(self.matriz[x][y][2]),") ", end=" ")
            print("\n")
    
    def matrizAtual(self):
        for x in range(len(self.matriz)):
            for y in range(len(self.matriz)):
                # print dos pontos vazios(onde não há retas)
                print(self.matrizDePontos[x][y], end="  ")
            print("\n")
       
    def xyParaOrigem(self):
        #leva o X para a origem(x == 0)
        if self.x > 0:
            while self.x != 0:
                self.xContadorOrigem = self.xContadorOrigem + 1
                self.x = self.x - 1
                self.xf = self.xf - 1
        elif self.x < 0:
            while self.x != 0:
                self.xContadorOrigem = self.xContadorOrigem - 1
                self.x = self.x + 1
                self.xf = self.xf + 1
        
        if self.y > 0:
            while self.y != 0:
                self.yContadorOrigem = self.yContadorOrigem + 1
                self.y = self.y - 1
                self.yf = self.yf - 1
        elif self.y < 0:
            while self.y != 0:
                self.yContadorOrigem = self.yContadorOrigem - 1
                self.y = self.y + 1
                self.yf = self.yf + 1

    def xyParaOrigemInversa(self):
        #levando X para seu lugar original
            if self.xContadorOrigem != 0:
                for i in range(len(self.listaX)):
                    self.listaX[i] = self.listaX[i] + self.xContadorOrigem
                self.xContadorOrigem = 0
         
            if self.yContadorOrigem != 0:
                for i in range(len(self.listaY)):
                    self.listaY[i] = self.listaY[i] + self.yContadorOrigem
                self.yContadorOrigem = 0
            
    def reflexao(self):
        self.m = (self.yf-self.y) / (self.xf-self.x)
        if self.m > 1 or self.m < -1:
            aux = self.x
            self.x = self.y; self.y=aux
            
            aux = self.xf
            self.xf=self.yf; self.yf=aux
            self.trocaxy = True

        if self.x > self.xf:
            self.x = self.x - self.x * 2
            self.xf = self.xf - self.xf * 2
            self.trocax = True
        
        if self.y > self.yf:
            self.y = self.y - self.y * 2
            self.yf = self.yf - self.yf * 2
            self.trocay = True

        self.m = round((self.yf-self.y) / (self.xf-self.x), 1)
              
    def reflexao_inversa(self):
        
        if self.trocay == True:
            # receber lista de pontos Y
            for i in range(len(self.listaY)):
                self.listaY[i] = self.listaY[i] - self.listaY[i] * 2
                self.trocay = False

        if self.trocax == True:
            for i in range(len(self.listaX)):
                self.listaX[i] = self.listaX[i] - self.listaX[i] * 2
                self.trocax = False

        if self.trocaxy == True:
            #trocar lista X por Y
            lista_x_aux = []
            lista_y_aux = []
            for i in range(len(self.listaY)):
                lista_x_aux.append(self.listaX[i])
                lista_y_aux.append(self.listaY[i])
                
            for i in range(len(self.listaY)):
                self.listaX[i] = lista_y_aux[i]
                self.listaY[i] = lista_x_aux[i]

            aux = self.x
            self.x = self.y; self.y=aux            
            aux = self.xf
            self.xf=self.yf; self.yf=aux
            self.trocaxy = False

    def reta(self, x_ini, y_ini, x_fin, y_fin, cor=Icone.COR_VERMELHO.value):
        #calcula os pontos da reta e a desenha na matriz de pontos
        #tendo como base a matriz de coordenadas
        self.x=x_ini ; self.y=y_ini; self.xf=x_fin; self.yf=y_fin

        """
        0 == COR FUNDO(transparente)
        1 == BORDA(VERMELHO)
        2 == COR verde
        3 == COR amarelo
        4 == COR roxo
        """
        pixelCor = 1
        if cor == 1:
            cor = Icone.COR_VERMELHO.value
            pixelCor = 1
        elif cor == 2:
            cor = Icone.COR_VERDE.value
            pixelCor = 2
        elif cor == 3:
            cor = Icone.COR_AMARELO.value
            pixelCor = 3
        elif cor == 4:
            cor = Icone.COR_ROXO.value
            pixelCor = 4
       
        if self.x != self.xf: 
            #out: branch Quadrante
            self.xyParaOrigem()
            
            self.reflexao()

            # calculando pontos da reta
            self.listaY = []
            self.listaX = []
            anterior = self.y
            for i in range(self.x, self.xf+1):
                if i == 0:
                    self.listaY.append(self.y)
                    self.listaX.append(i)
                    #anterior = i
                else:
                    anterior = anterior + self.m
                    #print("planoCartesiano: ",anterior)
                    self.listaY.append(round(anterior))
                    self.listaX.append(i)
            
            self.reflexao_inversa()
            self.xyParaOrigemInversa()
            
            for x in range(len(self.matriz)):
                for y in range(len(self.matriz)):
                    #   x , y
                    #  x = indice_1, y = indice_0
                    for i in range(len(self.listaY)):
                        if self.matriz[x][y][1] == self.listaX[i] and self.matriz[x][y][0] == self.listaY[i]:
                            # self.matrizDePontos[x][y] = "  \033[31m X\033[m"
                            self.matrizDePontos[x][y] = str(cor)+"   X"+str(Icone.FIM_COR.value)
                            self.matriz[x][y][2] = pixelCor
                           
        else:
            lista = []
           
            if self.y < self.yf:
                for i in range(self.y, self.yf+1):
                    lista.append(i)
            
                for x in range(len(self.matriz)):
                    for y in range(len(self.matriz)):
                        for i in range(len(lista)):
                            if self.matriz[x][y][1] == self.x and self.matriz[x][y][0] == lista[i]:
                                self.matrizDePontos[x][y] = str(cor)+"   X"+str(Icone.FIM_COR.value)
                                self.matriz[x][y][2] = pixelCor

            else:
                for i in range(self.y, self.yf-1, -1):
                    lista.append(i)

                for x in range(len(self.matriz)):
                    for y in range(len(self.matriz)):
                        for i in range(len(lista)):
                            if self.matriz[x][y][1] == self.x and self.matriz[x][y][0] == lista[i]:
                                self.matrizDePontos[x][y] = str(cor)+"   X"+str(Icone.FIM_COR.value)
                                self.matriz[x][y][2] = pixelCor

    def marcaPonto(self, x, y, cor=1):
        """
        0 == COR FUNDO(transparente)
        1 == BORDA(VERMELHO)
        2 == COR verde
        3 == COR amarelo
        4 == COR roxo
        """
        pixelCor = 1
        if cor == 1:
            cor = Icone.COR_VERMELHO.value
            pixelCor = 1
        elif cor == 2:
            cor = Icone.COR_VERDE.value
            pixelCor = 2
        elif cor == 3:
            cor = Icone.COR_AMARELO.value
            pixelCor = 3
        elif cor == 4:
            cor = Icone.COR_ROXO.value
            pixelCor = 4

        for linha in range(len(self.matriz)):
                for coluna in range(len(self.matriz)):
                    if self.matriz[linha][coluna][1] == x and self.matriz[linha][coluna][0] == y:
                        self.matrizDePontos[linha][coluna] = str(cor)+"   X"+str(Icone.FIM_COR.value)
                        self.matriz[linha][coluna][2] = pixelCor
        
    def execute(self):
        adicionarReta = 0
        listaParesOrdenados = []
        while True:
            
            self.tela.limparTela()
            print("Bresenham\n")
            self.matrizAtual()
            print("\nLista de pares Ordenados:", listaParesOrdenados)
            print("[0]Sair - [1]adicionar retas")
            adicionarReta = int(input("opção:"))
            
            if adicionarReta == 1:
                while True:    
                    self.tela.limparTela()
                    print("Bresenham\n")
                    self.matrizAtual()
                    print("\nLista de pares Ordenados:", listaParesOrdenados)        
                    print("!!   de enter vazio para cancelar   !!")
                    x = input("\nX Inicial:")
                    y = input("\nY Inicial:")
                    x_f = input("\nX Final:")
                    y_f = input("\nY Final:")
                    if x == "" or y == "" or x_f == "" or y_f == "":
                        break
                    parInicial = [int(x), int(y)]        
                    parFinal = [int(x_f), int(y_f)]        
                    listaParesOrdenados.append(parInicial)
                    listaParesOrdenados.append(parFinal)
                    
                    if len(listaParesOrdenados) > 1:
                        for i in range(0, len(listaParesOrdenados), 2):
                            xInicial = listaParesOrdenados[i][0]
                            yInicial = listaParesOrdenados[i][1]
                            xFinal = listaParesOrdenados[i+1][0]
                            yFinal = listaParesOrdenados[i+1][1]
                            self.reta(xInicial, yInicial, xFinal, yFinal)
            else:
                break
            