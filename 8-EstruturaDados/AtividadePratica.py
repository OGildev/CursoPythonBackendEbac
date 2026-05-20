biblioteca = {}
historico_emprestimos = []


def adicionar_livro():
    titulo = input("Digite o título do livro: ")
    autor = input("Digite o nome do autor: ")

    try:
        quantidade = int(input("Digite a quantidade de exemplares: "))

        biblioteca[titulo] = {
            "autor": autor,
            "quantidade": quantidade
        }

        print("Livro adicionado com sucesso!")

    except ValueError:
        print("Erro: a quantidade deve ser um número inteiro.")


def listar_livros():
    if not biblioteca:
        print("Nenhum livro cadastrado.")
    else:
        print("\nLista de livros:")

        for titulo in sorted(biblioteca.keys()):
            autor = biblioteca[titulo]["autor"]
            quantidade = biblioteca[titulo]["quantidade"]

            print(f"{titulo} - {autor} - {quantidade} disponível(is)")


def remover_livro():
    titulo = input("Digite o título do livro a ser removido: ")

    if titulo in biblioteca:
        del biblioteca[titulo]
        print("Livro removido com sucesso!")
    else:
        print("Erro: livro não encontrado.")


def atualizar_quantidade():
    titulo = input("Digite o título do livro: ")

    if titulo in biblioteca:
        try:
            nova_quantidade = int(input("Digite a nova quantidade de exemplares: "))

            biblioteca[titulo]["quantidade"] = nova_quantidade

            print("Quantidade atualizada com sucesso!")

        except ValueError:
            print("Erro: a quantidade deve ser um número inteiro.")
    else:
        print("Erro: livro não encontrado.")


def registrar_emprestimo():
    titulo = input("Digite o título do livro: ")

    if titulo in biblioteca:
        try:
            quantidade_emprestada = int(input("Digite a quantidade de exemplares a ser emprestada: "))

            quantidade_disponivel = biblioteca[titulo]["quantidade"]

            if quantidade_emprestada <= quantidade_disponivel:
                biblioteca[titulo]["quantidade"] -= quantidade_emprestada

                historico_emprestimos.append({
                    "titulo": titulo,
                    "quantidade": quantidade_emprestada
                })

                print("Empréstimo registrado com sucesso!")
            else:
                print("Erro: exemplares insuficientes disponíveis.")

        except ValueError:
            print("Erro: a quantidade deve ser um número inteiro.")
    else:
        print("Erro: livro não encontrado.")


def exibir_historico():
    if not historico_emprestimos:
        print("Nenhum empréstimo registrado.")
    else:
        print("\nHistórico de empréstimos:")

        for emprestimo in historico_emprestimos:
            print(
                f"{emprestimo['titulo']} - "
                f"{emprestimo['quantidade']} exemplar(es) emprestado(s)"
            )


while True:
    print("\n===== MENU =====")
    print("1 - Adicionar livro")
    print("2 - Listar livros")
    print("3 - Remover livro")
    print("4 - Atualizar quantidade de livros")
    print("5 - Registrar empréstimo")
    print("6 - Exibir histórico de empréstimos")
    print("7 - Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        adicionar_livro()
    elif opcao == "2":
        listar_livros()
    elif opcao == "3":
        remover_livro()
    elif opcao == "4":
        atualizar_quantidade()
    elif opcao == "5":
        registrar_emprestimo()
    elif opcao == "6":
        exibir_historico()
    elif opcao == "7":
        print("Programa encerrado.")
        break

    else:
        print("Opção inválida. Favor tentar novamente.")