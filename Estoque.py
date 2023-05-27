from time import sleep
import functions

estoque = []

while True:
    opcao = functions.menu()
 
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
            delete = functions.deletar(estoque)
            print(f'O produtos {estoque[delete]["nome"]} foi apagado com sucesso')
            estoque.pop(delete)
            sleep(1)
        case 4:
            print('Saindo do programa...')
            break
        case _:
            print('Opção invalida')
            sleep(1)