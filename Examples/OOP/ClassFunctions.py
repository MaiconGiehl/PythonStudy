# Criar a class
class Funcionarios:

    def __init__(self, nome, sobrenome, data_nascimento):
        self.nome = nome
        self.sobrenome = sobrenome
        self.data_nascimento = data_nascimento

    def nome_completo(self):
        return self.nome + ' ' + self.sobrenome


# Criar o objeto
usuario1 = Funcionarios('Helena', 'Cabral', '12/01/2009')
usuario2 = Funcionarios('Carol', 'Silva', '15/10/2005')
usuario3 = Funcionarios('José', 'Abreu', '12/08/2003')

# Print
# print(usuario1.nome + ' ' + usuario1.sobrenome)
# print(usuario1.nome_completo())
print(Funcionarios.nome_completo(usuario1))