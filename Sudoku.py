'''
Sudoku 03/04/2019
1 Fase = Criar a matriz com os 91 numeros => FEITO
2 Fase = Não repetir os numeros nas linhas e colunas => FEITO
3 Fase = Criar o menu principal.
4 Fase = Apagar os numeros de acordo com a opção selecionada.
'''
#......................................................................
#Lista de importações:
import numpy as np
import random
#......................................................................
def cria_Matriz(n):
    M = np.zeros((n,n), dtype=int) #Inicializa a matriz compostas de zeros;
    for l in range(0,n):
        for c in range(0,n):
            print(M)
            cte = random.randint(1,n) #Seleciona um número aleatório;
            M[l][c] = cte
            T = list()
            i = 0
            while True:
                i = i + 1
                lin = verlin(l,c,M) #Verifica se o nº já tem na linha atual;
                col = vercol(l,c,M) #Verifica se o nº já tem na coluna atual;
                if (lin==0) and (col==0):
                    break  #Se ele não pertencer a ambas, prossiga;
                elif (lin==0) and (col==1):
                    M[l][c] = random.randint(1,n)
                elif (lin==1) and (col==0):
                    M[l][c] = random.randint(1,n)
                T.append(i)
                print(T)
                if ( len(T) >= n):
                    print("Erro")
                    reset()              
    return M
#......................................................................
def verlin(l,c,M):
    linha = set() #Inicializa um conjunto vazio;
    #linha.add(M[l][0]) #Adiciona o primeiro elemento de cada linha ao conjunto;
    for j in range (0,c):
        linha.add(M[l][j]) #Adiciona os outros nº ao cojunto (exceto o nº atual);
    print(linha)
    if M[l][c] in linha:
        return 1  #Se o nº atual pertencer a linha;
    else:
        return 0 #Se o nº atual não pertencer a linha;
#......................................................................
def vercol(l,c,M):
    coluna = set() #Inicializa um conjunto vazio;
    #coluna.add(M[0][c]) #Adiciona o primeiro elemento de cada coluna ao conjunto;
    for i in range (0,l):
        coluna.add(M[i][c]) #Adiciona os outros nº ao cojunto (exceto o nº atual);
    print(coluna)
    if M[l][c] in coluna:
        return 1 #Se o nº atual pertencer a coluna;
    else:
        return 0 #Se o nº atual não pertencer a coluna;
#......................................................................
def main():
    print ('Teste')
    n= int(input('Digite o Tamnho da Matriz Quadrada: '))
    Matriz = cria_Matriz(n)
    print(Matriz)
    #reset()
#......................................................................
def reset():
    while True:
        reset = input('\nDeseja continuar[S/N]? ')
        if reset in 'Ss':
            main()
        elif reset in 'Nn':
            print('Fim do Programa')
            break
        else:
            print('Codigo errado')
#......................................................................
main()