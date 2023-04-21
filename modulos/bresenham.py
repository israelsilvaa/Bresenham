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
        self.criarMatriz()
            
    def criarMatriz(self):
        #cria matriz de coordenadas e de de pontos
        """
        0 == COR DO FUNDO
        1 == COR DA BORDA(VERMELHO)
        2 == COR DO PREENCEMENTO
        """
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
                    self.matrizDePontos[x][y] = "  0,0"
                # X
                elif self.matriz[x][y][0] == 0:
                    if self.matriz[x][y][1] > 0:
                        self.matrizDePontos[x][y] = "   "+ str(self.matriz[x][y][1])
                    else:
                        self.matrizDePontos[x][y] = "  "+ str(self.matriz[x][y][1])
                elif self.matriz[x][y][1] == 0:
                    self.matrizDePontos[x][y] = "  "+ str(self.matriz[x][y][0])

                    if self.matriz[x][y][0] > 0:
                        self.matrizDePontos[x][y] = "   "+ str(self.matriz[x][y][0])
                    else:
                        self.matrizDePontos[x][y] = "  "+ str(self.matriz[x][y][0])
                
    def matrizCoordenada(self):
        #matriz com todas as coordenadas dos pontos 
        for x in range(len(self.matriz)):
            for y in range(len(self.matriz)):
                #   x , y
                print("(",self.matriz[x][y][0],self.matriz[x][y][1],self.matriz[x][y][2],") ", end=" ")
            print("\n")
        print("\n Fim matrz de coordenadas (X, Y, cor)\n\n")
    
    def matrizAtual(self):
        for x in range(len(self.matriz)):
            for y in range(len(self.matriz)):
                # print dos pontos vazios(onde não há retas)
                print(self.matrizDePontos[x][y], end=" ")
            print("\n")
        print("\nFim matriz atual                                   \n", end="")
        
    #x = 0; y = 3; xf = 3; yf = 9
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
            print("xcont:" , self.xContadorOrigem, self.yContadorOrigem)

            if self.xContadorOrigem != 0:
                print("teste")
                for i in range(len(self.listaX)):
                    self.listaX[i] = self.listaX[i] + self.xContadorOrigem
                self.xContadorOrigem = 0
         
            if self.yContadorOrigem != 0:
                print("teste y")

                for i in range(len(self.listaY)):
                    self.listaY[i] = self.listaY[i] + self.yContadorOrigem
                self.yContadorOrigem = 0
            
            print("origem inversa:")
            for i in range(len(self.listaY)):
                print("(", self.listaX[i], " ," , self.listaY[i], ")")
            
          
           
    #out: branch Quadrante       
    def reflexao(self):
        self.m = (self.yf-self.y) / (self.xf-self.x)
        print("(", self.x, self.y,")    (", self.xf, self.yf,")")
        if self.m > 1 or self.m < -1:
            aux = self.x
            self.x = self.y; self.y=aux
            
            aux = self.xf
            self.xf=self.yf; self.yf=aux
            self.trocaxy = True
        print("(", self.x, self.y,")    (", self.xf, self.yf,")")

        if self.x > self.xf:
            self.x = self.x - self.x * 2
            self.xf = self.xf - self.xf * 2
            self.trocax = True
        
        if self.y > self.yf:
            self.y = self.y - self.y * 2
            self.yf = self.yf - self.yf * 2
            self.trocay = True

        self.m = round((self.yf-self.y) / (self.xf-self.x), 1)
        print("(", self.x, self.y,")    (", self.xf, self.yf,")", self.m)
       

    #out: branch Quadrante        
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

    def reta(self, x_ini, y_ini, x_fin, y_fin):
        #calcula os pontos da reta e a desenha na matriz de pontos
        #tendo como base a matriz de coordenadas
        self.x=x_ini ; self.y=y_ini; self.xf=x_fin; self.yf=y_fin
       
        # print pontos iniciais e finais dados para fazer a reta 
        # for x in range(len(self.matriz)):
        #     for y in range(len(self.matriz)):
        #         if self.matriz[x][y][0] == self.y and self.matriz[x][y][1] == self.x:
        #             self.matrizDePontos[x][y] = "  \033[32m i\033[m"
                # elif self.matriz[x][y][0] == self.yf and self.matriz[x][y][1] == self.xf:
                #     #print("x:", self.x," y:", self.y," xf:", self.xf," yf:", self.yf)
                #     self.matrizDePontos[x][y] = "  \033[32m f\033[m"
        
        if self.x != self.xf: 
            #out: branch Quadrante
            self.xyParaOrigem()
            print("-----retorno para origem-------(", self.x, self.y,")    (", self.xf, self.yf,")")

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
                    #print("TESTE: ",anterior)
                    self.listaY.append(round(anterior + 0.1))
                    self.listaX.append(i)
            
            print("Pontos calculados:")
            for i in range(len(self.listaY)):
                print("(", self.listaX[i], " ," , self.listaY[i], ")")
            
            self.reflexao_inversa()
            self.xyParaOrigemInversa()
            
        
        # print("passo 2:")
        # for i in range(len(self.listaY)):
        #     print("(", self.listaX[i], " ," , self.listaY[i], ")")

        # print("tt  x:", self.x," y:", self.y," xf:", self.xf," yf:", self.yf, "\n")
      

        # print("DEPOIS da inversa\n( x  , y )")
        # for i in range(len(self.listaY)):
        #     print("(", self.listaX[i], " ," , self.listaY[i], ")")

            for x in range(len(self.matriz)):
                for y in range(len(self.matriz)):
                    #   x , y
                    #  x = indice_1, y = indice_0
                    for i in range(len(self.listaY)):
                        if self.matriz[x][y][1] == self.listaX[i] and self.matriz[x][y][0] == self.listaY[i]:
                            self.matrizDePontos[x][y] = "  \033[31m X\033[m"
                            self.matriz[x][y][2] = 1

                            """
                            0 == COR DO FUNDO
                            1 == COR DA BORDA(VERMELHO)
                            2 == COR DO PREENCEMENTO
                            """
        else:
            lista = []
           
            if self.y < self.yf:
                for i in range(self.y, self.yf+1):
                    lista.append(i)
                print("Pontos calculados:", lista)
                
            
                for x in range(len(self.matriz)):
                    for y in range(len(self.matriz)):
                        for i in range(len(lista)):
                            if self.matriz[x][y][1] == self.x and self.matriz[x][y][0] == lista[i]:
                                self.matrizDePontos[x][y] = "  \033[31m X\033[m"
            else:
                for i in range(self.y, self.yf-1, -1):
                    lista.append(i)
                print("Pontos calculados:", lista)

                
                for x in range(len(self.matriz)):
                    for y in range(len(self.matriz)):
                        for i in range(len(lista)):
                            if self.matriz[x][y][1] == self.x and self.matriz[x][y][0] == lista[i]:
                                self.matrizDePontos[x][y] = "  \033[31m X\033[m"

                            


        # print("\n Fim matrz de coordenadas\n\n")
        # for x in range(self.x, self.xf+1):
        #     for y in range(self.x, self.xf+1):
        #         var_x = self.matriz[x][y][0]
        #         var_y = self.matriz[x][y][1]

        #         #print("comparando com", var_x, var_y)
        #         for i in range(len(listaY)):
        #             if var_x == listaX[i] and var_y == listaY[i]:
        #                 self.matrizDePontos[x][y] = " x"
                
            
