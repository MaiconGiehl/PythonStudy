try:
    valor = int(input('Digite o valor do seu produto: '))
    print(valor)
except ValueError:
    print('Favor digitar um valor em números')
else:
    print('Usuário digitou um valor correto')
    resultado = valor * 2
    print(resultado)
finally:
    print('codigo ok')

print('Mais codigo abaixo')