
# List Comprehension - Manipulação de array/listas

#List Comprehension:
array = [elemento for elemento in range(1,6)]
print(array)

# Exemplo comum:
for elemento in range(1,6):
    print(elemento)

# Outro exemplo: Pegar a letra inicial de cada palavra de um array/lista

palavras = ["python", "é", "divertido"]

# Exemplo comum:
for palavra in palavras:
    print(palavra[0])

#List Comprehension:
iniciais = [palavra[0] for palavra in palavras]
print(iniciais)

# Outro exemplo: Em uma lista de 10 números, pegar os quadrados dos números impares

#List Comprehension:
quadrados_impares = [elemento**2 for elemento in range(1,11) if elemento % 2 != 0]
print(quadrados_impares)

# Exemplo de resolução comum:
array2 = []

for elemento in range(1,11):
    array2.append(elemento**2)
        
for elemento in range(1,11):
    if elemento % 2 != 0:
        print(elemento)