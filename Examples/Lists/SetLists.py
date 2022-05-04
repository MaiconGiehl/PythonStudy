# Set (listas)
    # Similar à listas
    # Evita itens duplicados
    # Não utiliza index

list1 = [10, 20, 30, 40, 50]
list2 = [10, 20, 60, 70]

num1 = set(list1)
num2 = set(list2)

print(num1 | num2) 
# | = Union, união retirando os repetidos

print(num1 - num2)
# - = Difference, mostra os valores em que o num1 se diferencia do num2

print(num1 ^ num2)
# ^ Symmetric Difference, retira os duplicados em ambas as listas

print(num1 & num2)
# & = And = mostra os duplicados

print(len(num1)) # = print(num1[0]) (set perde o index)