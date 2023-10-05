valor = int(input("Digite um valor: "))

if valor <= 0:
    print("Digite um valor válido!")
else:
    saque = valor

    notas = [100, 50, 20, 10, 5, 2]
    quantidades = [0, 0, 0, 0, 0, 0]

    for i in range(len(notas)):
        while valor >= notas[i]:
            valor -= notas[i]
            quantidades[i] += 1

    if valor == 0:
        mensagem = f"Foi sacado {saque}, sendo"
        for i in range(len(notas)):
            if quantidades[i] > 0:
                mensagem += f"{quantidades[i]} notas de {notas[i]}R$,"
        mensagem = mensagem[:-1]
        print(mensagem)
    else:
        print("O valor solicitado deve ser múltiplo de R$ 2, R$ 5, R$ 10, R$ 20, R$ 50 ou R$ 100 reais!")
