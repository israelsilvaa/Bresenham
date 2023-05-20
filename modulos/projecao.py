# import random
from modulos.bresenham import Bresenham
from modulos.tela import Tela

class Projecao:

    def __init__(self, inicioMatriz, fimMatriz):
        print("teste proje")
        self.tela = Tela()

    def pegarSolido3d(self):
     
        listaParesOrdenados = []

        while True:
            self.tela.limparTela()
            print("\nLista de pares Ordenados:", listaParesOrdenados)
            print("Adicionar pares ordenados")
            print("!!!!    para cancelar apenas de ENTER no X e Y     !!!!")
            x = input("\nX:")
            y = input("\nY:")
            z = input("\nZ:")
            if x == "" or y == "" or z == "":
                break
            par = [int(x), int(y), int(z)]        
            listaParesOrdenados.append(par)

           
        return listaParesOrdenados