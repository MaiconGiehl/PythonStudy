
corCliente = input('Digite a cor desejada: ')
cores = ['amarelo', 'verde', 'azul', 'vermelho']

#lower = lower case

if corCliente.lower() in cores:
    print('Em estoque')
else:
    print('Não temos a cor em estoque')