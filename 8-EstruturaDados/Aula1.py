

# Dado um número inteiro não negativo,
# retorne a raiz quadrada para o número inteiro mais próximo.
# O número inteiro retornado também deve ser não negativo.

# 1. O que é uma raiz quadrada
# 2. O que é uma biblioteca
# 3. Escrevendo a solução para o problema

import math

numero = int(input("Digite um número: "))

resultado = math.sqrt(numero)

print("A raiz quadrada de", numero, "é:", resultado)