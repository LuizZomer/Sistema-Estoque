from time import sleep

def titulo(msg):
    print('='*40)
    print(f'{msg:^40}')
    print('='*40)


def menu():
    titulo('estoque')
    print('1 - visualizar estoque\n2 - cadastrar produtos\n3 - apagar produtos\n4 = Sair do programa')
    while True:
        try:
            opcaotxt = input('Escolha uma opção: ')
            opcao = int(opcaotxt)
            return opcao
        except ValueError:
            print('Valor invalido')
            sleep(1)


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
    print(f'Em que ordem deseja mostrar o {var}?\n1 - Crescente\n2 - Decrescente')
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


def adicionar():
    produto = {}
    produto.clear()
    titulo('Cadastro de produtos')
    produto['nome'] = input('Nome do produto: ')
    while True:
        try:
            produto['preco'] = float(input('Preço do produto: '))
            break
        except (ValueError, TypeError):
            print('Impossivel anexar esse preço ao produto')
    print(f'O produto {produto["nome"]} foi cadastrado com sucesso.')
    return produto


def deletar(estoque):
    while True:
        if len(estoque) == 1: 
            print(f'0 é o unico numero disponivel')
        else:
            print(f'Os numeros disponiveis são de 0 a {len(estoque)-1}')
        try:
            deletartxt = input('Escolha o numero do produto para excluir: ')
            deletar = int(deletartxt)
            if deletar > len(estoque)-1:
                print('Numero inxistente')
            else:
                return deletar
        except ValueError:
            print('Valor incorreto')
        
