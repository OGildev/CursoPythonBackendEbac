

 
try:
    numero = int(input("Digite um número:"))
    resultado = 10 / numero
    print(resultado)
except ValueError:
    print("Erro: Entrada válida. Favor inserir apenas números.")
except ZeroDivisionError:
    print("Erro: Não existe divisão por zero.")