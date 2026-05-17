
# Dada um array de números inteiros, retorne a soma do menor número e do maior número do array.

array = [1,5,33,8,6,99]

# 1. Ordenar o array

array.sort()

print(array)

menor_numero = 0
maior_numero = 0
soma = 0

menor_numero = array[0]
maior_numero = array[-1]

print(menor_numero + maior_numero)
