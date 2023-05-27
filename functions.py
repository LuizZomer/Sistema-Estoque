from time import sleep

def titulo(msg):
    print('='*40)
    print(f'{msg:^40}')
    print('='*40)


def cabecalho():
    print(f'{"nº":<1} |   {"Nome":^5}  |  {"preço":>1}')


def visualizacao(estoque):
    while True:
        cont = 0
        print('Visualizar por:\n1 - Ordem adicionada\n2 - Nome\n3 - preço\n4 - Voltar')
        filtrotxt = input('Escolha uma opção: ')
        try:
            filtro = int(filtrotxt)
        except (ValueError,TypeError):
            print('Opção não é um numero inteiro')
            sleep(1)
            continue
        if filtro > 4 or filtro < 1:
            print('Opção não existente')
        else:
            match (filtro):
                case 1:
                    cabecalho()
                    for p in estoque:
                        print(f'{cont:<1}  {p["nome"]:^10} {p["preco"]:>5}')
                        cont+=1
                        sleep(0.5)
                case 2:
                    nome_reverso = reverso('nome')
                    cabecalho()
                    ordenada_nome = sorted(estoque, key=lambda produto: produto['nome'], reverse=nome_reverso )
                    for p in ordenada_nome:
                        print(f'{cont:<1}  {p["nome"]:^10} {p["preco"]:>5}')
                        cont+=1
                        sleep(0.5)
                case 3:
                    preco_reverso = reverso('preço')
                    cabecalho()
                    ordenada_preco = sorted(estoque, key=lambda produto: produto['preco'], reverse=preco_reverso)
                    for p in ordenada_preco:
                        print(f'{cont:<1}  {p["nome"]:^10} {p["preco"]:>5}')
                        cont+=1
                        sleep(0.5)
                case 4:
                    sleep(0.5)
                    break


def reverso(var):
    print(f'Deseja mostrar o {var} em ordem crescente\n1 - Sim\n2 - Não')
    while True:
        try:
            escolhatxt = input('Selecione a opção: ')
            escolha = int(escolhatxt) 
            if escolha > 2 or escolha < 1:
                print('Essa opção não existe')
            else:
                if escolha == 1:
                    return False
                return True
        except (ValueError, TypeError):
            print('Esse valor não é um numero inteiro')
