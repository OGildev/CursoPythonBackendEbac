
# Dado um endereço IP válido (IPv4), retorno uma versão ajustada desse endereço IP.
# Um endereço IP ajustado substitui cada ponto "." por "[.]".

# 1. Receber a string com nosso endereço IP.

endereco_ip = input()

# 2. Fazer a operação para substituir os pontos por parenteses e ponto

novo_ip = ""

for i in endereco_ip:
    if i == ".":
        novo_ip += "[.]"
    else:
        novo_ip += i

print(novo_ip)

# OUTRA FORMA DE RESOLVER ESTE EXERCÍCIO
# endereco_ip = input()
# endereco_ip = endereco_ip.replace('.', '[.]')
# print(endereco_ip)