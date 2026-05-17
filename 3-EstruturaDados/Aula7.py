
# Receba uma lista de palavras e ordene-as em ordem alfabética

# 1. Criar um array vazio para receber essas palavras

array = []

# 2. Definir uma quantidade de palavras

# Serão 5 palavras!

# 3. Criar a lógica para receber essas palavras e adicionar dentro do array

for i in range(1,6):
    palavra = input()
    array.append(palavra)

print(array)

# 4. Ordenar a lista

array.sort()

# 5. Printar na tela

print(array)