

# Dado um array de tamanho n, retorne o elemento majoritário.
# O elemento majoritário é aquele que aparece mais de n/2 vezes.
# Você pode assumir que o elemento majoritário sempre existe no array. 


array = [3,2,3]
# n é o tamanho do array
n = len(array)

# item majoritario é o item que aparece mais de n/2 vezes
item_majoritario = n/2

dicionario = {}

for item in array:
    if item not in dicionario:
        dicionario[item] = 1
    else:
        dicionario[item] += 1 

for chave, valor in dicionario.items():
    if valor >= item_majoritario:
        print(chave)
    