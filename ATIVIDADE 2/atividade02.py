# Inicializando uma lista vazia para armazenar os países
paises = []

# Pedindo ao usuário para informar o nome de 5 países
for i in range(5):
    pais = input(f"Informe o nome do {i + 1}º país: ")
    paises.append(pais)  # Adicionando o nome do país à lista

# Mostrando a lista de países preenchida
print("\nLista de países:")
for pais in paises:
    print(pais)
