from time import sleep
import functions

estoque = []

while True:
    functions.titulo('estoque')
    print('1 - visualizar estoque\n2 - cadastrar produtos\n3 - apagar produtos\n4 = Sair do programa')
    opcaotxt = input('Escolha uma opção: ')
    try:
        opcao = int(opcaotxt)
    except ValueError:
        print('Valor invalido')
        sleep(1)
        continue    
    match opcao:
        case 1:
            functions.titulo('Visualização do estoque')
            if len(estoque) == 0:
                print('O estoque está vazio')
                sleep(1)
            else:
                functions.visualizacao(estoque)
        case 2:
            produto = functions.adicionar()
            estoque.append(produto.copy())
            sleep(1)
        case 3:
            deletartxt = input('Escolha o numero do produto para excluir: ')
            try:
                deletar = int(deletartxt)
            except ValueError:
                print('Valor incorreto')
            if deletar > len(estoque)-1:
                print('Numero inxistente')
            else:
                print(f'O produtos {estoque[deletar]["nome"]} foi apagado com sucesso')
                estoque.pop(deletar)
                sleep(1)
        case 4:
            print('Saindo do programa...')
            break
        case _:
            print('Opção invalida')
            sleep(1)