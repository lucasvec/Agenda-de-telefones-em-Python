def mostrarMenu():
    global escolha_menu
    print('-- MENU -- ')
    print('1 - Adicionar contato.')
    print('2 - Editar número de um contato existente.')
    print('3 - Excluir número de contato existente.')
    print('4 - Excluir contato.')
    print('5 - Mostrar agenda.')
    escolha_menu = int(input('R: '))

def pegarInformacoes():
    global quantidade_telefone
    global dados
    global numeros
    numeros = []
    dados = {}
    dados['nome'] = str(input('Nome: '))
    quantidade_telefone = int(input('Quantos números você irá adicionar: '))

def incluirNovoTel(dados, numeros, quantidade_telefone, agenda):
    for i in range(0, quantidade_telefone):
        telefone = int(input('Número de telefone: '))
        numeros.append(telefone)
        dados['numero'] = numeros
    agenda.append(dados)

def incluirTel(dados, numeros):
    nome_existente = str(input('Nome: '))
    for i in agenda:
        for k, v in i.items():
            if nome_existente == v:
                print('O nome tem, vamos adicionar um novo número.')
                novo_numero = int(input('Novo número: '))
                
                k.append(novo_numero)

agenda = []

while True:
    mostrarMenu()
    if escolha_menu == 1:
        pegarInformacoes()
        incluirNovoTel(dados, numeros, quantidade_telefone, agenda)
    elif escolha_menu == 2:
        incluirTel(dados, numeros)
    elif escolha_menu == 5:
        print(agenda)
        break