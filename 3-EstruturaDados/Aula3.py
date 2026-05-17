
# Escreva um programa que calcule a média entre duas notas de um aluno.
# Condição 1: Média maior que 7 está aprovado.
# Condição 2: Média entre 5 e 7 está em recuperação.
# Condição 3: Média abaixo de 5 está reprovado. 

nota1, nota2 = map(int, (input().split()))

media = nota1 + nota2 / 2

print(media)

if media >= 7:
    print("Aluno aprovado! A média do aluno foi: ", media)
elif media >= 5 and media < 7:
    print("Aluno em recuperação! A média do aluno foi: ", media)
else:
    print("Aluno reprovado!A média do aluno foi: ", media)
