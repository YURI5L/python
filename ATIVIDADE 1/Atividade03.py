
nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))
nota3 = float(input("Digite a terceira nota: "))


media = (nota1 + nota2 + nota3) / 3


if media >= 7:
    situacao = "aprovado"
else:
    situacao = "reprovado"

print("A média do aluno é {media:.2f}.")
print("O aluno está {situacao}.")
