
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

    def mostrar_altura_pokemon(self):
        print(f"A altura do meu pokemon é: {self.altura}") 

    def mostrar_tipo_pokemon(self):
        print(f"A altura do meu pokemon é: {self.tipo}")

pikachu = MoldePokemon("Pikachu", 400, "Eletrico", "Choque do Trovão", 50, 15)
charizard = MoldePokemon("Lapras", 1000, "Agua", "Gelo do Alasca", 500, 1000)

pikachu.mostrar_nome_pokemon()
charizard.mostrar_nome_pokemon()