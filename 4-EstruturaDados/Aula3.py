# Você recebe um array de números inteiros: array
# Os elementos únicos de um array são os elementos que aparecem exatamente uma vez no array.
# Retorne a soma de todos os elementos únicos do array.

array = [1,2,2,2,3,3,4,5,5,5]

# 1. Criar uma estrutura de dados / dicionário para adicionar a chave e o valor

dicionario = {}

for i in array:
    if i not in dicionario:
        dicionario[i] = 1 
    else:
        dicionario[i] += 1 

# 2. Encontrar quem são os valores que aparecem uma única vez
# 3. fazer a soma das chaves que aparecem apenas uma vez

soma_das_chaves = 0

for chave, valor in dicionario.items():
    if valor == 1:
        soma_das_chaves += chave

print(soma_das_chaves)

