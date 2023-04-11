class Bresenham:
    def __init__(self, x_ini, y_ini, x_fin, y_fin, tamanhoMatriz):
        self.matriz = []
        self.matrizDePontos = []
        self.tamanhoMatriz = None
        self.x=x_ini ; self.y=y_ini; self.xf=x_fin; self.yf=y_fin
        self.inicioMatriz = 0
       
        self.inicioM = 0
        self.fimM = 0
        
        if self.x <= self.y:
            self.inicioM = self.x
        else:
            self.inicioM = self.y
        
        if self.xf >= self.yf:
            self.fimM = self.xf
        else:
            self.fimM = self.yf
            
        # self.m = (self.yf-self.y) / (self.xf-self.x)
        # if self.m > 1:
        #     self.x=y_ini ; self.y=x_ini; self.xf=y_fin; self.yf=x_fin
        #     self.m = (self.yf-self.y) / (self.xf-self.x)
            
    def criarMatriz(self):
        for x in range(self.fimM, self.inicioM-1, -1):
            linha = []
            for y in range(self.inicioM, self.fimM+1):
                coordenada = [x, y]   
                linha.append(coordenada)
            self.matriz.append(linha)
    
    def matrizAtual(self):
        for x in range(len(self.matriz)):
            for y in range(len(self.matriz)):
                
                #   x , y
                if  self.matriz[x][y][1] == 0 and self.matriz[x][y][0] == 0: 
                    print("+0+0", end=" ")
                elif  self.matriz[x][y][1] == 0 and self.matriz[x][y][0] == -3: 
                    print("+0-3", end=" ")
                else:
                    print("  . ", end=" ")
            print("\n")
        print("\nprint 2\n\n")
        
     
        
