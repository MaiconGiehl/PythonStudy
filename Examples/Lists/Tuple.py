# Tuples
    # Armazenar mais de uma informação em variáveis
    # Manter a sequência dos dados em uma variável
    # Não podem ser alteradas (Immutable)

cores_list = ['amarelo', 'verde', 'azul', 'vermelho']
cores_tuple = ('amarelo', 'verde', 'azul', 'vermelho')

print(type(cores_list))
print(type(cores_tuple))

duas_listas = cores_list * 2
duas_tuple = cores_tuple * 2
print(duas_listas)
print(duas_tuple)

cores_list.append('Roxo')
print(cores_list)

# cores_tuple.append('Roxo')
# print(cores_list) ======== Worthless


# Usar tuples para armazenamentos maiores e para valores imutáveis