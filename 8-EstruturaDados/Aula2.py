
# Dada uma string, retorne o número de segmentos na string.
# Um segmento é definido como uma sequência contínua de caracteres não espaciais

# Portanto, precisamos retornar a quantidade de caracteres que se iniciam uma palavra!
# Por exemplo, na string "Olá, meu nome é Gilberto Lima" existem 6 segmentos: "Olá," igual a 1 segmento, "meu" igual a mais 1 segmento
# e assim por diante.

string = "Olá, meu nome é Gilberto Lima"

# função split() divide uma string em uma lista de partes.
# Portanto, cria-se uma lista sem os espaços da string. Após feita a separação pelo split(), podemos utilizar a len() para contagem

array = string.split()

print(len(array))
