# map, filter, reduce

lista = [1, 2, 3, 4, 5, 6]
# Quero = [2, 4, 6, 8, 10, 12]

# map(funcao, iteravel)

def dobro(numero):
  return numero * 2

nova_lista = map(dobro, lista)
print(list(nova_lista))


######

# filter(funcao, iteravel)
def menor_que_4(numero):
  return numero < 4

filter(menor_que_4, lista)
