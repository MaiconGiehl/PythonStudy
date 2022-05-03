# Parametro ==> Argumento
# Default = Aquele que você define o valor no parametro (Sempre no início)
# Non-Default = Aquele que você não define o valor no parâmetro (Sempre no final)


def boas_vindas(quantidade, nome='Maicao'):
    print(f'Olá {nome}.')
    print(f'Temos {str(quantidade)} laptops em estoque')


boas_vindas(6)