from modulos.tela import Tela

class Recorte:

    def __init__(self, objeto):
        self.objeto = objeto
        
    def escreverLinhas(self, listaParesOrdenados: list):

        for i in range(0, len(listaParesOrdenados), 2):
            xInicial = listaParesOrdenados[i][0]
            yInicial = listaParesOrdenados[i][1]
            xFinal = listaParesOrdenados[i+1][0]
            yFinal = listaParesOrdenados[i+1][1]
            self.objeto.reta(xInicial, yInicial, xFinal, yFinal)
        
        return self.objeto

    def pegarPontos(self, listaParesOrdenados: list):
        tela = Tela()
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
            self.objeto = self.escreverLinhas(listaParesOrdenados)
            
        
        return listaParesOrdenados