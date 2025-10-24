import os

restaurantes = ['Pizza', 'Sushi']

def exibir_nome_do_programa():
    print('''
█▀ ▄▀█ █▄▄ █▀█ █▀█   █▀▀ ▀▄▀ █▀▄▀█ █▀█ █▀█ █▀▀ █▀ █▀
▄█ █▀█ █▄█ █▄█ █▀▄   ██▄ █░█ █░▀░█ █▀▀ █▀▄ ██▄ ▄█ ▄█
          ''')

def exibir_opçoes():
    print('1. Cadastrar Restaurantes')
    print('2. Listar Restaurantes')
    print('3. Ativar Restaurantes')
    print('4. Sair\n')

def finalizar_app():
    os.system('cls')
    print('Encerrando o programa\n')

def opçao_invalida():
    print('Opção Inválida\n')
    input('Precione enter para voltar ao menu principal')
    main()

def cadastrar_novo_restaurante():
    os.system('cls')
    print('Cadastro de novos restaurantes.\n')
    nome_do_restaurante = input('Digite o nome do restaurante que deseja cadastrar: ')
    restaurantes.append(nome_do_restaurante)
    print(f'O restaurante {nome_do_restaurante} foi cadastrado com sucesso!')
    input('\nPrecione enter para voltar para o menu principal')
    main()

def listar_restaurantes():
    os.system('cls')
    print('Listando restaurantes\n')
    for restaurante in restaurantes:
        print(f'.{restaurante}')
    input('\nPrecione enter para voltar para o menu principal')
    main()

def escolher_opcao():
    try:
        opcao_escolhida = int(input('Escolha uma opcão: '))

        match opcao_escolhida:
            case 1:
                cadastrar_novo_restaurante()
            case 2:
                listar_restaurantes()
            case 3:
                print('Ativar Restaurantes')
            case 4:
                finalizar_app()
            case _:
                opçao_invalida()
    except:
        opçao_invalida()

def main():
    os.system('cls')
    exibir_nome_do_programa()
    exibir_opçoes()
    escolher_opcao()

if __name__ == '__main__':
    main()