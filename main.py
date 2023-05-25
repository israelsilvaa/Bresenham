# import random
from modulos.transformacoes import Transformacoes
from modulos.bresenham import Bresenham
from modulos.circulo import Circulo
from modulos.projecao import Projecao
from modulos.varreduraPreenchimento import VarreduraPreenchimento
from modulos.recorte import Recorte
from modulos.tela import Tela
import time

tela = Tela()

inicioMatriz = -5
fimMatriz = 10
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

    if opc == 9:
        tela.sobre()
    
    if opc == 8:
        tela.limparTela()  
        print("curva de berzier\n aperte ENTER para sair")
        s = input()
        
    if opc == 7:
        teste = Bresenham(inicioMatriz,fimMatriz)
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
            teste.matrizAtual()
            print("Pontos:", listaParesOrdenados)
            print("ARESTAS:", listaArestas)
            print("[1]adic. Solido 3D      [2]Adic. Arestas      [3]Ortogonal      [4]Perspectiva(cabinet 30°)      [5]Sair")
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
                teste = projecao.ortogonal(listaParesOrdenados, listaArestas)
                listaParesOrdenados = projecao.listaParesOrdenados

                tela.limparTela()
                teste.matrizAtual()
                print("Pontos:", listaParesOrdenados)
                print("ARESTAS:", listaArestas)
                sair = input("sair")

                listaParesOrdenados = listaPontosOriginais
                teste = Bresenham(inicioMatriz, fimMatriz)

            elif adicionarReta == 4:
                projecao = Projecao(inicioMatriz, fimMatriz)
                teste = projecao.cabinet(listaParesOrdenados, listaArestas)
                listaParesOrdenados = projecao.listaParesOrdenados

                tela.limparTela()
                teste.matrizAtual()
                print("Pontos:", listaParesOrdenados)
                print("ARESTAS:", listaArestas)
                sair = input("sair")
                
                listaParesOrdenados = listaPontosOriginais
                teste = Bresenham(inicioMatriz, fimMatriz)
                
            else:
                break

    elif opc == 6:
        teste = Bresenham(inicioMatriz,fimMatriz)
        tela.painelConfigRapida()
        listaParesOrdenados = []

        varredura = VarreduraPreenchimento(inicioMatriz, fimMatriz)
        y = 0
        while True:

            # listaParesOrdenados = [ [0,8], [3, 1], [5, 6], [9, 1], [10, 10]]
            # listaParesOrdenados = [[-3, -4], [7, -1], [9, 7], [2, 5]]
            # listaParesOrdenados = [ [1,1], [8, 5], [2, 7] ]
            tela.painelConfigRapida()
            tela.limparTela()
            teste.matrizAtual()
            print("\nLista de pares Ordenados:", listaParesOrdenados)
            print("[1]adic Aresta - [2]Varredura(Poli. Irregular) - [3]Preenchimento(Poli. Regular) - [5]Sair")
            varredura.printTabelaVarredura()
            varredura.printTabelaInterseccoes()
            
            adicionarReta = int(input("opção:"))
            if adicionarReta == 1:
                listaParesOrdenados = varredura.pegarRetas()
                teste = varredura.planoCartesiano

            elif adicionarReta == 2:
                varredura.criaTabelaVarredura(listaParesOrdenados)
                teste = varredura.fazerVarredura()
                teste = varredura.pintarBordas(listaParesOrdenados, teste)
                s = input("continuar...")

            elif adicionarReta == 3:
                x = int(input("x:"))
                y = int(input("y:"))
                varredura.preenchimento(x, y,1, teste)
                s = input("continuar...")

            else:
                break

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
                listaParesOrdenados = transfor.listaParesOrdenados
                
            elif adicionarReta == 3:
                tela.limparTela()
                teste.matrizAtual()
                print("\nLista de pares Ordenados:", listaParesOrdenados)
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
                listaParesOrdenados = transfor.listaParesOrdenados

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
