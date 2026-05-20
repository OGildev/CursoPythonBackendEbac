

# Retorne a media de todos os salarios, com exceção do maior e menor

array_salary = [4000,3000,1000,2000]

# Ordenando o array através da função sorted()
new_array = sorted(array_salary)

new_array.remove(new_array[0])
new_array.remove(new_array[-1])

print(new_array)

media = 0

for salario in new_array:
    media += salario

print(media // len(new_array))