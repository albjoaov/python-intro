escolha = input("Digite um NÚMERO: ")
print("O tipo escolhido é: ", type(escolha)) # Tipo String

# Realizar o casting:
# int, float, str, bool

como_inteiro = int(escolha)
print("Agora o tipo é: ", type(como_inteiro)) # Tipo Inteiro

# Conhecendo melhor o casting
# 0b1010111 == 87
binary_87 = "0b1010111" # 87 em binário
print("O valor na base 10 é: ", int(binary_87, base=2))

# Também temos a possibilidade de fazer isso para float, str, bool

# Esses são os principais e essencias a serem estudados
# str, int, float, list, tuple, dict, set, bool, None
