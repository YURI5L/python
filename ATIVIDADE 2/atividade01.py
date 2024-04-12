
nomes = []


nomes.append("João")
nomes.append("Maria")
nomes.append("Carlos")
nomes.append("Ana")
nomes.append("Pedro")


print("Lista de nomes:", nomes)


print("Primeiro nome:", nomes[0])


nomes.remove("Carlos")
print("Lista de nomes após remover Carlos:", nomes)


print("Tamanho da lista:", len(nomes))


if "Ana" in nomes:
    print("Ana está na lista.")
else:
    print("Ana não está na lista.")
