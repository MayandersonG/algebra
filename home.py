from menu import help
from operacoes import transpose, sum

a_linhas = int(input('Informe o número de linhas da matriz A: '))
a_colunas = int(input('Informe o número de colunas matriz A: '))

# Criação da matriz
matrizA = [None] * a_linhas
for i in range(len(matrizA)):
    matrizA[i] = [None] * a_colunas

# Cadastro dos valores na matriz
for i in range(len(matrizA)):
    for j in range(len(matrizA[i])):
        matrizA[i][j] = float(input(f"Digite o valor da posição [{i+1}][{j+1}]: "))

b_linhas = int(input('Informe o número de linhas da matriz B: '))
b_colunas = int(input('Informe o número de colunas matriz B: '))

# Criação da matriz
matrizB = [None] * b_linhas
for i in range(len(matrizB)):
    matrizB[i] = [None] * b_colunas

# Cadastro dos valores na matriz
for i in range(len(matrizB)):
    for j in range(len(matrizB[i])):
        matrizB[i][j] = float(input(f"Digite o valor da posição [{i+1}][{j+1}]: "))

objA = { 'matriz': matrizA, 'linhas': a_linhas, 'colunas': a_colunas }
objB = { 'matriz': matrizB, 'linhas': b_linhas, 'colunas': b_colunas }

help()
while True:
    escolha = input('Escolha uma das opções: ')

    if escolha == '1':
        matriz_escolhida = input('Escolha qual matriz você quer calcular a transposta (a ou b): ')
        if matriz_escolhida == 'a':
            obj = objA
        if matriz_escolhida == 'b':
            obj = objB
        transpose.transpose(obj)

    elif escolha == '2':
        sum.sum(objA, objB)
    
    elif escolha == '3':
        pass

    elif escolha == 'help':
        help()
        



