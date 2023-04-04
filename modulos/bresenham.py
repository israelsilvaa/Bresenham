class Bresenham:
    matriz = []
    x = None;
    y = None;
    xf = None;
    yf = None
    m = None
    tamanhoMatriz = None
    zero_zero = None

    def __init__(self, x_ini, y_ini, x_fin, y_fin, tamanhoMatriz):

        global matriz
        global x
        global y
        global xf
        global yf
        global zero_zero
        self.x = x_ini
        self.y = y_ini
        self.xf = x_fin
        self.yf = y_fin
        self.tamanhoMatriz = tamanhoMatriz

        self.m = (self.yf - self.y) / (self.xf - self.x)
        if self.m > 1:
            self.x = y_ini
            self.y = x_ini
            self.xf = y_fin
            self.yf = x_fin
            self.m = (self.yf - self.y) / (self.xf - self.x)

        print("OK m:" , self.m)

        # 2,3 - 3,9
        if self.x > 0:
            self.zero_zero = 0
            for i in range(self.x, 0, -1):
                self.zero_zero = self.zero_zero + 1
                self.x = self.x - 1
            self.xf = self.xf - self.zero_zero
        print("ZERO:  ", self.zero_zero)

        for i in range(self.tamanhoMatriz):
            linha = []
            for x in range(self.tamanhoMatriz):
                linha.append(" .")
                # linha.append(str(i)+str(x))
            self.matriz.append(linha)
        print(self.x, self.y, self.xf, self.yf)

        self.matriz[self.x][self.y] = str(self.x) + str(self.y)
        self.matriz[self.yf][self.xf] = str(self.xf) + str(self.yf)

    # v = 7
    def matrizAtual(self):
        global matriz
        global tamanhoMatriz

        for linha in range(self.tamanhoMatriz - 1, -1, -1):
            for coluna in range(self.tamanhoMatriz):
                if (coluna == 0):
                    print(linha, end="_  ")
                print(self.matriz[linha][coluna], ' ', end='')
            print("\n")
        print("    ", end="")
        for i in range(self.tamanhoMatriz):
            print(" " + str(i), end="  ")

    def reta(self):
        global matriz;
        global x;
        global y;
        global xf;
        global yf
        global m;
        global tamanhoMatriz

        pontoY = 0
        listaY = []
        listaX = []

        for i in range(1, self.xf):
            listaX.append(i)
            if i > 0:
                pontoY = pontoY + self.m
                listaY.append(round(pontoY))
            else:
                pontoY = pontoY
                listaY.append(pontoY)
                # print("X:", l,"Y_round:", pontoY)
            self.matriz[listaY[i - 1]][listaX[i - 1]] = "X"

        self.x = self.x + self.zero_zero
        self.xf = self.xf + self.zero_zero
        for i in range(self.zero_zero):
            listaX[i] = listaX[i] + self.zero_zero

        for linha in range(self.tamanhoMatriz - 1, -1, -1):
            for coluna in range(self.tamanhoMatriz):
                self.matriz[linha][coluna] = " ."
                if (self.x == linha and coluna == self.y) or (self.xf == coluna and self.yf == coluna):
                    self.matriz[linha][coluna] = str(linha) + str(coluna)

        print(self.x, self.y, self.xf, self.yf)
        for linha in range(len(listaX)):
            print("Linha:" , linha , "Coluna" , coluna)
            self.matriz[listaX[linha]][listaY[linha]] = " X"

        print("Lista X: ", listaX)
        print("Lista Y: ", listaY)

        # for linha in range(len(listax)):
        # matriz[listax[linha]][listay[linha]] = "x"
