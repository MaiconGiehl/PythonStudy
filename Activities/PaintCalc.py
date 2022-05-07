# Desafio com Funções

'''
Criar um programa que calcula a quantidade de tinta necessária para
pintar uma parede. O usuário deverá fornecer as seguintes
informações: Rendimento, altura e largura.
O programa deve mostrar na tela a mensagem 'Você necessita de x
latas de tinta'
'''


def qtdNecessaria (rendimento, altura, largura):
    return f'Você precisa de {altura * largura / rendimento} litros de tinta'


rendimento = int(input('Qual é o rendimento da lata de tinta?'))
altura = int(input('Qual é a altura da parede?'))
largura = int(input('Qual é a largura da parede?'))

print(qtdNecessaria(rendimento, altura, largura))