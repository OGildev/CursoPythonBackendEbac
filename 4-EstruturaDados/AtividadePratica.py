
def adicionar_produto(estoque):
    nome = input("Nome do produto: ").strip()
    quantidade = int(input("Quantidade: "))
    preco = float(input("Preço: "))

    estoque[nome] = {
        "quantidade": quantidade,
        "preço": preco
    }

def listar_produtos(estoque):
    if not estoque:
        print("Nenhum produto cadastrado.")
    else:
        for nome, dados in sorted(estoque.items(), key=lambda item: item[0]):
            print(
                f"{nome}: Quantidade disponível - {dados['quantidade']} | Preço - R${dados['preço']:.2f}"
            )

def remover_produto(estoque):
    nome = input("Nome do produto: ").strip()

    if nome in estoque:
        del estoque[nome]
        print(f"Produto '{nome}' removido com sucesso!")
    else:
        print("Erro: Produto não encontrado.")

def atualizar_quantidade(estoque):
    nome = input("Nome do produto: ").strip()

    if nome in estoque:
        nova_quantidade = int(input("Nova quantidade: "))
        estoque[nome]["quantidade"] = nova_quantidade
    else:
        print("Erro: Produto não encontrado.")

def exibir_menu():
    print("Adicionar produto")
    print("Listar produtos")
    print("Remover produto")
    print("Atualizar quantidade de produto")
    print("Sair")

def main():
    estoque = {}

    while True:
        exibir_menu()

        opcao = input("Escolha uma opção: ").strip()

        if opcao == "1":
            adicionar_produto(estoque)

        elif opcao == "2":
            listar_produtos(estoque)

        elif opcao == "3":
            remover_produto(estoque)

        elif opcao == "4":
            atualizar_quantidade(estoque)

        elif opcao == "5":
            break

        else:
            print("Opção inválida.")

if __name__ == "__main__":
    main()