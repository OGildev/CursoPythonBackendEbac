
# Função anonima = Lambda, elas não precisam ser inicializadas. Podemos utilizar elas dentro de um processo / aplicação, ou seja, 
# poupa tempo, e organiza melhor o código.


# Glossário:
# Também conhecidas como funções anônimas, são funções definidas de forma compacta para operações rápidas e simples, sem a necessidade de uma declaração completa.

# def soma(x, y):
#     return x + y

# print(soma(5,10))

# soma = lambda x, y : x + y

# print(soma(5,5))

array_duplicados = []

array = [1,2,3,4,5]

for i in array:
    array_duplicados.append(i * 2)

# Aplicação da função Lambda para resolver o problema acima
duplicados = map(lambda numero : numero * 2, array)

print(array_duplicados)
print(list(duplicados))