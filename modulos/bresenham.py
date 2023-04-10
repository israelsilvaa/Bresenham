class Bresenham:
    def __init__(self, x_ini, y_ini, x_fin, y_fin, tamanhoMatriz):
        self.matriz = []
        self.tamanhoMatriz = None
        self.x=x_ini ; self.y=y_ini; self.xf=x_fin; self.yf=y_fin
        self.inicioMatriz = 0
       
        self.inicioM = 0
        self.fimM = 0
        
        if self.x <= self.y:
            self.inicioM = self.x - 1
        else:
            self.inicioM = self.y - 1
        
        if self.xf >= self.yf:
            self.fimM = self.xf + 2
        else:
            self.fimM = self.yf + 2
            
        # self.m = (self.yf-self.y) / (self.xf-self.x)
        # if self.m > 1:
        #     self.x=y_ini ; self.y=x_ini; self.xf=y_fin; self.yf=x_fin
        #     self.m = (self.yf-self.y) / (self.xf-self.x)
            
    def criarMatriz(self):
        matriz = []
        for x in range(self.inicioM, self.fimM):
            linha = []
            for y in range(self.inicioM, self.fimM):
                linha.append(".")  
            matriz.append(linha)
    
    def matrizAtual(self):
        for x in range(self.fimM, self.inicioM, -1):
            for y in range(self.inicioM, self.fimM):
                print(y, x, end="       ")             
            print("\n")
        
