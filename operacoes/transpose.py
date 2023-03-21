def transpose(obj):
    matriz = obj['matriz']

    # Criação dos valores na matriz C
    matriz_transposta = [None] * obj['colunas']
    for i in range(len(matriz_transposta)):
        matriz_transposta[i] = [None] * obj['linhas']

    # Inserção dos valores na matriz C
    for i in range(len(matriz_transposta)):
        for j in range(len(matriz_transposta[i])):
            matriz_transposta[i][j] = matriz[j][i]

    # Imprimindo a matriz original e a matriz transposta
    print('-' * 50)
    print("Matriz original:")
    for row in matriz:
        print(row)

    print("Matriz transposta:")
    for row in matriz_transposta:
        print(row)
    print('-' * 50)