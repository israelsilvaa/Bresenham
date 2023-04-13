class Bresenham:
    def __init__(self, inicioMatriz, fimMatriz):
        self.matriz = []
        self.matrizDePontos = []
        self.inicioM = inicioMatriz
        self.fimM = fimMatriz
        self.x=None ; self.y=None; self.xf=None; self.yf=None
        self.quadrante2 = 0
        
        self.criarMatriz()

            
    def criarMatriz(self):
        #cria matriz de coordenadas e de de pontos
        for x in range(self.fimM, self.inicioM-1, -1):
            linha = []
            linhapontos = []
            for y in range(self.inicioM, self.fimM+1):
                coordenada = [x, y]   
                linha.append(coordenada)
                linhapontos.append("  .")
            self.matriz.append(linha)
            self.matrizDePontos.append(linhapontos)

    def matrizCoordenada(self):
        #matriz com todas as coordenadas dos pontos 
        for x in range(len(self.matriz)):
            for y in range(len(self.matriz)):
                #   x , y
                print("(",self.matriz[x][y][0],self.matriz[x][y][1],") ", end=" ")
            print("\n")
        print("\n Fim matrz de coordenadas\n\n")
    
    def matrizAtual(self):
        for x in range(len(self.matriz)):
            for y in range(len(self.matriz)):
                
                #print eixo x,y
                if self.matriz[x][y][0] == 0 and self.matriz[x][y][1] == 0:
                    self.matrizDePontos[x][y] = "  +"
                elif self.matriz[x][y][0] == 0:
                    self.matrizDePontos[x][y] = "  -"
                elif self.matriz[x][y][1] == 0:
                    self.matrizDePontos[x][y] = "  |"
                    
                # print coluna de indices (Eixo Y)
                if self.matriz[x][y][1] == self.inicioM:
                    if self.matriz[x][y][0] > -1:
                        print("",self.matriz[x][y][0], end="")
                    else:
                        print(self.matriz[x][y][0], end="")
                    
                # print dos pontos vazios(onde não há retas)
                print(self.matrizDePontos[x][y], end=" ")

            print("\n")
        
        # print linha de indices (eixo X)
        for i in range(self.inicioM, self.fimM+1):
            if i == self.inicioM:
                print("    ", i,end="  ")
            else:
                print(i, end="   ")
            
        print("\nFim matriz atual ------------------\n\n")
        
    #x = 0; y = 3; xf = 3; yf = 9
    def paraOrigem(self):
        #leva o X para a origem(x == 0)
        contador = 0
        print("x:", self.x," y:", self.y," xf:", self.xf," yf:", self.yf, "\n")
        
        while self.x > 0:
            contador = contador +1
            self.x = self.x-1
            self.xf = self.xf-1
        print("x:", self.x," y:", self.y," xf:", self.xf," yf:", self.yf, "\n")
            
            
    def reta(self, x_ini, y_ini, x_fin, y_fin):
        #calcula os pontos da reta e a desenha na matriz de pontos
        #tendo como base a matriz de coordenadas
        self.x=x_ini ; self.y=y_ini; self.xf=x_fin; self.yf=y_fin

        # print pontos iniciais e finais dados para fazer a reta 
        for x in range(len(self.matriz)):
            for y in range(len(self.matriz)):
                if self.matriz[x][y][0] == self.y and self.matriz[x][y][1] == self.x:
                    self.matrizDePontos[x][y] = "  X"
                elif self.matriz[x][y][0] == self.yf and self.matriz[x][y][1] == self.xf:
                    #print("x:", self.x," y:", self.y," xf:", self.xf," yf:", self.yf)
                    self.matrizDePontos[x][y] = "  X"

        # calculo do M
        # 1º quadrante
        self.m = (self.yf-self.y) / (self.xf-self.x)
        print("m: ",self.m)     
        print("x:", self.x," y:", self.y," xf:", self.xf," yf:", self.yf, "\n")

        # 2º quadrante
        if self.m > 1:
            self.quadrante2 = 1
            self.x=y_ini ; self.y=x_ini; self.xf=y_fin; self.yf=x_fin
            self.m = (self.y-self.x) / (self.yf-self.xf)
            print("m: ",self.m)     
            print("x:", self.x," y:", self.y," xf:", self.xf," yf:", self.yf, "\n ok, pronto para calcular os ponto s da reta\n")

        #calculando pontos da reta
        listaY = []
        listaX = []
        anterior = 0
        for i in range(self.x, self.xf+1):
            if i == 0:
                listaY.append(i)
                listaX.append(i)
                anterior = i
            else:
                anterior = anterior + self.m
                listaY.append(round(anterior + 0.5))
                listaX.append(i)

        
        print("lista de pontos da reta:")
        if self.quadrante2 == 0:
            print("listaX:", listaX)
            print("listaY:", listaY, "\n")
        else:
            print("listaX:", listaY)
            print("listaY:", listaX, "\n")

        # for x in range(self.x, self.xf+1):
        #     for y in range(self.x, self.xf+1):
        #         var_x = self.matriz[x][y][0]
        #         var_y = self.matriz[x][y][1]
        #         for i in range(len(listaY)):
        #             if var_x == i and var_y == listaY[i]:
        #                 self.matrizDePontos[x][y] = "x"
                
