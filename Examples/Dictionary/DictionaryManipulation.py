
aluno = {'nome': 'Ana', 'idade': 16, 'nota_final': 'A', 'aprovacao': True}

# aluno.update({'nome': 'Jose', 'nota_final': 'B'})

print(aluno.get('endereco', 'Não existe'))

aluno.update({'endereco': 'Rua A'})
print(aluno.get('endereco', 'Não existe'))

del aluno['idade']
print(aluno)