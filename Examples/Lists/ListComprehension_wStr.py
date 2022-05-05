# List Comprehension
    # Mais simples de se escrever
    # Utilizado quando você precisa criar uma nova lista a partir de uma existente
    # [expressao for item in items]


frutas1 = ['abacate', 'banana', 'morango', 'kiwi', 'abacaxi']

# frutas2 = []

# for item in frutas1:
#     if 'n' in item:
#         frutas2.append(item)


# print(frutas2)


frutas2 = [item for item in frutas1 if 'n' in item]
print(frutas2)