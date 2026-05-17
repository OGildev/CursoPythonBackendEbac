

# Escreva um programa que receba um número N e exiba a soma de todos os números de 1 até N.

# 1. Receba um número qualquer

numero = int(input())

# 2. Entender a lógica da soma

# Caso o número do usuário for 5, o programa deverá somar 1 + 2 + 3 + 4 + 5 = 15 e apresentar na tela o resultado.

soma = 0

for i in range (1, numero + 1):
    soma += i

print(soma)