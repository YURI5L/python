
numeros = []


for i in range(10):
    numero = int(input(f"Informe o {i + 1}º número: "))
    
    
    if numero % 2 == 0:
        numero += 100
    
    
    numeros.append(numero)


print("\nNúmeros digitados:")
for num in numeros:
    print(num)
