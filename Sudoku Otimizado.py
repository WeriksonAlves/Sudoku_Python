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
            M[l][c] = random.randint(1,n) #Seleciona um número aleatório;
            while True:
                lin = verlin(l,c,M) #Verifica se o nº já tem na linha atual;
                col = vercol(l,c,M) #Verifica se o nº já tem na coluna atual;
                if (lin==0) and (col==0):
                    break  #Se ele não pertencer a ambas, prossiga;
                else: #Caso contrario selecione um novo número;
                    M[l][c] = random.randint(1,n)
                    lin = verlin(l,c,M) #Verifica se o nº já tem na linha atual;
                    col = vercol(l,c,M) #Verifica se o nº já tem na coluna atual;
    return M
#......................................................................
def verlin(l,c,M):
    linha = set() #Inicializa um conjunto vazio;
    linha.add(M[l][0]) #Adiciona o primeiro elemento de cada linha ao conjunto;
    for j in range (0,c):
        linha.add(M[l][j]) #Adiciona os outros nº ao cojunto (exceto o nº atual);
    if M[l][c] in linha:
        return 1  #Se o nº atual pertencer a linha;
    else:
        return 0 #Se o nº atual não pertencer a linha;
#......................................................................
def vercol(l,c,M):
    coluna = set() #Inicializa um conjunto vazio;
    coluna.add(M[0][c]) #Adiciona o primeiro elemento de cada coluna ao conjunto;
    for i in range (0,l):
        coluna.add(M[i][c]) #Adiciona os outros nº ao cojunto (exceto o nº atual);
    if M[l][c] in coluna:
        return 1 #Se o nº atual pertencer a coluna;
    else:
        return 0 #Se o nº atual não pertencer a coluna;
#......................................................................
def main():
    n= int(input('Digite o Tamnho da Matriz Quadrada: '))
    Matriz = cria_Matriz(n)
    print('Teste')
    print(Matriz)
#......................................................................
main()