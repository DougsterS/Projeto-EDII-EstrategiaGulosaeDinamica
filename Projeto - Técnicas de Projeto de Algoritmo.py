#encoding='UTF-8'
__author__ = '''Douglas A. Monteiro Alcantara Justino - 1710017920
e Karoline Lyra de Vasconcelos - 1710018255'''

import time

def greedy(c, n2, d2):#Algoritmo guloso
        soma = 0#soma de vezes que 'eu te amo' aparece
        caracteres=0#variavel auxiliar para assimilar o valor de caracteres ja incorporados no cartão
        for x in range(len(d2)):#Percorre o array
                if(len(n2) == 1):#Encerra o loop caso o programa tenha apenas um
                        if((n2[0]+caracteres) <= c):
                                soma += d2[0]
                        break
                elif((n2[d2.index(max(d2))] + caracteres) <= c):#Compara a soma do valor atual da variavel auxiliar com
                                                                #o valor de caracteres equivalentes do numero maximo de caracteres informados
                        soma+=max(d2)#soma o maior valor possivel a variavel
                        caracteres += n2[d2.index(max(d2))]#adiciona o valor de caracteres
                d2.remove(max(d2))#remove o maior valor possivel dentre as vezes que eu te amo aparece
                n2.remove(n2[d2.index(max(d2))])#remove o indice equivalente do maior numero de eu te amos
        print('Estrategia Gulosa: ',soma) 

def dinamic(c, n2, d2):
        soma = 0
        
print('''
------------------------------------
*              Ti amu              *
------------------------------------
Bem vindo ao Ti amu, nesse programa
voce deve nos informar o tamanho de
caracteres permitidos e o numero de
frases presentes na mensagem deseja-
-da e informaremos o máximo de vezes
que a palavra : "Eu te amo" deve
aparecer.''')
loop = True
while(loop):
        print('''\n1 - Executar programa\n2 - Equipe responsavel\n3 - Sair do Programa''')
        opcao = int(input('Opcao: '))
        
        if opcao == 1:#Opcao principal que roda as opcoes do programa
                loop2 = True
                N2 = []
                D2 = []
                cartao=1#Enumera o cartao inserido
                while(loop2):
                        print('\nPor favor:\nInforme as informacoes requisitadas')
                        C = int(input('Informe o Comprimento maximo do cartao: '))#Variavel que indica o comprimento maximo do cartao em caracteres
                        F = int(input('Informe o Numero de frases coletadas: '))#Numero de frases coletadas para o cartao
                        if(C == 0 and F ==C):
                                break
                        elif(8>C or C >1000):
                                print('Por favor,informe um Comprimento de cartao(C): maior que 8 e menor que 1000')
                                break
                        elif(1>F or F >50):
                                print('Por favor, informe um Numero de frases(F): maior que 1 e menor do que 50')
                                break
                        else:
                                contador = 0
                                while(contador < F):
                                        print('Por favor informe as seguintes informacoes referentes a FRASE ',(contador+1))
                                        N = int(input('Informe a quantidade de caracteres dessa frase: '))#Indica o numero de caracteres da frase coletada
                                        D = int(input('Informe o numero de vezes que -Eu te Amo- aparece na frase: '))#Indica o numero de vezes que eu te amo aparece na frase em questao
                                        if(D==0 and N==D):
                                                while(contador<F):
                                                        contador+=1#Garante que o programa encerre caso o usuario insira valores nulos
                                        while(8>N or N>1000):
                                                N = int(input('Por favor informe um valor de Caracteres da frase(N) onde ele e maior que 8 e menor que 1000: '))
                                        while(1>D or D>50):
                                                D = int(input('Por favor informe um valor de -Eu Te Amo-(D) onde ele e maior que 1 e menor que 50: '))
                                        N2.append(N)
                                        D2.append(D)
                                        contador +=1
                                print('\n---Resultados---\n')
                                print('Cartao ',cartao)#Exibe o numero do cartao em questao
                                greedy(C,N2,D2)#Faz uso do algoritmo guloso
                                cartao+=1#adiciona mais um pra o caso do usuario adicionar mais um teste
                pass
        
        elif opcao == 2:#Opcao que informa os autores do codigo
                print('\n///Equipe responsavel///\n')
                print(__author__,'\n')#Autores do codigo
                pass
        
        else:#Opcao que sai do programa
                print('\nObrigado por utilizar o nosso programa! Ate logo')
                time.sleep(3)
                break
                pass
