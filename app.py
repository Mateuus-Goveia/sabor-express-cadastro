import os

def finalizar_app():
    os.system('cls')
    print('Encerrando o programa\n')

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

def opçao_invalida():
    print('Opção Inválida\n')
    input('Precione enter para voltar ao menu principal')
    main()

def escolher_opcao():
    try:
        opcao_escolhida = int(input('Escolha uma opcão: '))

        match opcao_escolhida:
            case 1:
                print('Cadastrar Restaurantes')
            case 2:
                print('Listar Restaurantes')
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