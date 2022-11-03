frutas = ["maca", "banana", "pera", "acerola"]

# É uma estrutura de dados Ordenada
maca = frutas[0]
banana = frutas[1]
pera = frutas[2]
# ... e assim por diante

# Intercambiável
print(frutas)
frutas[3] = "abacate"

# Permito valores duplicados
frutas.append("abacate")
print(frutas)

# Permito uma lista multi-valorada
nova_lista = [1, 2, False, 3.0, [], {}, "último elemento"]
print(nova_lista)

# Como pegar o último elemento da lista?
print(nova_lista[-1])

# Como pegar um intervalo específico?
lista_numerica = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(lista_numerica[:-2])
print(lista_numerica[0:-2])

# Compreensão de lista
# Problema, quais são os elementos que contém a letra 'e'? ['maca', 'banana', 'pera', 'abacate', 'abacate']

# Jeito não Pythonico
lista_filtrada = []
for fruta in frutas:
  if "e" in fruta:
    lista_filtrada.append(fruta)

print(lista_filtrada)

# Pythonico
nova_lista_filtrada = [fruta for fruta in frutas if "e" in fruta]
print(nova_lista_filtrada)

nova_lista_numerica = [numero ** 2 for numero in lista_numerica]
print(nova_lista_numerica)


# Tupla

tupla = (1,2)
tupla_com_1_elemento = (1,) # Lembrando que é diferente disso (1)

# Conjunto
sets = {"um", "dois"}
