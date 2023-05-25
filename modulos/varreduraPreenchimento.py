from modulos.bresenham import Bresenham
from enums.icone import Icone
from modulos.tela import Tela

class VarreduraPreenchimento:

    def __init__(self,inicioMatriz, fimMatriz):
        self.planoCartesiano = Bresenham(inicioMatriz, fimMatriz)
        self.inicioMatriz = inicioMatriz
        self.fimMatriz = fimMatriz
        self.arestasVarredura = []
        self.listaInterseccoes = []
    
    def criaTabelaVarredura(self, listaParesOrdenados):  
        #pega os valores ymin, ymax, X_ymin e M p/ aresta
        if len(listaParesOrdenados) > 1:
                for i in range(0, len(listaParesOrdenados)-1):
                    if i < len(listaParesOrdenados):
                        if listaParesOrdenados[i][1] < listaParesOrdenados[i+1][1]:
                            y_minimo = listaParesOrdenados[i][1]
                            y_maximo = listaParesOrdenados[i+1][1]
                            x_yminimo = listaParesOrdenados[i][0]
                        else:
                            y_minimo = listaParesOrdenados[i+1][1]
                            y_maximo = listaParesOrdenados[i][1]
                            x_yminimo = listaParesOrdenados[i+1][0]
                            
                        #calcula o M
                        m =  (listaParesOrdenados[i+1][1]-listaParesOrdenados[i][1]) / (listaParesOrdenados[i+1][0]-listaParesOrdenados[i][0])
                        m = round(1 / m, 2)
                      
                        self.arestasVarredura.append([ y_minimo, y_maximo, x_yminimo, m])

                # exceção para a ultima reta( ult ponto p/ primei)
                if listaParesOrdenados[-1][1] < listaParesOrdenados[0][1]:
                    y_minimo = listaParesOrdenados[-1][1]
                    y_maximo = listaParesOrdenados[0][1]
                    x_yminimo = listaParesOrdenados[-1][0]
                else:
                    y_minimo = listaParesOrdenados[0][1]
                    y_maximo = listaParesOrdenados[-1][1]
                    x_yminimo = listaParesOrdenados[0][0]        
        
                m = (listaParesOrdenados[0][1]-listaParesOrdenados[-1][1]) / (listaParesOrdenados[0][0]-listaParesOrdenados[-1][0])
                m = round(1 / m, 2) 

                self.arestasVarredura.append([ y_minimo, y_maximo, x_yminimo, m])

    
    def printTabelaVarredura(self):
        if len(self.arestasVarredura) > 0:
            print("              y_min  |  y_max  |  x_Ymin  |     M      |   Intersecção")
            for i in range(len(self.arestasVarredura)):
                print("Reta ", i,"|      ", self.arestasVarredura[i][0], "        ",self.arestasVarredura[i][1],"        ", self.arestasVarredura[i][2],"      ", self.arestasVarredura[i][3])
    
    def printTabelaInterseccoes(self):
        if len(self.listaInterseccoes) > 0:
            print("              y_varredura  |  lista Intersecção")
            for i in range(len(self.listaInterseccoes)):
                print("Y_varredura |      ", self.listaInterseccoes[i][0],"        ", self.listaInterseccoes[i][1])
                # print("Reta ", i,"|      ", self.listaInterseccoes[i][0])

    def fazerVarredura(self):
        #pegando a altura maxima e minima de uma aresta
        alturaMinPoligono = self.arestasVarredura[0][0] 
        alturaMAxPoligono = self.arestasVarredura[0][1]
        for i in range(len(self.arestasVarredura)):
            if self.arestasVarredura[i][0] < alturaMinPoligono: 
                alturaMinPoligono = self.arestasVarredura[i][0]

            if self.arestasVarredura[i][1] > alturaMAxPoligono: 
                alturaMAxPoligono = self.arestasVarredura[i][1]
        
        # faz a verredura para todos os Y(entre alturaMAx e alturaMin)
        #e pega os pares de interseção em X
        for Y_varredura in range(alturaMinPoligono, alturaMAxPoligono+1):
            interseccoesX = []
            
            for aresta in range(len(self.arestasVarredura)):
                y_minimo = self.arestasVarredura[aresta][0]
                y_maximo = self.arestasVarredura[aresta][1]
                x_yminimo = self.arestasVarredura[aresta][2]
                m = self.arestasVarredura[aresta][3]
            
                if Y_varredura >= y_minimo and Y_varredura <= y_maximo:
                    x = round(m * (Y_varredura - y_minimo) + x_yminimo)
                    interseccoesX.append( x )              
            
            if len(interseccoesX) == 0:
                interseccoesX = ["não possui"]


            self.listaInterseccoes.append([Y_varredura, interseccoesX])
        
        for i in range(len(self.listaInterseccoes)):
            if len(self.listaInterseccoes[i][1]) > 1:

                print("Y:", self.listaInterseccoes[i][0], "lista:",self.listaInterseccoes[i][1])

                for x in range( 0, len(self.listaInterseccoes[i][1]), 2):
                    if x+1 < len(self.listaInterseccoes[i][1]):
                        self.planoCartesiano.reta(self.listaInterseccoes[i][1][x], self.listaInterseccoes[i][0], self.listaInterseccoes[i][1][x+1], self.listaInterseccoes[i][0],  Icone.COR_ROXO.value)
                        print("x:", self.listaInterseccoes[i][1][x],"y:", self.listaInterseccoes[i][0],"xf:", self.listaInterseccoes[i][1][x+1],"yf:", self.listaInterseccoes[i][0])

        # self.planoCartesiano.matrizAtual()
        self.printTabelaVarredura()
        self.printTabelaInterseccoes()

        return self.planoCartesiano

    def pintarBordas(self, listaParesOrdenados, planoCartesiano):

        if len(listaParesOrdenados) > 1:
            for i in range(0, len(listaParesOrdenados)-1):
                if i < len(listaParesOrdenados):
                    xInicial = listaParesOrdenados[i][0]
                    yInicial = listaParesOrdenados[i][1]
                    xFinal = listaParesOrdenados[i+1][0]
                    yFinal = listaParesOrdenados[i+1][1]
                    planoCartesiano.reta(xInicial, yInicial, xFinal, yFinal)

            xFinal = listaParesOrdenados[-1][0]
            yFinal = listaParesOrdenados[-1][1]
            planoCartesiano.reta(listaParesOrdenados[0][0], listaParesOrdenados[0][1], xFinal, yFinal)
        return planoCartesiano


    def pegarRetas(self):
        tela = Tela()
        listaParesOrdenados = []

        

        while True:
            tela.limparTela()
            self.planoCartesiano.matrizAtual()
            print("\nLista de pares Ordenados:", listaParesOrdenados)

            print("Obsevações: o 1° ponto se conecta com o segundo, o ultimo ponto se conecta com o primeiro")
            print("Recomendação: inserção de retas no sentido anti-horario")
            print("\nAdicionar pares ordenados")
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

    """     OBS:
    0 == COR DO FUNDO
    1 == COR DA BORDA(VERMELHO)
    2 == COR DO PREENCEMENTO(AZUL)
    """

    def preenchimento(self, x, y, corBorda, planoCartesiano):
        # p [x, y, cor]
        pixel = self.lerPixel(x, y, planoCartesiano)
        print("PIXELL",pixel)

        if pixel[2] != corBorda and pixel[2] != 2:
            planoCartesiano = self.pintarPixel(x, y, planoCartesiano)
            self.preenchimento(x+1, y,  corBorda, planoCartesiano)
            self.preenchimento(x, y+1, corBorda, planoCartesiano)
            self.preenchimento(x-1, y, corBorda, planoCartesiano)
            self.preenchimento(x, y-1, corBorda, planoCartesiano)
    
    def lerPixel(self, x, y, planoCartesiano):
        pixel = [None]
        for linha in range(len(planoCartesiano.matriz)):
            for coluna in range(len(planoCartesiano.matriz)):
                #   x , y                    x = indice_1     y = indice_0
                if planoCartesiano.matriz[linha][coluna][1] == x and planoCartesiano.matriz[linha][coluna][0] == y:
                    pixel = planoCartesiano.matriz[linha][coluna]
        
        return pixel
    
    def pintarPixel(self, x, y, planoCartesiano):
        cor = Icone.COR_VERDE.value
       
        for linha in range(len(planoCartesiano.matriz)):
            for coluna in range(len(planoCartesiano.matriz)):
                #   x , y                    x = indice_1     y = indice_0
                if planoCartesiano.matriz[linha][coluna][1] == x and planoCartesiano.matriz[linha][coluna][0] == y:
                    planoCartesiano.matrizDePontos[linha][coluna] = str(cor)+"   X"+str(Icone.FIM_COR.value)
                    planoCartesiano.matriz[linha][coluna][2] = 2
        
        return planoCartesiano
        