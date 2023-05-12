import random
from modulos.bresenham import Bresenham
from modulos.tela import Tela
import time

tela = Tela()

inicioMatriz = -4
fimMatriz = 4
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
        tela.painelConfigRapida()
        
        quantidateEntregas = int(input("\nQuantidade de entregas:"))
    elif opc == 3:
        tela.painelConfigRapida()
        
        listaPedidos = []
        novoPontoPartida = int(input("\nPizzaria:"))
        if not(novoPontoPartida in listaPedidos):
            enderecoPizzaHut = novoPontoPartida

    elif opc == 2:
        teste = Bresenham(inicioMatriz,fimMatriz)
        listaParesOrdenados = []

        adicionarReta = 0
        while adicionarReta != 999:
            tela.painelConfigRapida()
            print("\nLista de pares Ordenados:", listaParesOrdenados)
            print("Serão traçadas retas de ponto a ponto considerando a lista acima")
            x = int(input("\nX:"))
            y = int(input("\nY:"))
            par = [x, y]        
            listaParesOrdenados.append(par)
            
            if len(listaParesOrdenados) > 3:
                tela.painelConfigRapida()
                print("\nLista de pares Ordenados:", listaParesOrdenados)
                print("[1]adicionar nova Reta         [2]Sair")
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
        teste.matrizAtual()
        sair = input("aperte enter para sair.")

    elif opc == 1:
        tela.painelConfigRapida()
        adicionarReta = 0
        listaParesOrdenados = []
        while adicionarReta != 999:
            tela.painelConfigRapida()
            if len(listaParesOrdenados) > 0:
                for i in range(0, len(listaParesOrdenados), 2):
                    xInicial = listaParesOrdenados[i][0]
                    yInicial = listaParesOrdenados[i][1]
                    xFinal = listaParesOrdenados[i+1][0]
                    yFinal = listaParesOrdenados[i+1][1]
                    teste.reta(xInicial, yInicial, xFinal, yFinal)
                teste.matrizAtual()
            print("\nLista de pares Ordenados:", listaParesOrdenados)
            print("[1]adicionar nova Reta         [2]Sair")
            adicionarReta = int(input("opção:"))
            if adicionarReta == 2:
                adicionarReta = 999
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
        print(".    .    |    .    "+str(fimMatriz)+str(fimMatriz))
        print(".    .    |    .    .")
        print("--------- 0 ---------")
        print(".    .    |    .    .")
        print(str(inicioMatriz)+str(inicioMatriz)+" .    |    .    .")
        print("\nRecomendado:")
        print("X menor que X2")
        inicioMatriz = int(input("\nX:"))
        fimMatriz = int(input("\nX2:"))
        teste = Bresenham(inicioMatriz,fimMatriz)
        opc = 1

tela.limparTela()
print("       Obrigado por usar nosso simulador <3\n\n\n\n\n\n")
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