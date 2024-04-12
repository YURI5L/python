
numeros = []
for i in range(10):
    num = int(input(f"Digite o {i + 1}º número inteiro: "))
    numeros.append(num)

soma = sum(numeros)


media = soma / len(numeros)


print(f"\nSoma dos números: {soma}")
print(f"Média dos números: {media:.2f}")
