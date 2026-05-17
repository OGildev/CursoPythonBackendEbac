
# Decorator é um acessório para uma função que adiciona passos / tratativas na função principal.

# Glossário:

# Decoradores
# Ferramentas que permitem adicionar funcionalidades ou modificar o comportamento de funções de maneira flexível e reutilizável, enriquecendo o código.

def decorator(func):
    def wrapper():
        print("Antes da execução minha função!")
        func()
        print("Depois da execução da minha função!")
    return wrapper

@decorator
def despedida():
    print("Adeus, meu mano. Arrivederte.")

@decorator
def chegada():
    print("Salve! Salvado, meu mano.")

chegada()
despedida()