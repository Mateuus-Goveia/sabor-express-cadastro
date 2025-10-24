import os

restaurantes = [
    {'nome': 'Casole', 'categoria': 'Pizzaria', 'ativo': False},
    {'nome': 'Praça', 'categoria': 'Japonesa', 'ativo': True},
    {'nome': 'Cantina', 'categoria': 'Mineira', 'ativo': False}
]

def voltar_ao_menu_principal():
    input('\nPrecione enter para voltar ao menu principal')
    main()

def exibir_subtitulo(texto):
    os.system('cls')
    print(texto)
    print()

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
    exibir_subtitulo('Finalizando o programa')

def opçao_invalida():
    print('Opção Inválida\n')

    voltar_ao_menu_principal()

def cadastrar_novo_restaurante():
    exibir_subtitulo('Cadastro de novos restaurantes')

    nome_do_restaurante = input('Digite o nome do restaurante que deseja cadastrar: ')
    categoria = input(f'Digite a nome da categoria do restaurante {nome_do_restaurante}: ')

    dados_do_restaurante = {'nome':nome_do_restaurante, 'categoria':categoria, 'ativo':False}
    restaurantes.append(dados_do_restaurante)

    print(f'O restaurante {nome_do_restaurante} foi cadastrado com sucesso!')

    voltar_ao_menu_principal()

def listar_restaurantes():
    exibir_subtitulo('Listando restaurantes')

    for restaurante in restaurantes:
        nome_restaurante = restaurante['nome']
        categoria = restaurante['categoria']
        ativo = restaurante['ativo']
        print(f'- {nome_restaurante} | {categoria} | {ativo}')

    voltar_ao_menu_principal()

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