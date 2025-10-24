print('''
█▀ ▄▀█ █▄▄ █▀█ █▀█   █▀▀ ▀▄▀ █▀▄▀█ █▀█ █▀█ █▀▀ █▀ █▀
▄█ █▀█ █▄█ █▄█ █▀▄   ██▄ █░█ █░▀░█ █▀▀ █▀▄ ██▄ ▄█ ▄█\n''')

print('1. Cadastrar Restaurantes')
print('2. Listar Restaurantes')
print('3. Ativar Restaurantes')
print('4. Sair\n')

opcao_escolhida = int(input('Escolha uma opcão: '))

match opcao_escolhida:
    case 1:
        print('Cadastrar Restaurantes')
    case 2:
        print('Listar Restaurantes')
    case 3:
        print('Ativar Restaurantes')
    case 4:
        print('Encerrando o programa')
    case _:
        print('Opção inválida')