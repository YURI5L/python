
def adicao(a, b):
    return a + b


def subtracao(a, b):
    return a - b


def multiplicacao(a, b):
    return a * b


def divisao(a, b):
    if b != 0:
        return a / b
    else:
        return "Divisão por zero não é permitida."


num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))


print(f"\n{num1} + {num2} = {adicao(num1, num2)}")
print(f"{num1} - {num2} = {subtracao(num1, num2)}")
print(f"{num1} * {num2} = {multiplicacao(num1, num2)}")
print(f"{num1} / {num2} = {divisao(num1, num2)}")
