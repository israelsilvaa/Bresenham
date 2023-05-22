from modulos.bresenham import Bresenham
from modulos.tela import Tela

class VarreduraPreenchimento:

    def __init__(self,inicioMatriz, fimMatriz):
        self.planoCartesiano = Bresenham(inicioMatriz, fimMatriz)
        self.inicioMatriz = inicioMatriz
        self.fimMatriz = fimMatriz
        self.listaDeRetas = []
    
    def tabelaVarredura(self):
        print("Lista de retas do poligono acima:\n", self.listaDeRetas, "\n")
                
        print("          Min_x  |  Max_y  |  Min_X  |  Max_Y | Delta_Y | Delta_X | M ")
        for i in range(len(self.listaDeRetas)):
            print("Reta ", i,"     ", self.listaDeRetas[i][0], "      ",self.listaDeRetas[i][1],"      ", self.listaDeRetas[i][2],"      ", self.listaDeRetas[i][3],"      ", self.listaDeRetas[i][4],"      ", self.listaDeRetas[i][5],"      ", self.listaDeRetas[i][6])
            # print[self.listaDeRetas[i][0], self.listaDeRetas[i][1], self.listaDeRetas[i][2], self.listaDeRetas[i][3]]

    
    def pegarRetas(self):
        tela = Tela()
        listaParesOrdenados = []

        while True:
            tela.limparTela()
            self.planoCartesiano.matrizAtual()
            print("\nLista de pares Ordenados:", listaParesOrdenados)
            print("Adicionar pares ordenados")
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

                        reta = [xInicial, xFinal, yInicial, yFinal, 0, 0, 0]
                        self.listaDeRetas.append(reta)

                xFinal = listaParesOrdenados[-1][0]
                yFinal = listaParesOrdenados[-1][1]
                self.planoCartesiano.reta(listaParesOrdenados[0][0], listaParesOrdenados[0][1], xFinal, yFinal)

        return listaParesOrdenados


    """     OBS:
    
    0 == COR DO FUNDO
    1 == COR DA BORDA(VERMELHO)
    2 == COR DO PREENCEMENTO(AZUL)
    """