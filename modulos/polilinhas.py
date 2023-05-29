from modulos.bresenham import Bresenham
from modulos.tela import Tela
from enums.icone import Icone

class Polilinhas:

    def __init__(self, inicioMatriz, fimMatriz):
        self.tela = Tela()
        self.inicioMatriz = inicioMatriz
        self.fimMatriz = fimMatriz
        self.planoCartesiano = Bresenham(self.inicioMatriz, self.fimMatriz)
        self.listaParesOrdenados = []

    def execute(self):
        while True:
            self.tela.limparTela()
            print("Polilinhas\n")
            
            self.planoCartesiano.matrizAtual()
            print("\nLista de pares Ordenados:", self.listaParesOrdenados)
            print("Serão traçadas retas de ponto a ponto considerando a lista acima")
            print("!!   de enter vazio para cancelar   !!")
            
            x = input("\nX:")
            y = input("\nY:")
            if x == "" or y == "":
                break

            par = [int(x), int(y)]       
            self.listaParesOrdenados.append(par)

            if len(self.listaParesOrdenados) > 1:
                for i in range(len(self.listaParesOrdenados)):
                    if i < len(self.listaParesOrdenados)-1:
                        xInicial = self.listaParesOrdenados[i][0]
                        yInicial = self.listaParesOrdenados[i][1]
                        xFinal = self.listaParesOrdenados[i+1][0]
                        yFinal = self.listaParesOrdenados[i+1][1]

                        self.planoCartesiano.reta(xInicial, yInicial, xFinal, yFinal)
              