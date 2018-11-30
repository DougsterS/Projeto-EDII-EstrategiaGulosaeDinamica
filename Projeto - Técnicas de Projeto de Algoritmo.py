#encoding='UTF-8'
__author__ = '''Douglas A. Monteiro Alcantara Justino - 1710017920
e Karoline Lyra de Vasconcelos - 1710018255'''

import time

def gulosa(arrayCarac,arrayFrase):#Função da Estratégia Gulosa
        totalCarac = 0#Responsável por calcular o tamanho de Caracteres dos respectivos cartoes
        totalFrase = 0#Responsável por calcular o tamanho de vezes que o Eu te amo aparece dentro da range desejada
        i = 0#Variavel utilizada apra acessar os indices do vetor
        for x in arrayCarac:#Percorre o vetor dos cartoes
                if((totalCarac+arrayCarac[i]) <= arrayCarac[0]):#Verifica se o valor dos cartoes informados 
                        if i==0:#Condicional necessaria para que o programa nao adicione o primeiro valor
                                #no total de caracteres de cartoes ocasionando em uma falha onde o programa
                                #so adiciona o valor do índice 0
                                totalFrase += arrayFrase[i]
                                i+=1         
                        else:
                                totalFrase += arrayFrase[i]
                                totalCarac += arrayCarac[i]
                                i+=1
                else:#esse else e necessario para que o contador continue sendo adicionado
                     #no caso do valor lido ser um valor maior que o valor do índice 0
                        i+=1
        print('Estrategia Gulosa: ',totalFrase,'\n')

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
        print('''1 - Executar programa\n2 - Equipe responsavel\n3 - Sair do Programa''')
        opcao = int(input('Opcao: '))
        
        if opcao == 1:#Opcao principal que roda as opcoes do programa
                carac = 1
                frase = 1
                totalTeAmo = 0
                caracters = []
                frases = []
                loop2 = True
                print('''\nInforme o valor de diversos cartoes, caso deseje encerrar o processo\ndigite 0 em qualquer uma das opcoes abaixo:\n''')
                while(loop2):
                        carac = int(input('Informe o valor de caracteres disponiveis no cartao: '))
                        frase = int(input('Informe o numero de frases selecionadas: '))
                        caracters.append(carac)
                        frases.append(frase)
                        if(carac == 0 and frase ==0):
                                loop2 = False
                pass
        
        elif opcao == 2:#Opcao que informa os autores do codigo
                print('\n///Equipe responsavel///\n')
                print(__author__,'\n')#Autores do codigo
                pass
        
        else:#Opcao que sai do programa
                print('\nObrigado por utilizar o nosso programa! Ate logo')
                time.sleep(3)
                loop = False
                pass
