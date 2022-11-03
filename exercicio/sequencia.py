from random import randint
lista = [randint(1, 100) for _ in range(100)]

nova_lista = []
for numero in lista:
  if numero > 10:
    nova_lista.append(numero)

nova_lista_2 = [numero for numero in lista if numero > 10]

print(nova_lista)
