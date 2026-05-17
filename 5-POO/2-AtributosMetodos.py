
# Uma classe é um molde.
# Vamos usar esse molde para construir coisas que queremos que tem um mesmo padrão

# HP 
# Tipo do meu Pokemon (Terra, Eletrico, Fogo, etc)
# Quais seus ataques (Choque do trovão)
# Altura
# Peso

# Relembrando funções:

# def mostrar_nome(nome):
#     print(f"Oi meu nome é {nome}")

# mostrar_nome("Gilberto Lima")

class MoldePokemon:
    # Método == Função
    # Método construtor
    # Self tem a responsabilidade de armazenar e manipular essas informações dos atributos
    def __init__(self, nome, hp, tipo, ataque, altura, peso):
        self.nome = nome
        self.hp = hp
        self.tipo = tipo
        self.ataque = ataque
        self.altura = altura
        self.peso = peso
        
    def mostrar_nome_pokemon(self):
        print(f"O nome do pokemnon é: {self.nome}")