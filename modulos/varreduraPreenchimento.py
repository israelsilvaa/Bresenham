from modulos.bresenham import Bresenham
from modulos.tela import Tela

class VarreduraPreenchimento:

    def __init__(self,inicioMatriz, fimMatriz):
        self.planoCartesiano = Bresenham(inicioMatriz, fimMatriz)
        self.inicioMatriz = inicioMatriz
        self.fimMatriz = fimMatriz
        self.arestasVarredura = []
    
    def tabelaVarredura(self, listaParesOrdenados):  
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
                            
                        m = (listaParesOrdenados[i+1][1]-listaParesOrdenados[i][1]) / (listaParesOrdenados[i+1][0]-listaParesOrdenados[i][0])
                        self.arestasVarredura.append([ y_minimo, y_maximo, x_yminimo, round(1/m, 2)])

                if listaParesOrdenados[-1][1] < listaParesOrdenados[0][1]:
                    y_minimo = listaParesOrdenados[-1][1]
                    y_maximo = listaParesOrdenados[0][1]
                    x_yminimo = listaParesOrdenados[-1][0]
                else:
                    y_minimo = listaParesOrdenados[0][1]
                    y_maximo = listaParesOrdenados[-1][1]
                    x_yminimo = listaParesOrdenados[0][0]

                m = (listaParesOrdenados[0][1]-listaParesOrdenados[-1][1]) / (listaParesOrdenados[0][0]-listaParesOrdenados[-1][0])

                self.arestasVarredura.append([ y_minimo, y_maximo, x_yminimo, round(1/m, 2)])

        print("              y_min  |  y_max  |  x_Ymin  |     M ")
        for i in range(len(self.arestasVarredura)):
            print("Reta ", i,"|      ", self.arestasVarredura[i][0], "        ",self.arestasVarredura[i][1],"        ", self.arestasVarredura[i][2],"      ", self.arestasVarredura[i][3])
    
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