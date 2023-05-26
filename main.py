# import random
from modulos.transformacoes import Transformacoes
from modulos.bresenham import Bresenham
from modulos.circulo import Circulo
from modulos.projecao import Projecao
from modulos.varreduraPreenchimento import VarreduraPreenchimento
from modulos.recorte import Recorte
from modulos.tela import Tela
import time

inicioMatriz = -10
fimMatriz = 10

planoCartesiano = Bresenham(inicioMatriz,fimMatriz)
tela = Tela()

listaParesOrdenados = []

opc = 1
while opc != 0:
    
    # perguntar qual a proxima opc sempre que o laço é (RE)iniciado, 
    if opc != 0:
        tela.painelConfigRapida()
        opc = int(input("\nOpção:"))


    if opc == 10:       
        while True:
            tela.limparTela()
            print("Enquadramento do plano Cartesiano\n")
            planoCartesiano = Bresenham(inicioMatriz,fimMatriz)
            planoCartesiano.matrizAtual()
            tela.miniEnquandramento(inicioMatriz,fimMatriz)
            print("[0]Sair    [1]Novo enquadramento")
            tamanhoMatriz = int(input("opção:"))
            if tamanhoMatriz == 1:
                inicioMatriz = int(input("\nX1(negativo):"))
                fimMatriz = int(input("\nX2(positivo):"))
            elif tamanhoMatriz == 0:
                break
        opc = 1
    
    elif opc == 9:
        tela.sobre()
    
    elif opc == 8:
        tela.limparTela()  
        print("curva de berzier\n aperte ENTER para sair")
        s = input()
        
    elif opc == 7:
        planoCartesiano = Bresenham(inicioMatriz,fimMatriz)
        tela.painelConfigRapida()
        listaParesOrdenados = []
        listaArestas = []
        listaPontosOriginais = listaParesOrdenados
        
        # listaParesOrdenados = [[-5,-7,0],
        #                        [5,-7,0],
        #                        [5,3,0],
        #                        [-5,3,0],
        #                        [-5,-7,-10], 
        #                        [5,-7,-10],
        #                        [5,3,-10],
        #                        [-5,3,-10]]
        
        # listaArestas = [ [0,1],[0,3],[0,4],[1,2],[1,5],[2,3],[2,6],[3,7],[7,4],[7,6],[5,6],[5,4]]
        
        
        while True:
            tela.painelConfigRapida()
            tela.limparTela()
            print("Projeções\n")
            planoCartesiano.matrizAtual()
            print("Pontos:", listaParesOrdenados)
            print("ARESTAS:", listaArestas)
            print("[0]Sair     [1]adic. Solido 3D      [2]Adic. Arestas      [3]Ortogonal      [4]Perspectiva(cabinet 30°)")
            adicionarReta = int(input("opção:"))

            if adicionarReta == 1:
                projecao = Projecao(inicioMatriz, fimMatriz)
                listaParesOrdenados = projecao.pegarSolido3d(listaParesOrdenados)
                listaPontosOriginais = listaParesOrdenados
            
            elif adicionarReta == 2:
                projecao = Projecao(inicioMatriz, fimMatriz)
                listaArestas = projecao.criarArestas(listaParesOrdenados)
                
            elif adicionarReta == 3:
                projecao = Projecao(inicioMatriz, fimMatriz)
                planoCartesiano = projecao.ortogonal(listaParesOrdenados, listaArestas)
                listaParesOrdenados = projecao.listaParesOrdenados

                tela.limparTela()
                planoCartesiano.matrizAtual()
                print("Pontos:", listaParesOrdenados)
                print("ARESTAS:", listaArestas)
                sair = input("sair")

                listaParesOrdenados = listaPontosOriginais
                planoCartesiano = Bresenham(inicioMatriz, fimMatriz)

            elif adicionarReta == 4:
                projecao = Projecao(inicioMatriz, fimMatriz)
                planoCartesiano = projecao.cabinet(listaParesOrdenados, listaArestas)
                listaParesOrdenados = projecao.listaParesOrdenados

                tela.limparTela()
                planoCartesiano.matrizAtual()
                print("Pontos:", listaParesOrdenados)
                print("ARESTAS:", listaArestas)
                sair = input("sair")
                
                listaParesOrdenados = listaPontosOriginais
                planoCartesiano = Bresenham(inicioMatriz, fimMatriz)
                
            else:
                break

    elif opc == 6:
        planoCartesiano = Bresenham(inicioMatriz,fimMatriz)
        tela.painelConfigRapida()
        listaParesOrdenados = []
        varredura = VarreduraPreenchimento(inicioMatriz, fimMatriz)
        while True:

            # listaParesOrdenados = [ [0,8], [3, 1], [5, 6], [9, 1], [10, 10]] #ex slide
            # listaParesOrdenados = [[-3, -4], [7, -1], [9, 7], [2, 5]]
            # listaParesOrdenados = [ [1,1], [8, 5], [2, 7] ]
            # listaParesOrdenados =  [[-4, 0], [0, -3], [7, 1], [3, 8]]

            # listaParesOrdenados = [[-5, -5], [6, -3], [10, 1], [2, 9], [-5, 4], [0, 0]]  #ex 1
            # listaParesOrdenados = [[-8, -1], [2, 2], [-1, 7], [-6, 3], [-4, -6], [5, 0], [10, 4], [-2, 10], [-10, 5]]  #ex 2
            # listaParesOrdenados =  [[0, 5], [6, -8], [10, 0], [6, 7], [0, -5], [-7, 7], [-10, 0], [-7, -8]]  #ex 3

            tela.painelConfigRapida()
            tela.limparTela()
            print("Preenchimento\n")

            planoCartesiano.matrizAtual()
            print("\nLista de pares Ordenados:", listaParesOrdenados)
            print("[0]Sair - [1]adic Aresta - [2]Varredura(Poli. Irregular) - [3]Preenchimento(Poli. Regular)")
            varredura.printTabelaVarredura()
            varredura.printTabelaInterseccoes()
            
            adicionarReta = int(input("opção:"))
            if adicionarReta == 1:
                listaParesOrdenados = varredura.pegarRetas()
                planoCartesiano = varredura.planoCartesiano

            elif adicionarReta == 2:
                varredura.criaTabelaVarredura(listaParesOrdenados)
                planoCartesiano = varredura.fazerVarredura()
                planoCartesiano = varredura.pintarBordas(listaParesOrdenados, planoCartesiano)
                s = input("continuar...")

            elif adicionarReta == 3:
                tela.limparTela()
                planoCartesiano.matrizAtual()
                print("informe o ponto inicial")
                x = int(input("x:"))
                y = int(input("y:"))
                planoCartesiano = varredura.preenchimento(x, y,1, planoCartesiano)
                s = input("continuar...")

            else:
                break

    elif opc == 5:
        
        while True:
            adicionarReta = 0
            tela.limparTela()
            planoCartesiano = Bresenham(inicioMatriz,fimMatriz)
            listaParesOrdenados = []

            print("Recorde de linha e poligonos\n")
            planoCartesiano.matrizAtual()

            print("\nLista de pares Ordenados:", listaParesOrdenados)
            print("[0]Sair - [1]linha - [2]Poligono")
            adicionarReta = int(input("opção:"))
            
            if adicionarReta == 1:
                while True:
                    tela.limparTela()
                    recorte = Recorte(inicioMatriz, fimMatriz)
                    print("Recorde de linha\n")
                    # pegar linhas
                    listaParesOrdenados = recorte.pegarRetas(listaParesOrdenados)
                    break

                while True:
                    tela.limparTela()
                    planoCartesiano = recorte.escreverLinhas(listaParesOrdenados)

                    planoCartesiano.matrizAtual()
                    print("\nLista de pares Ordenados:", listaParesOrdenados)
                    tela.miniEnquandramento(inicioMatriz,fimMatriz)
                    print("\n[0]Sair   [1]Novo enquadramento")
                    tamanhoMatriz = int(input("opção:"))
                    if tamanhoMatriz == 1:
                        inicioMatriz = int(input("\nX1(negativo):"))
                        fimMatriz = int(input("\nX2(positivo):"))
                        recorte = Recorte(inicioMatriz, fimMatriz)
                    elif tamanhoMatriz == 0:
                        adicionarReta = 0
                        break

            elif adicionarReta == 2:
                tela.limparTela()
                recorte = Recorte(inicioMatriz, fimMatriz)

                # pegar linhas                  
                listaParesOrdenados = recorte.pegarRetas(listaParesOrdenados)
                planoCartesiano = recorte.planoCartesiano
    
                while True:
                    tela.limparTela()
                    planoCartesiano.matrizAtual()

                    print("\nLista de pares Ordenados:", listaParesOrdenados)
                    tela.miniEnquandramento(inicioMatriz,fimMatriz)
                    print("\n[0]Sair   [1]Novo enquadramento")
                    
                    tamanhoMatriz = int(input("opção:"))
                    if tamanhoMatriz == 1:
                        inicioMatriz = int(input("\nX1(negativo):"))
                        fimMatriz = int(input("\nX2(positivo):"))
                        recorte = Recorte(inicioMatriz, fimMatriz)
                        planoCartesiano = recorte.escreverLinhas(listaParesOrdenados)           
                    else:
                        break
            else:
                break
       
    elif opc == 4:
        planoCartesiano = Bresenham(inicioMatriz,fimMatriz)
        listaParesOrdenados = []

        while True:
            tela.limparTela()
            print("Transformações Básicas\n")
            planoCartesiano.matrizAtual()
            print("\nLista de pares Ordenados:", listaParesOrdenados)
            print("[0]Sair - [1]adicionar nova Reta - [2]translação - [3]Rotação - [4]Escala")
            adicionarReta = int(input("opção:"))

            if adicionarReta == 1:
                transfor = Transformacoes(inicioMatriz, fimMatriz)
                listaParesOrdenados = transfor.pegarPontos()
                planoCartesiano = transfor.planoCartesiano
    
            elif adicionarReta == 2:
                print("translação")
                eixoX = int(input("translação em X:"))
                eixoY = int(input("translação em y:"))
                transfor = Transformacoes(inicioMatriz, fimMatriz)
                planoCartesiano = transfor.fazerTranslacao(listaParesOrdenados, eixoX, eixoY)
                listaParesOrdenados = transfor.listaParesOrdenados
                
            elif adicionarReta == 3:
                tela.limparTela()
                planoCartesiano.matrizAtual()
                print("\nLista de pares Ordenados:", listaParesOrdenados)
                indicePivo = int(input("Selecione o Pivo na lista de Pontos acima(atraves de seu indice na lista):"))
                print("Angulos disponiveis(tambem negativo): 30°, 45°, 60°, 90° \n")
                angulo = int(input("Angulo:"))
                transfor = Transformacoes(inicioMatriz, fimMatriz)
                planoCartesiano = transfor.fazerRotacao(angulo, indicePivo, listaParesOrdenados)
                listaParesOrdenados = transfor.listaParesOrdenados

            elif adicionarReta == 4:
                tela.limparTela()
                print("Escala")
                planoCartesiano.matrizAtual()
                print("E > 1:      Ampliação da imagem")
                print("0 < E < 1:  redução da imagem")
                print("E < 0:      Espelhamento\n")
                Ex = float(input("fator de escala para X:"))
                Ey = float(input("fator de escala para Y:"))
                print("\nLista de pares Ordenados:", listaParesOrdenados)
                pontoFixo = int(input("Ponto fixo(indice na lista de pontos):"))
                transfor = Transformacoes(inicioMatriz, fimMatriz)
                planoCartesiano = transfor.atualizarEscala(listaParesOrdenados, Ex, Ey, pontoFixo)
                listaParesOrdenados = transfor.listaParesOrdenados

            else:
                break

    elif opc == 3:
        tela.limparTela()
        planoCartesiano = Bresenham(inicioMatriz,fimMatriz)
        print("Circulo\n")

        planoCartesiano.matrizAtual()
        
        xc = int(input("\nXc inicial:"))
        yc = int(input("\nYc inicial:"))
        raio = int(input("\nRaio(R>1):"))
        
        circulo = Circulo(xc, yc, raio, planoCartesiano)
        circulo.calcPontosCirculo()
        circulo.desenhaCirculo()
        
        tela.limparTela()
        planoCartesiano.matrizAtual()
        sair = input("aperte enter para sair.")

    elif opc == 2:
        planoCartesiano = Bresenham(inicioMatriz,fimMatriz)
        listaParesOrdenados = []

        while True:
            tela.limparTela()
            print("Polilinhas\n")
            tela.painelConfigRapida()
            planoCartesiano.matrizAtual()
            print("\nLista de pares Ordenados:", listaParesOrdenados)
            print("Serão traçadas retas de ponto a ponto considerando a lista acima")
            x = int(input("\nX:"))
            y = int(input("\nY:"))
            par = [x, y]        
            listaParesOrdenados.append(par)

            planoCartesiano = Bresenham(inicioMatriz,fimMatriz)
            if len(listaParesOrdenados) > 1:
                for i in range(len(listaParesOrdenados)):
                    if i < len(listaParesOrdenados)-1:
                        xInicial = listaParesOrdenados[i][0]
                        yInicial = listaParesOrdenados[i][1]
                        xFinal = listaParesOrdenados[i+1][0]
                        yFinal = listaParesOrdenados[i+1][1]
                        planoCartesiano.reta(xInicial, yInicial, xFinal, yFinal)
              
                tela.painelConfigRapida()
                planoCartesiano.matrizAtual()
                print("\nLista de pares Ordenados:", listaParesOrdenados)
                print("[0]Sair  -  [1]adicionar novo Ponto   ")
                adicionarReta = int(input("opção:"))
            
                if adicionarReta == 0:
                    break
            
    elif opc == 1:
        planoCartesiano = Bresenham(inicioMatriz,fimMatriz)
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
                    planoCartesiano.reta(xInicial, yInicial, xFinal, yFinal)
                planoCartesiano.matrizAtual()
            tela.limparTela()
            print("Bresenham\n")
            planoCartesiano.matrizAtual()
            print("\nLista de pares Ordenados:", listaParesOrdenados)
            print("[0]Sair - [1]adicionar nova Reta - [2]remover")
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
                listaParesOrdenados.pop(-1)
                listaParesOrdenados.pop(-1)
                planoCartesiano = Bresenham(inicioMatriz,fimMatriz)
            else:
                break

tela.limparTela()
print("       Obrigado por usar nosso paint <3\n\n\n\n\n\n")
time.sleep(3)
