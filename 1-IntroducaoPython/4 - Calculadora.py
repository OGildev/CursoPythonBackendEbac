print("Seja bem-vindo à calculadora!")

continuar = "S"

while continuar == "S":

    print("Escolha a operação:")
    print("1 - Soma")
    print("2 - Subtração")
    print("3 - Multiplicação")
    print("4 - Divisão")

    opcao = int(input("Digite o número da operação desejada: "))

    if opcao < 1 or opcao > 4:
        print("Você digitou uma opção inválida! Digite uma operação da calculadora entre 1 e 4.")
        continue

    num1 = float(input("Digite o primeiro número: "))
    num2 = float(input("Digite o segundo número: "))

    if opcao == 1:
        print("Resultado:", num1 + num2)
    elif opcao == 2:
        print("Resultado:", num1 - num2)
    elif opcao == 3:
        print("Resultado:", num1 * num2)
    elif opcao == 4:
        if num2 == 0:
            print("O num2 que você inseriu é igual a 0! Não é possível realizar divisões por zero! Escolha outro número.")
            continue
        else:
            print("Resultado:", num1 / num2)
    
    continuar = input("Deseja realizar outra operação matemática? Digite S para continuar ou N para sair: ")

print("Obrigado por utilizar a calculadora! Tenho certeza que nos veremos novamente!")
        