from Contato import Contato

# Opções
menu =[]
opcoes = ["", "[1] - Mostrar Contatos", "[2] Excluir Contato", "[3] Inserir Contato"]
while True:
  print("Selecione uma das seguintes opções")
  for opcao in opcoes:
    print(opcao)
  selecao = int(input(""))  
  if selecao == 1:
    for contato in menu:
      print(f"O contato do {contato.nome} está agendado")
  elif selecao == 2:
    while True:
      indice = 0
      for item in menu:
        print(f"{indice} - {item.nome} - {item.telefone}")
        indice += 1
      print(f"Selecione {indice} para sair...")
      indice_selecionado = input("Qual desses contatos você deseja excluir? ")
      if indice_selecionado.isnumeric():
          indice_selecionado_convertido = int(indice_selecionado)
          if indice_selecionado_convertido in range(0, indice):
            print("Apagando...")
            item_selecionado = menu.pop(indice_selecionado_convertido)
            print(f"Seu item {item.nome} foi removido")
            break
          elif indice_selecionado_convertido == indice:
            break
          else:
            print("Não existe opção")
      else:
        print("Opção incorreta")
  elif selecao == 3:
# Criação de contato
    nome = input("Digite o nome do contato: \n")
    telefone = input("Digite o telefone: \n") 
    if telefone.isnumeric():  
      endereco = input("Digite o endereço: \n")
      contato = Contato(nome, telefone, endereco)
      menu.append(contato)
      print("Contato adicionado")
    else:
      print("Erro! Você digite alguma informação errada")
  elif opcoes not in (1, 2, 3):
    print("Erro!")

