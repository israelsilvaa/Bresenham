import random
from modulos.bresenham import Bresenham
from modulos.tela import Tela
from modulos.circulo import Circulo
import time

tela = Tela()

inicioMatriz = -7
fimMatriz = 7
teste = Bresenham(inicioMatriz,fimMatriz)

tela.limparTela()

listaParesOrdenados = []

opc = 1
tela.limparTela()
while opc != 10:
    
    # perguntar qual a proxima opc, 
    if opc != 0:
        tela.painelConfigRapida()
        opc = int(input("\nOpção:"))

    if opc == 7:
        tela.sobre()
        sair = str(input())

    elif opc == 6:
        NovoPedido = 99
        while NovoPedido != -1:
            tela.painelConfigRapida()
            
            print("\n[-1]cancelar   [-2]Remover ultimo:")

            NovoPedido = int(input("\nAdicionar pedido:"))

            # if NovoPedido >= 0 and not(NovoPedido in listaPedidos) and NovoPedido != enderecoPizzaHut and NovoPedido <= tamanhoGrid * tamanhoGrid - 1:
            #     listaPedidos.append(NovoPedido)
            #     quantidateEntregas = len(listaPedidos)
            # elif NovoPedido == -2 and len(listaPedidos) >= 1:
            #     listaPedidos.pop()
            #     quantidateEntregas = len(listaPedidos)
            #     if quantidateEntregas == 0:
            #         quantidateEntregas = 1

    elif opc == 5:
        tela.painelConfigRapida()
       
        velociadeAtualizacao = float(input("\nVelocidade da simulação:"))
    elif opc == 4:
        teste = Bresenham(inicioMatriz,fimMatriz)
        tela.painelConfigRapida()
        adicionarReta = 0
        listaParesOrdenados = []
        while True:
            tela.painelConfigRapida()
            if len(listaParesOrdenados) > 0:
                for i in range(0, len(listaParesOrdenados), 2):
                    xInicial = listaParesOrdenados[i][0]
                    yInicial = listaParesOrdenados[i][1]
                    xFinal = listaParesOrdenados[i+1][0]
                    yFinal = listaParesOrdenados[i+1][1]
                    teste.reta(xInicial, yInicial, xFinal, yFinal)
                teste.matrizAtual()
            tela.limparTela()
            teste.matrizAtual()
            print("\nLista de pares Ordenados:", listaParesOrdenados)
            print("[1]adicionar nova Reta - [2]translação - [3]Rotação - [4]Escala - [5]Sair")
            adicionarReta = int(input("opção:"))
            if adicionarReta == 1:
                x = int(input("\nX Inicial:"))
                y = int(input("\nY Inicial:"))
                x_f = int(input("\nX Final:"))
                y_f = int(input("\nY Final:"))
                parInicial = [x, y]        
                parFinal = [x_f, y_f]        
                listaParesOrdenados.append(parInicial)
                listaParesOrdenados.append(parFinal)
            elif adicionarReta == 2:
                print("translação")
                eixoX = int(input("translação em X:"))
                eixoY = int(input("translação em y:"))
                for i in range(len(listaParesOrdenados)):
                    listaParesOrdenados[i][0] = listaParesOrdenados[i][0] + eixoX 
                    listaParesOrdenados[i][1] = listaParesOrdenados[i][1] + eixoY 
                teste = Bresenham(inicioMatriz,fimMatriz)
                
            elif adicionarReta == 3:
                print("rotação")
                senAng = 0
                cosAng = 0
                angulo = int(input("Angulo:"))

                if angulo == 30:
                    senAng = 0.50 
                    cosAng = 0.87
                elif angulo == -30:
                    senAng = -0.50
                    cosAng = 0.87

                elif angulo == 45:
                    senAng = 0.70
                    cosAng = 0.70
                elif angulo == -45:
                    senAng = -0.70
                    cosAng = 0.70

                elif angulo == 60:
                    senAng = 0.87
                    cosAng = 0.50
                elif angulo == -60:
                    senAng = -0.87
                    cosAng = 0.50
                    
                listaParesOrdenados[1][0] = int(listaParesOrdenados[1][0]*cosAng - listaParesOrdenados[1][1]*senAng)
                # listaParesOrdenados[i][1] = round(listaParesOrdenados[i][0]*senAng + listaParesOrdenados[i][1]*cosAng)
                teste = Bresenham(inicioMatriz,fimMatriz)

                #x´= x.cos ‐ y.sen
                #y´= x.sen + y.cos

                print("Angulo:",angulo ,"    Sen:", senAng, "Cos:", cosAng)
                sair = input("sdsdsdsds")





            elif adicionarReta == 4:
                print("Escala")
                Ex = float(input("fator de escala para X:"))
                Ey = float(input("fator de escala para Y:"))
                for i in range(len(listaParesOrdenados)):
                    listaParesOrdenados[i][0] = int(listaParesOrdenados[i][0] * Ex) 
                    listaParesOrdenados[i][1] = int(listaParesOrdenados[i][1] * Ey)
                teste = Bresenham(inicioMatriz,fimMatriz)
                sair = input("saiindo")
            else:
                break

    elif opc == 3:
        tela.limparTela()
        teste = Bresenham(inicioMatriz,fimMatriz)
        tela.painelConfigRapida()

        teste.matrizAtual()
        
        xc = int(input("\nXc inicial:"))
        yc = int(input("\nYc inicial:"))
        raio = int(input("\nRaio(R>1):"))
        
        circulo = Circulo(xc, yc, raio, teste)
        circulo.calcPontosCirculo()
        circulo.desenhaCirculo()
        
        tela.limparTela()
        teste.matrizAtual()
        sair = input("aperte enter para sair.")

    elif opc == 2:
        teste = Bresenham(inicioMatriz,fimMatriz)
        listaParesOrdenados = []

        adicionarReta = 0
        while adicionarReta != 999:
            tela.limparTela()
            tela.painelConfigRapida()
            teste.matrizAtual()
            print("\nLista de pares Ordenados:", listaParesOrdenados)
            print("Serão traçadas retas de ponto a ponto considerando a lista acima")
            x = int(input("\nX:"))
            y = int(input("\nY:"))
            par = [x, y]        
            listaParesOrdenados.append(par)
            
            if len(listaParesOrdenados) > 3:
                tela.painelConfigRapida()
                teste.matrizAtual()
                print("\nLista de pares Ordenados:", listaParesOrdenados)
                print("[1]adicionar nova Reta         [2]Sair e plotar grafico")
                adicionarReta = int(input("opção:"))
            
                if adicionarReta == 2:
                    break
            

        for i in range(len(listaParesOrdenados)):
            if i < len(listaParesOrdenados)-1:
                xInicial = listaParesOrdenados[i][0]
                yInicial = listaParesOrdenados[i][1]
                xFinal = listaParesOrdenados[i+1][0]
                yFinal = listaParesOrdenados[i+1][1]
                teste.reta(xInicial, yInicial, xFinal, yFinal)
        teste.reta(listaParesOrdenados[-1][0], listaParesOrdenados[-1][1], listaParesOrdenados[0][0], listaParesOrdenados[0][1])
        tela.limparTela()
        teste.matrizAtual()
        sair = input("aperte enter para sair.")

    elif opc == 1:
        teste = Bresenham(inicioMatriz,fimMatriz)
        tela.painelConfigRapida()
        adicionarReta = 0
        listaParesOrdenados = []
        while True:
            tela.painelConfigRapida()
            if len(listaParesOrdenados) > 0:
                for i in range(0, len(listaParesOrdenados), 2):
                    xInicial = listaParesOrdenados[i][0]
                    yInicial = listaParesOrdenados[i][1]
                    xFinal = listaParesOrdenados[i+1][0]
                    yFinal = listaParesOrdenados[i+1][1]
                    teste.reta(xInicial, yInicial, xFinal, yFinal)
                teste.matrizAtual()
            tela.limparTela()
            teste.matrizAtual()
            print("\nLista de pares Ordenados:", listaParesOrdenados)
            print("[1]adicionar nova Reta         [2]Sair")
            adicionarReta = int(input("opção:"))
            if adicionarReta == 2:
                break
            else:
                x = int(input("\nX Inicial:"))
                y = int(input("\nY Inicial:"))
                x_f = int(input("\nX Final:"))
                y_f = int(input("\nY Final:"))
                parInicial = [x, y]        
                parFinal = [x_f, y_f]        
                listaParesOrdenados.append(parInicial)
                listaParesOrdenados.append(parFinal)

    elif opc == 0:       
        tamanhoMatriz = 0
        while True:
            tela.limparTela()
            teste = Bresenham(inicioMatriz,fimMatriz)
            teste.matrizAtual()
            print("[1]Novo enquadramento         [2]Sair")
            tamanhoMatriz = int(input("opção:"))
            if tamanhoMatriz == 1:
                inicioMatriz = int(input("\nX(negativo):"))
                fimMatriz = int(input("\nX2(positivo):"))
            elif tamanhoMatriz == 2:
                break
        opc = 1
    
           
tela.limparTela()
print("       Obrigado por usar nosso paint <3\n\n\n\n\n\n")
time.sleep(3)

# teste.tabelaVarredura()
# teste.matrizCoordenada()

"""
passo 1: 
    PIVÔ, levar pra horigem

passo2:
    (rotação de -30°)
    Xlinha: x.coss_Ang - y.sen_Ang
    Xlinha: x.sen_Ang + y.coss_Ang

passo3:
    x': sx.x
    x': 2.2,87 =5,74
    y: 1.2,98= 2,98

passo4:
    x': x +Tx = 5,74 - 1 = 4,74
"""