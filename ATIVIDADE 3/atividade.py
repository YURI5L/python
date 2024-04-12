import os

fruta = [{'nome':'maça', 'categoria':'Utilitário', 'ativo':False}, 
            {'nome':'banana', 'categoria':'nanica', 'ativo':True},
            {'nome':'maça', 'categoria':'argentina', 'ativo':False}]

def exibirNomePrograma():
    print('frutas do zé :D')

def exibirOpcoes():
    print('1. Cadastrar fruta')
    print('2. Listar fruta')
    print('3. Alternar estado da fruta')
    print('4. Sair\n')

def finalizar():
    exibirSubtitulo('Finalizar app')

def voltarMenuPrincipal():
    input('\nDigite uma tecla para voltar ao menu ')
    main()

def opcaoInvalida():
    print('Opção inválida!\n')
    voltarMenuPrincipal()

def exibirSubtitulo(texto):
    os.system('cls')
    linha = '*' * (len(texto))
    print(linha)
    print(texto)
    print(linha)
    print()

def cadastrarFruta():
    exibirSubtitulo('Cadastro de novas Frutas')
    nomeFruta = input('Digite o nome da fruta a ser cadastrada: ')
    categoria = input(f'Digite a categoria da fruta {nomeFruta}: ')
    dadosFruta = {'nome':nomeFruta, 'categoria':categoria, 'ativo':False}
    fruta.append(dadosFruta)
    print(f'A fruta {nomeFruta} foi cadastrada!')
    voltarMenuPrincipal()

def listarFruta():
    exibirSubtitulo('Listagem de frutas')
    print(f'{'Nome da fruta'.ljust(22)} | {'Categoria'.ljust(20)} | Status')
    for fruta in fruta:
        nomeFruta = fruta['nome']
        categoria = fruta['categoria']
        ativo = 'ativado' if fruta['ativo'] else 'desativado'
        print(f'- {nomeFruta.ljust(20)} | {categoria.ljust(20)} | {ativo}')
    voltarMenuPrincipal()

def alterarFruta():
    exibirSubtitulo('Alterar estado da fruta')
    nomeFruta = input('Digite o nome da fruta que queira alterar o status: ')
    frutaEncontrado = False

    for fruta in fruta:
        if nomeFruta == fruta['nome']:
            frutaEncontrado = True
            fruta['ativo'] = not fruta['ativo']
            mensagem = f'A fruta {nomeFruta} foi ativado com sucesso' if fruta['ativo'] else f'A fruta {nomeFruta} foi desativado com sucesso'
            print(mensagem)
            
    if not frutaEncontrado:
        print('A fruta não foi encontrado')
            
    voltarMenuPrincipal()

def escolherOpcao():
    try:
        opcaoEscolhida = int(input('Escolha uma opção: '))
        if opcaoEscolhida == 1: 
            cadastrarFruta()
        elif opcaoEscolhida == 2: 
            listarFruta()
        elif opcaoEscolhida == 3: 
            alterarFruta()
        elif opcaoEscolhida == 4: 
            finalizar()
        else: 
            opcaoInvalida()
    except:
        opcaoInvalida()

def main():
    os.system('cls')
    exibirNomePrograma()
    exibirOpcoes()
    escolherOpcao()

if __name__ == '__main__':
    main()

