while True:
    # Entrada dos números com tratamento de exceção
    while True:
        try:
            numero1 = float(input("Insira o primeiro número: "))
            numero2 = float(input("Insira o segundo número: "))
            break
        except ValueError:
            print("Valor inválido! Por favor, insira apenas números.")

    # Operações utilizando lambda
    operacoes = {
        1: ("Soma", lambda a, b: a + b),
        2: ("Subtração", lambda a, b: a - b),
        3: ("Multiplicação", lambda a, b: a * b),
        4: ("Divisão", lambda a, b: a / b)
    }

    # Menu utilizando list comprehension
    print("\nEscolha uma operação:")
    [print(f"{chave} - {valor[0]}") for chave, valor in operacoes.items()]

    try:
        opcao = int(input("Digite a opção desejada: "))

        if opcao not in operacoes:
            print("Operação inválida!")
            continue

        print(f"Você escolheu: {operacoes[opcao][0]}")

        # Verificação de divisão por zero
        if opcao == 4:
            while numero2 == 0:
                try:
                    numero2 = float(
                        input("Divisão por zero não é permitida. Por favor, insira outro número: ")
                    )
                except ValueError:
                    print("Valor inválido! Por favor, insira apenas números.")

        # Executa a operação
        resultado = operacoes[opcao][1](numero1, numero2)

        print(f"O resultado é: {resultado}")

    except ValueError:
        print("Entrada inválida! Escolha uma opção numérica.")

    # Pergunta se deseja continuar
    continuar = input("Deseja realizar outra operação? (S/N): ").strip().upper()

    if continuar != "S":
        print("Programa encerrado.")
        break