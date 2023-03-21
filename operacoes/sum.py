def sum(objA, objB):
    matrizA = objA['matriz']
    matrizB = objB['matriz']

    linhasA = objA['linhas']
    linhasB = objB['linhas']

    colunasA = objA['colunas']
    colunasB = objB['colunas']

    print('-' * 50)

    # Verifica se as matrizes têm as mesmas dimensões
    if linhasA != linhasB or colunasA != colunasB:
        print("As matrizes devem ter as mesmas dimensões.")
        print('-' * 50)
        return
    
    # Cria a matriz resultante com as mesmas dimensões das matrizes originais
    resultado = [[0 for j in range(len(matrizA[0]))] for i in range(len(matrizA))]

    # Percorre as matrizes originais e soma os elementos correspondentes
    for i in range(len(matrizA)):
        for j in range(len(matrizA[0])):
            resultado[i][j] = matrizA[i][j] + matrizB[i][j]
    
    print("Resultante da soma:")
    for row in resultado:
        print(row)
    print('-' * 50)

