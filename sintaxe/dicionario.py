carro = {
  "marca": "VW",
  "nome": "Gol",
  "ano": 2020
}

# É ordenado?
# A partir do 3.7
# Antes desssa versão não

for chave, valor in carro.items():
  print(f"O carro tem {chave}: {valor}")
