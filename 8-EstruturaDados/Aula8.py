

# Dado um array, definimos uma soma acumulada de um array como runningSum[i] = sum(array[0]+array[i]).
# Retorne a soma acumulada de array.

array = [1,2,3,4]
resultado = []

contador = 0

for numero in array:
    contador += numero
    resultado.append(contador)

print(resultado)