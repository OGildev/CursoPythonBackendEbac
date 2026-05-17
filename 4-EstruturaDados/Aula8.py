
# Dado um array de inteiros, um inteiro sortudo é um inteiro que tem uma frequência no array igual ao seu valor.

array = [1,2,3,3,4,4,5,5,6,7,8,8,2]

# Criar um dicionário para adicionar todos os valores, descobrindo, assim, as chaves e valores
# A chave é o próprio número e o valor é a frequência, ou seja, a quantidade de vezes que esse número apareceu no array

dic = {}

# 2. Fazer um looping dentro do meu dicionário e descobrir quem é a chave que é a igual ao valor

for i in array:
    if i not in dic:
        dic[i] = 1
    else:
        dic[i] += 1

# print(dic)

for chave, valor in dic.items():
    if chave == valor:
       print(chave)