
# Desafio: 

# Objetivo: Implementar um programa em Python que gerencia tarefas, permitindo adicionar, listar, remover e marcar tarefas como concluídas, seguindo um menu interativo.
# Estrutura de Dados:
# Use um dicionário para armazenar as tarefas, onde:
# Chave: Nome da tarefa (string)
# Valor: Status (boolean: True para concluída, False para pendente).
# Funções a Serem Implementadas:
# adicionar_tarefa(tarefas):
# Solicita o nome da tarefa via input().
# Verifica se já existe no dicionário.
# Se existir: Exibe "Essa tarefa já existe.".
# Se não existir: Adiciona com status False e exibe "Tarefa '{nome}' adicionada com sucesso!".
# listar_tarefas(tarefas):
# Se não houver tarefas: Exibe "Nenhuma tarefa cadastrada.".
# Se houver: Lista todas em ordem alfabética, com emojis:
# ✅ Concluída para True.
# ❌ Não concluída para False.
# remover_tarefa(tarefas):
# Solicita o nome da tarefa via input().
# Se existir: Remove e exibe "Tarefa '{nome}' removida com sucesso!".
# Se não existir: Exibe "Erro: Tarefa não encontrada.".
# marcar_concluida(tarefas):
# Solicita o nome da tarefa via input().
# Se existir: Atualiza status para True e exibe "Tarefa '{nome}' marcada como concluída!".
# Se não existir: Exibe "Erro: Tarefa não encontrada.".
# exibir_menu():
# Exibe o menu formatado:
# Menu:  
# 1 - Adicionar tarefa  
# 2 - Listar tarefas  
# 3 - Remover tarefa  
# 4 - Marcar tarefa como concluída  
# 5 - Sair  
# Função Principal (main):
# Inicializa o dicionário tarefas = {}.
# Loop infinito que:
# Exibe o menu.
# Solicita uma opção via input().
# Executa a função correspondente à opção:
# Opções 1-4: Chamam as funções acima.
# Opção 5: Exibe "Saindo do programa..." e encerra o loop.
# Trata opções inválidas com "Opção inválida. Tente novamente.".

# Variável global de tarefas
tarefas = {}

def adicionar_tarefa(nome):
    global tarefas
    if nome in tarefas:
        return "Essa tarefa já existe."
    else:
        tarefas[nome] = False
        return f"Tarefa '{nome}' adicionada com sucesso!!"

def listar_tarefas(_=None):
    if not tarefas:
        return "Nenhuma tarefa cadastrada."
    else:
        resultado = []
        for nome, status in sorted(tarefas.items(), key=lambda item: item[0]):
            status_str = "✅ Concluída" if status else "❌ Não concluída"
            resultado.append(f"{nome}: {status_str}")
        return "\n".join(resultado)

def remover_tarefa(nome):
    global tarefas
    if nome in tarefas:
        del tarefas[nome]
        return f"Tarefa '{nome}' removida com sucesso!"
    else:
        return "Erro: Tarefa não encontrada."

def marcar_concluida(nome):
    global tarefas
    if nome in tarefas:
        tarefas[nome] = True
        return f"Tarefa '{nome}' marcada como concluída!"
    else:
        return "Erro: Tarefa não encontrada."

def exibir_menu():
    return (
        "Menu:\n"
        "1 - Adicionar tarefa\n"
        "2 - Listar tarefas\n"
        "3 - Remover tarefa\n"
        "4 - Marcar tarefa como concluída\n"
        "5 - Sair"
    )

def main():
    while True:
        print(exibir_menu())
        opcao = input("Escolha uma opção: ").strip()

        if opcao == "1":
            nome = input("Digite o nome da tarefa: ")
            print(adicionar_tarefa(nome))
        elif opcao == "2":
            print(listar_tarefas())
        elif opcao == "3":
            nome = input("Digite o nome da tarefa: ")
            print(remover_tarefa(nome))
        elif opcao == "4":
            nome = input("Digite o nome da tarefa: ")
            print(marcar_concluida(nome))
        elif opcao == "5":
            print("Saindo do programa...")
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()