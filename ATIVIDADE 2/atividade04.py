
nomes = []

for i in range(5):
    nome = input(f"Informe o {i + 1}º nome: ")
    nomes.append(nome)

print("\nLista de nomes atual:", nomes)

indice = int(input("\nInforme um número entre 0 e 4 para remover o nome da posição correspondente: "))

if indice >= 0 and indice <= 4:
  
    nome_removido = nomes.pop(indice)
    print(f"\nO nome {nome_removido} foi removido da lista.")
   
    print("Lista de nomes atualizada:", nomes)
else:
    print("\nNúmero fora do intervalo válido.")
