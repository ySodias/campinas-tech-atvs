print("Bem vindo Biblioteca!")

nome = input("Insira seu nome: ")

if nome.isnumeric():
    print("Erro")
else:
    opcoes = ['Crônicas de Nárnia - O sobrinho do mago', 'Crônicas de Nárnia - O Leão a Feiticeira e o guarda-roupa', 'Crônicas de Nárnia - O cavalo e seu menino', 'Crônicas de Nárnia - Príncipe Caspian', 'Crônicas de Nárnia - A viagem do peregrino da alvorada', 'Crônicas de Nárnia - A cadeura de prata', 'Crônicas de Nárnia - A última batalha', 'Coração Selvagem', 'Uma breve história do tempo', 'A teoria de tudo']
    
    indice_livro = 0

    for opcao in opcoes:
        if indice_livro < len(opcao):
            indice_livro += 1
            print(f"{indice_livro} - {opcao}")

    escolha_cliente = input("Qual sua opção? ")
    if escolha_cliente == '1':
        print("O livro escolhido foi Crônicas de Nárnia - O sobrinho do mago")
    elif escolha_cliente == '2':
        print("O livro escolhido foi Crônicas de Nárnia - O Leão a Feiticeira e o guarda-roupa")
    elif escolha_cliente == '3':
        print("O livro escolhido foi rônicas de Nárnia - O cavalo e seu menino")
    elif escolha_cliente == '4':
        print("O livro escolhido foi Crônicas de Nárnia - Príncipe Caspian")
    elif escolha_cliente == '5':
        print("O livro escolhido foi Crônicas de Nárnia - A viagem do peregrino da alvorada")
    elif escolha_cliente == '6':
        print("O livro escolhido foi Crônicas de Nárnia - A cadeura de prata")
    elif escolha_cliente == '7':
        print("O livro escolhido foi Crônicas de Nárnia - A última batalha")
    elif escolha_cliente == '8':
        print("O livro escolhido foi Coração Selvagem")
    elif escolha_cliente == '9':
        print("O livro escolhido foi Uma breve história do tempo")
    elif escolha_cliente == '10':
        print("O livro escolhido foi A teoria de tudo")
