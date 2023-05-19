import os
class Tela():

   def limparTela(self):
      os.system('cls')

   def painelConfigRapida(self):
      self.limparTela()
      print("------------"*4)
      print("              Opções\n")
      print("[10] - Sair")
      print("[7] - -")
      print("[6] - ")
      print("[5] - Recorde de linha e poligonos")
      print("[4] - Transformações(Rotação, Translação, Escala)")
      print("[3] - Circulo")
      print("[2] - Polilinhas")
      print("[1] - Bresenham")
      print("[0] - tamanho do plano cartesiano")
   
   def miniEnquandramento(self, inicioMatriz, fimMatriz):
      print("                            <--------X2  ")
      print("   .    .    .    |    .    .    "+str(fimMatriz)+str(fimMatriz)+"  |")
      print("   .    .    .    |    .    .    .   |")
      print("   .    .    .    |    .    .    .   |")
      print("^  -------------- 0 --------------   v")
      print("|  .    .    .    |    .    .    .")
      print("|  .    .    .    |    .    .    .")
      print("|  "+str(inicioMatriz)+str(inicioMatriz)+" .    .    |    .    .    .")
      print("X1------->  ")