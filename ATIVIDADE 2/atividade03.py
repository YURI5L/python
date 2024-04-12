# Inicializando uma lista com números inteiros
numeros = [10, 20, 30, 40, 50]

# Solicitando que o usuário informe um número
numero_usuario = int(input("Informe um número inteiro: "))

# Verificando se o número está na lista
if numero_usuario in numeros:
    print(f"O número {numero_usuario} está na lista.")
else:
    print(f"O número {numero_usuario} não está na lista.")
