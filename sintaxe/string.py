string_normal = "Olá, Mundo!"
string_multiline = """
Olá, Mundo!

Continuacao
Continuacao
Continuacao
Continuacao
Continuacao
Continuacao
"""

print(string_multiline)

# String é um iteravel

for letra in string_normal:
  print(letra)

# Ver concatenacao no arquivo concatenacao.py
# Lá temos f-string, concatenacao normal e usando o print

ultima_letra = string_normal[-1]
