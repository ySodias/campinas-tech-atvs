"""
  Programa criado para compensação de ausência
"""

from Receita import Receita
import time


nome_usuario = input("Digite seu nome: \t")

menu_opcoes = [" Sair", " Incluir Receita", " Ver Receitas", " Apagar Receita"]
lista_receitas = []
lista_vazia = []
while True:
  indice = 0
  for menu_opcao in menu_opcoes:
    print(f'{indice} - {menu_opcao}')
    indice += 1

  print("\n")

  selecao_usuario = input("Digite um número dentre as opções para prosseguir: \n")
  if selecao_usuario.isnumeric():
    if selecao_usuario == '0': # Sair
      print("Saindo do programa...")
      break
    if selecao_usuario == '1': # Incluir Receita
      while True:
        nome_receita = input("Digite o nome da receita: \n")
        if nome_receita.isnumeric():
          print("Erro! Nome inválido")
        else:
          if len(nome_receita) > 2:
            rendimento = input("Qual o rendimento da receita? \n")
            if rendimento.isnumeric():
              hora_cadastro = str(time.strftime("%d/%m/%Y, %H:%M:%S"))
              

              cadastro_receita = Receita(nome= nome_receita, rendimento=rendimento, hora_cadastro=hora_cadastro)
              lista_receitas.append(cadastro_receita)
              print(f'A receita {cadastro_receita.nome} foi cadastrada...')
              controle_exclusao = input("Deseja sair da inserção? (Digite 's' ou 'S' para sair) \n")
              if len(controle_exclusao) == 1:
                if controle_exclusao == "n" or controle_exclusao == "N" or controle_exclusao == "S" or controle_exclusao == "s":
                  if controle_exclusao.upper() == "S":
                    print("Saíndo da inserção de receita...")
                    break
            else:
              print("Erro! Caracteres inválidos \n")
          else:
            print("Erro! Nome muito pequeno \n")

    if selecao_usuario == '2': # Ver Receitas
      print("As seguintes receitas estão cadastradas: \n")
      indice = 0
      for lista in lista_receitas:
        indice += 1
        print(f'{indice} - {lista.nome} - rende {lista.rendimento} porções, cadastrada em {lista.hora_cadastro}')
      controle_exclusao = input("Deseja sair da lista de receita? (Digite 's' ou 'S' para sair) \n")
      if len(controle_exclusao) == 1:
          if controle_exclusao == "n" or controle_exclusao == "N" or controle_exclusao == "S" or controle_exclusao == "s":
            if controle_exclusao.upper() == "S":
              print("Saíndo da lista de receita...")
              break
      
    if selecao_usuario == '3': # Apagar Receita
      if lista_receitas != lista_vazia:
        while True:
              iterador_receita = 0
              max_receita = len(lista_receitas)
              while iterador_receita < max_receita: #Outra forma de fazer loop em lista
                a = iterador_receita+1
                print(f"{a} - {lista_receitas[iterador_receita].nome}")
                iterador_receita += 1
                  
              input_usuario = input("Digite um valor para a exclusão de receita \n")
              if input_usuario.isnumeric():
                  receita_selecionada = (int(input_usuario) - 1) #Solicite para o usuário o índice
                  if receita_selecionada in range(0, max_receita):
                      receita_excluida = lista_receitas.pop(receita_selecionada) #pop para excluir o professor e retornar o objeto excluído
                      print(f"A receita {receita_excluida.nome} foi excluído") #mostra para o usuário
                      #Solicitando a saída para o usuário    
                      controle_exclusao = input("Deseja sair da exclusão? (Digite 's' ou 'S' para sair) \n")
              if len(controle_exclusao) == 1:
                if controle_exclusao == "n" or controle_exclusao == "N" or controle_exclusao == "S" or controle_exclusao == "s":
                  if controle_exclusao.upper() == "S":
                    print("Saíndo da exclusão de receita...")
                    break
      else:
        print("Não existe receita cadastrada")  
  else:
    print("Erro! Número inválido")