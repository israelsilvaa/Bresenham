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
      print("[6] - -")
      print("[5] - -")
      print("[4] - Transformações(Rotação, Translação, Escala)")
      print("[3] - Circulo")
      print("[2] - Polilinhas")
      print("[1] - Bresenham")
      print("[0] - tamanho do plano cartesiano")
   