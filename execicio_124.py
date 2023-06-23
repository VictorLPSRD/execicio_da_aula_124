perguntas = [
   {
        'Pergunta': 'Quanto é 2+2?',
        'Opções': ['1', '3', '4', '5'],
        'Resposta': '4',
    },
    {
        'Pergunta': 'Quanto é 5*5?',
        'Opções': ['25', '55', '10', '51'],
        'Resposta': '25',
    },
    {
        'Pergunta': 'Quanto é 10/2?',
        'Opções': ['4', '5', '2', '1'],
        'Resposta': '5',
    },
]

qtd_acertos = 0 # A quantidade de perguntas começa com zero.
for pergunta in perguntas: # pegando todas as perguntas do dicionário.
    print('Pergunta:', pergunta['Pergunta']) # exibindo todos as perguntas do dicionário.
    print()# spaços entre as perguntas 

    opcoes = pergunta['Opções'] 
    for i, opcao in enumerate(opcoes): # pegando todas as resposta e enumerando ela (i).
        print(f'{i})', opcao) 
    print()

    escolha = input('Escolha uma opção: ') # pegando a resposta do usuario  ele sempre vai para no input .

    acertou = False # O acerto começa com False .
    escolha_int = None #  A escolha começa como None.
    qtd_opcoes = len(opcoes) # Pegando a quantidade de opçoes por pergunta .

    if escolha.isdigit(): # O isdigiti serve para verificar se oq o usuario colocou é um digito  .
        escolha_int = int(escolha) # Se oq o usuario digitou não for um digito ele vai ser convertido .

    if escolha_int is not None: #  Se a escolha do usuario não for None ele cair aq.
        if escolha_int >= 0 and escolha_int < qtd_opcoes: # se a escolha_int for maior igual que zero e ecolha_int for meno que qtd_opocoes 
            if opcoes[escolha_int] == pergunta['Resposta']:# Se opçoes com a ecolha_int  for igual a pergunya com a resposta certa .
                acertou = True # A escolha que era False vai se torna True.

    print()
    if acertou: # Se acertou  
        qtd_acertos += 1 # vai somar a quantidade de acertos 
        print('Acertou') # e vai exibir Acertou 
    else: # se não ele vai qxibir 
        print('Errou') # isso

    print()


print('Você acertou', qtd_acertos)
print('de', len(perguntas), 'perguntas.')
