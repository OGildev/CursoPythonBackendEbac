
class Animal: 
    def __init__(self, nome, idade):  
        self.nome = nome  
        self.idade = idade 

    def emitir_som(self):  
        return "O animal emitiu um som genérico."

class Cachorro(Animal):  
    def emitir_som(self):  
        return "O cachorro latiu!" 

class Gato(Animal):  
    def emitir_som(self): 
        return "O gato miou!" 
    
cachorro = Cachorro("Marlin", 1)
gato = Gato("Zequinha", 5)

print(cachorro.emitir_som())
print(gato.emitir_som())