from modulos.tela import Tela
from modulos.bresenham import Bresenham

class Recorte:

    def __init__(self, inicioMatriz, fimMatriz):
        self.objeto = Bresenham(inicioMatriz, fimMatriz)
        
    def escreverLinhas(self, listaParesOrdenados: list, linhaOuPoligono):

        if linhaOuPoligono == 1:
            for i in range(0, len(listaParesOrdenados), 2):
                xInicial = listaParesOrdenados[i][0]
                yInicial = listaParesOrdenados[i][1]
                xFinal = listaParesOrdenados[i+1][0]
                yFinal = listaParesOrdenados[i+1][1]
                self.objeto.reta(xInicial, yInicial, xFinal, yFinal)
            
            return self.objeto
        
        elif linhaOuPoligono == 2:
            for i in range(0, len(listaParesOrdenados)-1):
                if i < len(listaParesOrdenados):
                    xInicial = listaParesOrdenados[i][0]
                    yInicial = listaParesOrdenados[i][1]
                    xFinal = listaParesOrdenados[i+1][0]
                    yFinal = listaParesOrdenados[i+1][1]
                    self.objeto.reta(xInicial, yInicial, xFinal, yFinal)
                
            xFinal = listaParesOrdenados[-1][0]
            yFinal = listaParesOrdenados[-1][1]
            self.objeto.reta(listaParesOrdenados[0][0], listaParesOrdenados[0][1], xFinal, yFinal)
    
            return self.objeto


    def pegarPontosLinha(self, listaParesOrdenados: list):
        tela = Tela()
        linhaOuPoligono = 1

        while True:
            tela.limparTela()
            print("Recorde de linha\n")
            self.objeto.matrizAtual()
            print("\nLista de pares Ordenados:", listaParesOrdenados)
            print("Adicionar pares ordenados")
            print("!!!!    para cancelar apenas de um ENTER vazio     !!!!")
            x = input("\nX:")
            if x == "":
                break
            y = input("\nY:")
            if y == "":
                break
            x_f = input("\nX_f:")
            if x_f == "":
                break
            y_f = input("\nY_f:")
            if y_f == "":
                break

            par = [int(x), int(y)]        
            par_f = [int(x_f), int(y_f)]        
            listaParesOrdenados.append(par)
            listaParesOrdenados.append(par_f)

            self.objeto = self.escreverLinhas(listaParesOrdenados, linhaOuPoligono)

        return listaParesOrdenados
    
    def pegarPontosPoligono(self, listaParesOrdenados: list):
        tela = Tela()
        linhaOuPoligono = 2
        while True:
            tela.limparTela()
            print("Recorde de Poligonos\n")
            self.objeto.matrizAtual()
            print("\nLista de pares Ordenados:", listaParesOrdenados)
            print("Adicionar pares ordenados")
            print("!!!!    para cancelar apenas de um ENTER vazio     !!!!")
            x = input("\nX:")
            if x == "":
                break
            y = input("\nY:")
            if y == "":
                break

            par = [int(x), int(y)]        
            listaParesOrdenados.append(par)

            if len(listaParesOrdenados) >= 2:
                self.objeto = self.escreverLinhas(listaParesOrdenados, linhaOuPoligono)

        return listaParesOrdenados