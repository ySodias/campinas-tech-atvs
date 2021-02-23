from Usuario import Usuario

nome = input("Digite seu nome: ")
lista_emprestimo = []
lista_vazia = []

if nome.isnumeric():
  print("Erro")
else:
    if len(nome) > 1:
      opcoes = ['Crônicas de Nárnia - O sobrinho do mago', 'Crônicas de Nárnia - O Leão a Feiticeira e o guarda-roupa', 'Crônicas de Nárnia - O cavalo e seu menino', 'Crônicas de Nárnia - Príncipe Caspian', 'Crônicas de Nárnia - A viagem do peregrino da alvorada', 'Crônicas de Nárnia - A cadeura de prata', 'Crônicas de Nárnia - A última batalha', 'Coração Selvagem', 'Uma breve história do tempo', 'A teoria de tudo']
      
      while True:
        menus = ["0 -) Sair",
                "1 -) Solicitar empréstimo de livro",
                "2 -) Ver livros emprestados"]
        for menu in menus:
          print(f"{menu}")
        opcao_usuario = input("Escolha uma das opções para prosseguir: \n")
        if opcao_usuario.isnumeric():
          if opcao_usuario == '1':
            indice_livro = 0

            for opcao in opcoes:
                if indice_livro < len(opcao):
                    indice_livro += 1
                    print(f"{indice_livro} - {opcao}")

            escolha_cliente = input("Qual sua opção? \t")
            
            if escolha_cliente.isnumeric():
              escolha_cliente = int(escolha_cliente)
              print(f"O livro escolhido foi {opcoes[escolha_cliente-1]} \n")

              usuario = Usuario(nome=nome,livro=opcoes[escolha_cliente-1])
              lista_emprestimo.append(usuario)
            else:
              print("Erro")
          elif opcao_usuario == '2':
            if lista_emprestimo == lista_vazia:
                print("Nenhum livro foi emprestado")
            else:
              print("Os seguintes livros já foram emprestados: \n")
              for lista in lista_emprestimo:
                print(f"{lista.nome} - {lista.livro}\n")
          elif opcao_usuario == '0':
            break
          else:
            print("Opção não existe")

        else:
          print("Erro")
          break
    else:
      print("Erro! Nome inválido")
