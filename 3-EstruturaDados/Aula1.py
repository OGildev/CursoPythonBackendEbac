
# Escreva um programa que receba três números e exiba o segundo maior número entre eles.

# 1. Preciso receber os números separadamente

n1, n2, n3, n4 = map(int, input().split())

# 2. Criar uma lógica para ver quem é o segundo maior

# Criar o Array sempre utilizar chave []
array = []

# Para vincular as variáveis de entrada ao array, podemos utilizar o array.append(variavel)
array.append(n1)
array.append(n2)
array.append(n3)
array.append(n4)

print(array)

# Ordenando o array com sort()
array.sort()

print(array)

# 3. Mostrar na tela o segundo maior número

print(array[1])