lista_contatos = []
lista_vazia = []
lista_menu = ["0 - Sair", "1 - Inserir contato", "2 - Excluir contato", "3 - Ver contatos"]

while True:
  for menu in lista_menu:
    print(f"{menu}")
  insert_usuario = input("Selecione uma opção para prosseguir: \n")
  if insert_usuario.isnumeric():
    if insert_usuario == '1':
      nome_contato = input("Digite o nome do contato \n")
      ddd_contato = input("Digite o DDD do contato \n")
      telefone_contato = input("Digite o nome do telefone \n")
      if ddd_contato.isnumeric():
        if len(ddd_contato) == 3 or len(ddd_contato) == 2:
          if telefone_contato.isnumeric():
            if len(telefone_contato) == 9:
              endereco_contato = input("Digite o nome do endereco \n")
              contato_salvo = (nome_contato + " - " + "(" + ddd_contato +") " + telefone_contato + " - " + endereco_contato)
              lista_contatos.append(contato_salvo)
              print("O contato " + nome_contato + " foi salvo \n")
            else:
              print("Erro! Número inválido \n")
          else:
            print("Erro! Número inválido \n")
      else:
        print("Erro! DDD inválido \n")
    if insert_usuario == '2':
      if lista_vazia == lista_contatos:
        print("Sua lista não possui contatos! \n")
      else:
        while True:
          indice = 0
          for item in lista_contatos:
            print(f"{indice} - {item}")
            indice += 1
          indice_selecionado = input("Qual desses items você deseja excluir? (selecione um número) \n")
          if indice_selecionado.isnumeric():
            indice_selecionado_convertido = int(indice_selecionado)
            if indice_selecionado_convertido in range(0, indice):
              print("Apagando...")
              item_selecionado = lista_contatos.pop(indice_selecionado_convertido)
              print(f"Seu contato {indice} - {item} foi removido")
              break
          else:
            print("Erro!")
            break
    if insert_usuario == '3':
      if lista_vazia == lista_contatos:
        print("Sua lista não possui contatos! \n")
      else:
        print("Os seguintes contatos estão na lista: \n")
        print(f"{lista_contatos}")
    if insert_usuario == '0':
      break
  else:
    print("Erro! Caracteres inválidos \n")
    