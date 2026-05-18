
# Definimos o uso de letras maiúsculas em uma palavra como correto quando o seguinte o caso é valido:

# Todas as letras desta palavra são maiúslucas, como "EUA".

# Exercício: Dada uma palavra de string, retorne verdadeiro se o uso de letras maiúsculas está correto.

string = "EUA"

for letra in string:
    if letra.string.isupper():
        contador += 1

    
if contador == len(string):
    print("Passou pelo teste!")
else:
    print("Reprovado!")
