from modulos.bresenham import Bresenham
from modulos.tela import Tela

class Recorte:

    def __init__(self, inicioMatriz, fimMatriz):
        self.inicioMatriz = inicioMatriz
        self.fimMatriz = fimMatriz
        self.planoCartesiano = Bresenham(inicioMatriz, fimMatriz)

        self.tela = Tela()
        
    def escreverLinhas(self, listaParesOrdenados: list):
        self.planoCartesiano = Bresenham(self.inicioMatriz, self.fimMatriz)

        for i in range(len(listaParesOrdenados)):
            xInicial = listaParesOrdenados[i][0]
            yInicial = listaParesOrdenados[i][1]
            xFinal = listaParesOrdenados[i][2]
            yFinal = listaParesOrdenados[i][3]
            self.planoCartesiano.reta(xInicial, yInicial, xFinal, yFinal)
            
        return self.planoCartesiano
        
    def pegarRetas(self, listaParesOrdenados: list):
        while True:
            self.tela.limparTela()
            print("Recorde de Poligonos\n")
            self.planoCartesiano.matrizAtual()
            print("\nLista de pares Ordenados:", listaParesOrdenados)
            print("Adicionar pares ordenados")
            print("!!!!    para cancelar apenas de um ENTER vazio     !!!!")
            x = (input("\nX Inicial:"))
            y = (input("\nY Inicial:"))
            x_f = (input("\nX Final:"))
            y_f = (input("\nY Final:"))
            if y == "" or x == "" or x_f == "" or y_f == "":
                break      
            reta = [int(x), int(y) ,int(x_f), int(y_f)]        
            listaParesOrdenados.append(reta)

            self.planoCartesiano = self.escreverLinhas(listaParesOrdenados)

        return listaParesOrdenados