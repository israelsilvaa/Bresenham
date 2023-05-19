# import random
from modulos.bresenham import Bresenham
from modulos.tela import Tela
from enums.icone import Icone
from modulos.rotacao import Rotacao
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
        tela.limparTela()
        teste = Bresenham(inicioMatriz,fimMatriz)
        listaParesOrdenados = []

        print("Recorde de linha e poligonos\n")
        teste.matrizAtual()

        print("\nLista de pares Ordenados:", listaParesOrdenados)
        print("[1]linha - [2]Poligono - [3]Sair")
        adicionarReta = int(input("opção:"))
        while True:
            if adicionarReta == 1:
                while True:
                    tela.limparTela()
                    print("Recorde de linha\n")
                    teste.matrizAtual()
                    print("\nLista de pares Ordenados:", listaParesOrdenados)
                    print("Adicionar pares ordenados")
                    print("!!!!    para cancelar apenas de ENTER no X e Y     !!!!")
                    x = input("\nX:")
                    y = input("\nY:")
                    if x == "" or y == "":
                        break
                    par = [int(x), int(y)]        
                    listaParesOrdenados.append(par)

                    if len(listaParesOrdenados) % 2 == 0:
                        for i in range(0, len(listaParesOrdenados), 2):
                            xInicial = listaParesOrdenados[i][0]
                            yInicial = listaParesOrdenados[i][1]
                            xFinal = listaParesOrdenados[i+1][0]
                            yFinal = listaParesOrdenados[i+1][1]
                            teste.reta(xInicial, yInicial, xFinal, yFinal)
                        teste.matrizAtual()

                tela.limparTela()
                print("Recorde de linha\n")
                teste.matrizAtual()
                print("\nLista de pares Ordenados:", listaParesOrdenados)
                while True:
                    tela.limparTela()
                    teste.matrizAtual()
                    print("-enquadramento atual: X1:", inicioMatriz, "  X2:", fimMatriz)
                    tela.miniEnquandramento(inicioMatriz,fimMatriz)
                    print("[1]Novo enquadramento         [2]Sair")
                    tamanhoMatriz = int(input("opção:"))
                    if tamanhoMatriz == 1:
                        inicioMatriz = int(input("\nX1(negativo):"))
                        fimMatriz = int(input("\nX2(positivo):"))
                    elif tamanhoMatriz == 2:
                        break

            elif adicionarReta == 2:
                print("Recorde de poligono\n")
            
            else:
                break
       
    elif opc == 4:
        teste = Bresenham(inicioMatriz,fimMatriz)
        tela.painelConfigRapida()
        adicionarReta = 0
        listaParesOrdenados = []
        while True:
            tela.painelConfigRapida()
            tela.limparTela()
            teste.matrizAtual()

            print("\nLista de pares Ordenados:", listaParesOrdenados)
            print("[1]adicionar nova Reta - [2]translação - [3]Rotação - [4]Escala - [5]Sair")
            adicionarReta = int(input("opção:"))
            if adicionarReta == 1:
                while True:
                    tela.limparTela()
                    teste.matrizAtual()
                    print("\nLista de pares Ordenados:", listaParesOrdenados)
                    print("Adicionar pares ordenados")
                    print("!!!!    para cancelar apenas de ENTER no X e Y     !!!!")
                    x = input("\nX:")
                    y = input("\nY:")
                    if x == "" or y == "":
                        break
                    par = [int(x), int(y)]        
                    listaParesOrdenados.append(par)
            
            elif adicionarReta == 2:
                print("translação")
                eixoX = int(input("translação em X:"))
                eixoY = int(input("translação em y:"))
                for i in range(len(listaParesOrdenados)):
                    listaParesOrdenados[i][0] = listaParesOrdenados[i][0] + eixoX 
                    listaParesOrdenados[i][1] = listaParesOrdenados[i][1] + eixoY 
                teste = Bresenham(inicioMatriz,fimMatriz)
                
            elif adicionarReta == 3:
                objRotacao = Rotacao(listaParesOrdenados)
                angulo = int(input("Angulo:"))
                indicePivo = int(input("Selecione o Pivo na lista de Pontos acima(atraves de seu indice na lista):"))
                angulo = objRotacao.getSenCos(angulo)
                objRotacao.criarMatrizAnguloPonto(listaParesOrdenados, indicePivo)
                
                teste = Bresenham(inicioMatriz,fimMatriz)
                
                objRotacao.printMatrizAnguloPonto()
                objRotacao.multiplicarMatrizes()
                
                listaParesOrdenados = objRotacao.pegarPontosMultiplicados()
                
                sair = input("pausa depois de informar angulo(enter para continuar)")

            elif adicionarReta == 4:
                print("Escala")
                Ex = float(input("fator de escala para X:"))
                Ey = float(input("fator de escala para Y:"))
                for i in range(len(listaParesOrdenados)):
                    listaParesOrdenados[i][0] = int(listaParesOrdenados[i][0] * Ex) 
                    listaParesOrdenados[i][1] = int(listaParesOrdenados[i][1] * Ey)
                teste = Bresenham(inicioMatriz,fimMatriz)
                sair = input("(enter para continuar)")
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

        while True:
            tela.limparTela()
            tela.painelConfigRapida()
            teste.matrizAtual()
            print("\nLista de pares Ordenados:", listaParesOrdenados)
            print("Serão traçadas retas de ponto a ponto considerando a lista acima")
            x = int(input("\nX:"))
            y = int(input("\nY:"))
            par = [x, y]        
            listaParesOrdenados.append(par)

            teste = Bresenham(inicioMatriz,fimMatriz)
            if len(listaParesOrdenados) > 1:
                for i in range(len(listaParesOrdenados)):
                    if i < len(listaParesOrdenados)-1:
                        xInicial = listaParesOrdenados[i][0]
                        yInicial = listaParesOrdenados[i][1]
                        xFinal = listaParesOrdenados[i+1][0]
                        yFinal = listaParesOrdenados[i+1][1]
                        teste.reta(xInicial, yInicial, xFinal, yFinal)
                # teste.reta(listaParesOrdenados[-1][0], listaParesOrdenados[-1][1], listaParesOrdenados[0][0], listaParesOrdenados[0][1])
                
                tela.painelConfigRapida()
                teste.matrizAtual()
                print("\nLista de pares Ordenados:", listaParesOrdenados)
                print("[1]adicionar novo Ponto         [2]Sair")
                adicionarReta = int(input("opção:"))
            
                if adicionarReta == 2:
                    break
            
    elif opc == 1:
        teste = Bresenham(inicioMatriz,fimMatriz)
        tela.painelConfigRapida()
        adicionarReta = 0
        listaParesOrdenados = []
        while True:
            tela.painelConfigRapida()
            if len(listaParesOrdenados) > 1:
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
            print("[1]adicionar nova Reta      [2]Sair    [3]remover")
            adicionarReta = int(input("opção:"))
            if adicionarReta == 3:
                listaParesOrdenados.pop(-1)
            elif adicionarReta == 2:
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
        while True:
            tela.limparTela()
            teste = Bresenham(inicioMatriz,fimMatriz)
            teste.matrizAtual()
            print("-enquadramento atual: X1:", inicioMatriz, "  X2:", fimMatriz)
            tela.miniEnquandramento(inicioMatriz,fimMatriz)
            print("[1]Novo enquadramento         [2]Sair")
            tamanhoMatriz = int(input("opção:"))
            if tamanhoMatriz == 1:
                inicioMatriz = int(input("\nX1(negativo):"))
                fimMatriz = int(input("\nX2(positivo):"))
            elif tamanhoMatriz == 2:
                break
        opc = 1
    
           
tela.limparTela()
print("       Obrigado por usar nosso paint <3\n\n\n\n\n\n")
time.sleep(3)

# teste.tabelaVarredura()
# teste.matrizCoordenada()
