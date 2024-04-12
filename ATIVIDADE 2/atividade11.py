
def exibir_menu():
    print("Menu:")
    print("1 - Hello World")
    print("2 - Início da programação em Python")
    print("3 - Modularização com Python")
    
   
    escolha = input("Escolha uma opção: ")
    return escolha


while True:
    opcao = exibir_menu()

    if opcao == '1':
        print("Hello World")
        break
    elif opcao == '2':
        print("Início da programação em Python")
        break
    elif opcao == '3':
        print("Modularização com Python")
        break
    else:
        print("Opção inválida. Tente novamente.\n")
