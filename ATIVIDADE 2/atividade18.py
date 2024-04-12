
def encontrar_maior(lista):
    return max(lista)

def dobro(numero):
    return numero * 2

numeros = []
for i in range(4):
    num = float(input(f"Digite o {i + 1}º número: "))
    numeros.append(num)


maior_numero = encontrar_maior(numeros)


resultado = dobro(maior_numero)
print(f"O dobro do maior número ({maior_numero}) é {resultado}.")
