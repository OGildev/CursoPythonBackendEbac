
# Dada um array de números inteiros, cada elemento aparece duas vezes, exceto um. Encontre o elemento único.

array = [1,1,1,2,2,3,3,3,4,4,5]

dicionario = {}

for i in array:
    if i not in dicionario:
        dicionario[i] = 1 
    else:
        dicionario[i] += 1     

for chave, valor in dicionario.items():
    if valor == 1:
        print(chave)

