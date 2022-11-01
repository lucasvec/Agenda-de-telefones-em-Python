import time

def mostrarMenu():
    global escolha_menu
    print('')
    print('-- MENU -- ')
    print('0 - Mostrar agenda.')
    print('1 - Adicionar contato.')
    print('2 - Adicionar número em contato existente.')
    print('3 - Excluir número em contato existente')
    print('4 - Excluir contato.')
    print('5 - Sair')


    while True:
        escolha_menu = int(input('R: '))
        if escolha_menu >= 0 or escolha_menu <= 2:
            print('\n')
            break
        else:
            print('Erro! Escolha as opções válidas.')
            print('\n')
            continue


def pegarInformacoes():
    global quantidade_telefone
    global dados
    global numeros
    numeros = []
    dados = {}
    dados['nome'] = str(input('Nome: ')).title()
    quantidade_telefone = int(input('Quantos números você irá adicionar: '))


def incluirNovoTel(dados, numeros, quantidade_telefone, agenda):
    for i in range(0, quantidade_telefone):
        telefone = int(input('Número de telefone: '))
        numeros.append(telefone)
        dados['numero'] = numeros
    agenda.append(dados)


def incluirTel(dados, numeros):
    nome_existente = str(input('Nome: ')).title()
    for i in agenda:
        for k, v in i.items():
            if nome_existente == v:
                print('Vamos adicionar um novo número.')
                novo_numero = int(input('Novo número: '))
                if i['numero']:
                    i['numero'].append(novo_numero)
                    

def mostrarAgenda(agenda):
    if agenda == []:
        print('Não há conteúdo.\n')
    else:
        print('SEUS CONTATOS:')
        for i in agenda:
            for k, v in i.items():
                if len(v) > 0:
                    print(f'{k.title()} - {v}')
        print('\n')


def excluirContato(agenda):
    print('       EXCLUIR CONTATO.')
    contato_excluir = str(input('Nome: ')).title()
    if len(contato_excluir) > 0:
        for i in agenda:
            for k, v in i.items():
                if contato_excluir == v:
                    confirmacao = str(input('Tem certeza? [s/n]\nR: ')).lower()
                    if confirmacao == 's':
                        i['nome'] = ''
                        if i['numero']:
                            i['numero'].clear()
                            print('Contato excluido')

                        
def excluirNumero(agenda):
    print('       EXCLUIR NÚMERO')
    nome_contato = str(input('Nome: ')).title()
    for i in agenda:
        for k, v in i.items():
            if nome_contato == v:
                print(f'Números do {nome_contato}:')
                for num in i['numero']:
                    print(f'- {num}')
                excluir_numero = int(input('Deseja excluir: '))
                confirmacao = str(input('Tem certeza? [s/n]\nR: ')).lower()
                if confirmacao == 's':
                    i['numero'].remove(excluir_numero)
                    print('Número selecionado excluído.')


agenda = []

while True:
    mostrarMenu()
    if escolha_menu == 0:
        mostrarAgenda(agenda)
        time.sleep(2)

    elif escolha_menu == 1:
        pegarInformacoes()
        incluirNovoTel(dados, numeros, quantidade_telefone, agenda)

    elif escolha_menu == 2:
        incluirTel(dados, numeros)

    elif escolha_menu == 3:
        excluirNumero(agenda)

    elif escolha_menu == 4:
        excluirContato(agenda)

    elif escolha_menu == 5:
        print('Encerrando...')
        time.sleep(2)
        print('\x1b[2J')
        break