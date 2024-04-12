
datanasc = int(input("Digite o ano de nascimento: "))

ano = 2024

idade = ano - datanasc

print(type(datanasc))



if (idade >= 18):
    print(f"Você tem {idade} anos e já atingiu ou ultrapassou a maioridade.")
else:
    print(f"Você tem {idade} anos e ainda não atingiu a maioridade.")
