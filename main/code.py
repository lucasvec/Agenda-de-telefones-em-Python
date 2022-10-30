import time

def mostrarMenu():
    global escolha_menu
    print('-- MENU -- ')
    print('0 - Mostrar agenda.')
    print('1 - Adicionar contato.')
    print('2 - Adicionar número em contato existente.')

    while True:
        escolha_menu = int(input('R: '))
        if escolha_menu >= 0 or escolha_menu <= 2:
            print('\n')
            break
        else:
            print('Erro! Escolha as opções válidas.')
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
                print(f'{k.title()} - {v}')
        print('\n')


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