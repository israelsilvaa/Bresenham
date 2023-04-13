class Bresenham:
    def __init__(self, x_ini, y_ini, x_fin, y_fin):
        self.matriz = []
        self.matrizDePontos = []
        self.tamanhoMatriz = None
        self.x=x_ini ; self.y=y_ini; self.xf=x_fin; self.yf=y_fin
        self.inicioMatriz = 0
       
        self.inicioM = 0
        self.fimM = 0
        
        if self.x <= self.y:
            self.inicioM = self.x - 2
        else:
            self.inicioM = self.y - 2
        
        if self.xf >= self.yf:
            self.fimM = self.xf + 2
        else:
            self.fimM = self.yf + 2
            
        self.m = (self.yf-self.y) / (self.xf-self.x)
        
        if self.m > 1:
            print("m: ",self.m)     
            self.x=y_ini ; self.y=x_ini; self.xf=y_fin; self.yf=x_fin
            self.m = (self.y-self.x) / (self.yf-self.xf)
            
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
                        
                # print pontos iniciais e finais dados para fazer a reta
                if self.matriz[x][y][0] == self.y and self.matriz[x][y][1] == self.x:
                    self.matrizDePontos[x][y] = "  X"
                elif self.matriz[x][y][0] == self.yf and self.matriz[x][y][1] == self.xf:
                    #print("x:", self.x," y:", self.y," xf:", self.xf," yf:", self.yf)
                    self.matrizDePontos[x][y] = "  X"
                    
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
        print("x:", self.x," y:", self.y," xf:", self.xf," yf:", self.yf)
        
        while self.x > 0:
            contador = contador +1
            self.x = self.x-1
            self.xf = self.xf-1
        print("x:", self.x," y:", self.y," xf:", self.xf," yf:", self.yf)
            
            
    def reta(self):
        #calcula os pontos da reta e a desenha na matriz de pontos
        #tendo como base a matriz de coordenadas

        #print("reta:",self.paraOrigem())
        listaY = []
        anterior = 0
        for i in range(self.x, self.xf+1):
            if i == 0:
                listaY.append(i)
                anterior = i
            else:
                anterior = anterior + self.m
                listaY.append(round(anterior))
        print("listaY:", listaY)

        for x in range(self.x, self.xf+1):
            for y in range(self.x, self.xf+1):
                var_x = self.matriz[x][y][1]
                var_y = self.matriz[x][y][0]
                for i in range(len(listaY)):
                    if var_x == i and var_y == listaY[i]:
                        self.matrizDePontos[x][y] = "x"
                
