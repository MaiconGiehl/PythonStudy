from turtle import sety


s1 = {1, 2, 3, 4, 5, 6}
# Não fazer  s1 = {}

s1.add(4)
s1.update([6, 7, 8, 9, 10])
s1.remove(10)

s1.remove(90) # = error
s1.discard(90) # = ok

# print(list1)
print(s1)


