# import random
from modulos.bresenham import Bresenham
from modulos.circulo import Circulo
from modulos.recorte import Recorte
from modulos.transformacoes import Transformacoes
from modulos.tela import Tela
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
        
        while True:
            adicionarReta = 0
            tela.limparTela()
            teste = Bresenham(inicioMatriz,fimMatriz)
            listaParesOrdenados = []

            print("Recorde de linha e poligonos\n")
            teste.matrizAtual()

            print("\nLista de pares Ordenados:", listaParesOrdenados)
            print("[1]linha - [2]Poligono - [3]Sair")
            adicionarReta = int(input("opção:"))
            
            if adicionarReta == 1:
                while True:
                    tela.limparTela()
                    recorte = Recorte(inicioMatriz, fimMatriz)
                    print("Recorde de linha\n")
                    # pegar linhas
                    listaParesOrdenados = recorte.pegarPontosLinha(listaParesOrdenados)
                    break

                while True:
                    tela.limparTela()
                    teste = recorte.escreverLinhas(listaParesOrdenados, 1)

                    teste.matrizAtual()
                    print("\nLista de pares Ordenados:", listaParesOrdenados)
                    tela.miniEnquandramento(inicioMatriz,fimMatriz)
                    print("\n[1]Novo enquadramento         [2]Sair")
                    tamanhoMatriz = int(input("opção:"))
                    if tamanhoMatriz == 1:
                        inicioMatriz = int(input("\nX1(negativo):"))
                        fimMatriz = int(input("\nX2(positivo):"))
                        recorte = Recorte(inicioMatriz, fimMatriz)
                    elif tamanhoMatriz == 2:
                        adicionarReta = 0
                        break

            elif adicionarReta == 2:
                while True:
                    tela.limparTela()
                    recorte = Recorte(inicioMatriz, fimMatriz)
                    print("Recorde de Poligonos\n")
                    # pegar linhas                  
                    listaParesOrdenados = recorte.pegarPontosPoligono(listaParesOrdenados)
                    teste = recorte.objeto
                    break

                while True:
                    tela.limparTela()
                    teste = recorte.escreverLinhas(listaParesOrdenados, 2)

                    teste.matrizAtual()
                    print("\nLista de pares Ordenados:", listaParesOrdenados)
                    tela.miniEnquandramento(inicioMatriz,fimMatriz)
                    print("\n[1]Novo enquadramento         [2]Sair")
                    tamanhoMatriz = int(input("opção:"))
                    if tamanhoMatriz == 1:
                        inicioMatriz = int(input("\nX1(negativo):"))
                        fimMatriz = int(input("\nX2(positivo):"))
                        recorte = Recorte(inicioMatriz, fimMatriz)
                        teste = recorte.escreverLinhas(listaParesOrdenados, 2)
                    elif tamanhoMatriz == 2:
                        adicionarReta = 0
                        break            
                    else:
                        break
            else:
                break
       
    elif opc == 4:
        teste = Bresenham(inicioMatriz,fimMatriz)
        tela.painelConfigRapida()
        listaParesOrdenados = []

        while True:
            tela.painelConfigRapida()
            tela.limparTela()
            teste.matrizAtual()
            print("\nLista de pares Ordenados:", listaParesOrdenados)
            print("[1]adicionar nova Reta - [2]translação - [3]Rotação - [4]Escala - [5]Sair")
            adicionarReta = int(input("opção:"))

            if adicionarReta == 1:
                transfor = Transformacoes(inicioMatriz, fimMatriz)
                listaParesOrdenados = transfor.pegarPontos()
                teste = transfor.planoCartesiano
    
            elif adicionarReta == 2:
                print("translação")
                eixoX = int(input("translação em X:"))
                eixoY = int(input("translação em y:"))
                transfor = Transformacoes(inicioMatriz, fimMatriz)
                teste = transfor.fazerTranslacao(listaParesOrdenados, eixoX, eixoY)
                
            elif adicionarReta == 3:
                indicePivo = int(input("Selecione o Pivo na lista de Pontos acima(atraves de seu indice na lista):"))
                angulo = int(input("Angulo:"))
                transfor = Transformacoes(inicioMatriz, fimMatriz)
                teste = transfor.fazerRotacao(angulo, indicePivo, listaParesOrdenados)
                listaParesOrdenados = transfor.listaParesOrdenados

            elif adicionarReta == 4:
                print("Escala")
                Ex = float(input("fator de escala para X:"))
                Ey = float(input("fator de escala para Y:"))
                pontoFixo = int(input("Ponto fixo(indice na lista de pontos):"))
                transfor = Transformacoes(inicioMatriz, fimMatriz)
                teste = transfor.atualizarEscala(listaParesOrdenados, Ex, Ey, pontoFixo)

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
                listaParesOrdenados.pop(-1)
                teste = Bresenham(inicioMatriz,fimMatriz)

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
