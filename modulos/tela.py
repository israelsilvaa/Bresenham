import os
from enums.icone import Icone
class Tela():

   def limparTela(self):
      os.system('cls')

   def painelConfigRapida(self):
      self.limparTela()
      print("------------"*4)
      print("              Opções\n")
      print("[10] - Tamanho do plano cartesiano")
      print(str(Icone.COR_VERDE.value)+"[9] - Sobre"+str(Icone.FIM_COR.value))
      print(str(Icone.COR_VERMELHO.value)+"[8] - Curva de Bézier"+str(Icone.FIM_COR.value))
      print(str(Icone.COR_VERDE.value)+"[7] - Projeções(Ortografica, Persquectiva)"+str(Icone.FIM_COR.value))
      print(str(Icone.COR_VERDE.value)+"[6] - Preenchimento("+str(Icone.FIM_COR.value)+str(Icone.COR_AMARELO.value)+"varredura"+str(Icone.FIM_COR.value)+str(Icone.COR_VERDE.value)+", recursivo)"+str(Icone.FIM_COR.value))
      print(str(Icone.COR_VERDE.value)+"[5] - Recorde de linha e poligonos"+str(Icone.FIM_COR.value))
      print(str(Icone.COR_VERDE.value)+"[4] - Transformações("+str(Icone.FIM_COR.value)+str(Icone.COR_AMARELO.value)+"Rotação"+str(Icone.FIM_COR.value)+str(Icone.COR_VERDE.value)+", Translação, Escala)"+str(Icone.FIM_COR.value))
      print(str(Icone.COR_VERDE.value)+"[3] - Circulo"+str(Icone.FIM_COR.value))
      print(str(Icone.COR_VERDE.value)+"[2] - Polilinhas"+str(Icone.FIM_COR.value))
      print(str(Icone.COR_VERDE.value)+"[1] - Bresenham"+str(Icone.FIM_COR.value))
      print("[0] - Sair")
   
   def miniEnquandramento(self, inicioMatriz, fimMatriz):
      print("-enquadramento atual: X1:", inicioMatriz, "  X2:", fimMatriz)
      print("\n                            <--------X2  ")
      print("   .    .    .    |    .    .    "+str(fimMatriz)+str(fimMatriz)+"  |")
      print("   .    .    .    |    .    .    .   |")
      print("   .    .    .    |    .    .    .   |")
      print("^  -------------- 0 --------------   v")
      print("|  .    .    .    |    .    .    .")
      print("|  .    .    .    |    .    .    .")
      print("|  "+str(inicioMatriz)+str(inicioMatriz)+" .    .    |    .    .    .")
      print("X1------->  ")

   def sobre(self):
        self.limparTela()
        print(Icone.COR_VERDE.value,"             SISTEMAS DE INFORMAÇÃO\n\n", Icone.FIM_COR.value)
        print(Icone.COR_AMARELO.value,"Disciplina: ",Icone.FIM_COR.value ,"Computação Grafica")
        print(Icone.COR_AMARELO.value,"Docente:",Icone.FIM_COR.value ,"Prof. Dr. Bianchi Serique Meiguins")
        print(Icone.COR_AMARELO.value,"Discentes:",Icone.FIM_COR.value ," Israel Pinheiro da Silva")
        print("              Weslei Marcelo Amorin Dos Santos")
  
        print(Icone.COR_VERDE.value,"\n\n\n                Pressione ENTER para sair. '-'", Icone.FIM_COR.value)
        s = input()