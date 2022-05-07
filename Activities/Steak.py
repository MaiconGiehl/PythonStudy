# Desafio com If, Elif, Else

'''
Criar um programa que dependendendo da temperatura (em celsius) do steak
ele retorna o ponto de cozimento em português. O usuário deverá fornecer a temperatura.

Temperaturas - Cozimento
120°F ou 48°C - Rare (Selada)
130°F ou 54°C - Medium rare (Ao ponto para o mal)
140°F ou 60°C - Medium (Ao ponto)
150°F ou 65°C - Medium well (Ao ponto para o bem)
160°F ou 71°C - Well done (Bem passada)
'''

tempCelsius = int(input('Qual a temperatura da carne? '))

if tempCelsius < 48:
    print('Deixe cozinhar por mais algum tempo')
elif tempCelsius in range(48, 53):
    print('Selada')
elif tempCelsius in range(54, 59):
    print('Ao ponto para o mal')
elif tempCelsius in range(60, 64):
    print('Ao ponto')
elif tempCelsius in range(65, 70):
    print('Ao ponto para o bem')
elif tempCelsius >= 71:
    print('Bem passada')
