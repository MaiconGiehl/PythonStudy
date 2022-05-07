# Criar a class
class Funcionarios:

    def __init__(self, nome, sobrenome, data_nascimento):
        self.nome = nome
        self.sobrenome = sobrenome
        self.data_nascimento = data_nascimento


# Criar o objeto
usuario1 = Funcionarios('Helena', 'Cabral', '12/01/2009')
usuario2 = Funcionarios('Carol', 'Silva', '15/10/2005')
usuario3 = Funcionarios('José', 'Abreu', '12/08/2003')

# View
print(usuario1.nome)
print(usuario2.nome)
print(usuario3.sobrenome)