numeros = [2, 3, 4, 5]
letras = ['a', 'b', 'c', 'd']

# final = numeros * 2
# final = numeros + letras

numeros.extend(letras)
print(numeros)


itens = [['item1', 'item2'], ['item3', 'item4']]
print(itens[1][1])