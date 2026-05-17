

#  Receba um número e determine se ele é um palíndromo (lê-se igual de frente para trás).

# 1. Receber um número inteiro

num = int(input())

# 2. Determinar se é um palíndromo

# Transforma a variavel num em string para poder manipular / inverter a ordem e verificar se é um palindromo
string = str(num)

if string == string[::-1]:
    print(string, "é um palíndromo!")
else:
    print(string, "não é um palíndromo!")