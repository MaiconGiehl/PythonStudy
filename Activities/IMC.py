# Calculo de IMC - Índice de Massa Corporal

'''
    Qual é altura em cm:
    Qual é o seu peso em kg:
'''

# Menor que 18,5    Magreza
# Entre 18,5 e 24,9 Normal
# Entre 25,0 e 29,9 Sobrepeso
# Entre 30,0 e 39,9 Obesidade
# Maior que 40,0    Obesidade Grave


altura = float(input('Digite sua altura, em centímetros: '))
peso = float(input('Digite seu peso, em quilos: '))

imc = peso / (altura / 100)**2


if imc < 18.5:
    print('Magreza')
elif imc >= 18.5 and imc < 24.9:
    print('Normal')
elif imc >= 25.0 and imc < 29.9:
    print('Sobrepeso')
elif imc >= 30.0 and imc < 39.9:
    print('Obesidade')
else:
    print('Obesidade grave')
