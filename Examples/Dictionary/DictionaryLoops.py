aluno = {'nome': 'Ana', 'idade': 16, 'nota_final': 'A', 'aprovacao': True}

# for x in aluno: == keys
#     print(x)


for x in aluno.values():
    print(x)


for keys, values in aluno.items():
    print(keys, values)