produtos = ['arroz', 'feijão', 'laranja', 'banana', 5, 6, 7, 8]

# item1 = produtos[0]
# item2 = produtos[1]
# item3 = produtos[2]
# item4 = produtos[3]

# item1, item2, item3, *outros = produtos
item1, item2, *outros, item8 = produtos


print(item1)
print(item2)
print(outros)
print(item8)