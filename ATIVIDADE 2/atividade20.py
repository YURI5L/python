
def maior_de_tres(a, b, c):
    return max(a, b, c)


num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))
num3 = float(input("Digite o terceiro número: "))


maior_numero = maior_de_tres(num1, num2, num3)


print(f"\nO maior número entre {num1}, {num2} e {num3} é {maior_numero}.")
