
# Yield serve para salvar um espaço na memória 

def counter_function():
    yield 1
    yield 2
    yield 3


contador = counter_function()

print(next(contador))
print(contador)
print(contador)