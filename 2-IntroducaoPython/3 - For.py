
def verificar_vip(nome):
    if nome in convidados_vip:
        return print("Parabéns seu nome " + nome + " está na lista!")
    else:
        return None

convidados_vip = ["Alice", "Bob", "Carol"]
nome = input("Digite seu nome para verificar se está na lista vip:" )

verificar_vip(nome)


#print(lista)

# if 1 in lista:
#     print("O número 1 está na lista")
# else:
#     print("Número não está na lista")
    
#for i in lista: 
#    print(i)