
def imprimir_lista(lista):
    print("\nLista completa:")
    for nome in lista:
        print(nome)


def adicionar_nome(lista):
    nome = input("\nDigite um nome para adicionar à lista: ")
    lista.append(nome)
    print(f"\n'{nome}' foi adicionado à lista.")


def pesquisar_nome(lista):
    nome_pesquisado = input("\nDigite o nome que deseja pesquisar na lista: ")
    if nome_pesquisado in lista:
        print(f"\n'{nome_pesquisado}' está na lista.")
    else:
        print(f"\n'{nome_pesquisado}' não está na lista.")


lista_nomes = []

for i in range(5):
    nome = input(f"Digite o {i + 1}º nome: ")
    lista_nomes.append(nome)


while True:
    print("\nMenu:")
    print("1 - Imprimir lista completa")
    print("2 - Adicionar nome à lista")
    print("3 - Pesquisar nome na lista")
    print("4 - Sair")

    opcao = input("\nEscolha uma opção: ")

    if opcao == '1':
        imprimir_lista(lista_nomes)
    elif opcao == '2':
        adicionar_nome(lista_nomes)
    elif opcao == '3':
        pesquisar_nome(lista_nomes)
    elif opcao == '4':
        print("\nEncerrando o programa. Até mais!")
        break
    else:
        print("\nOpção inválida. Tente novamente.")
