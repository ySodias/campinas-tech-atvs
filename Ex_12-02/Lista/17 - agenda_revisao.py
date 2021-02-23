# import

import time

# listas

agenda_revisao = {}
lista_proprietario_veiculo = []
lista_hora_revisao = []
lista_vazia = []

# menu

menus = [ "  Sair","  Inserir modelo para revisão", " Exibir lista de carros"]

# variaveis ou listas auxiliares

indice = 0

# print Menu

for menu in menus:
  print(f'{indice} -) {menu}')
  indice += 1

while True:
  escolha_usuario = input("Digite um número referente a uma das opções acima para prosseguir: \n")

  if escolha_usuario.isnumeric():
    escolha_usuario = int(escolha_usuario)
    if escolha_usuario <= 2:
      if escolha_usuario == 1: # inserção de cadastro de revisão
        while True:
          nome_proprietario = input("Insira seu nome: \t")
          if len(nome_proprietario) >= 2: # verifica os caracteres do nome, para verificar se é um nome/apelido ou apenas uma letra
            modelo_veiculo = input("Insira o modelo do carro: \t")
            if len(modelo_veiculo) >= 3:  # verifica os caracteres do veiculo, para verificar se é um  nome de carro ou apenas uma letra
              ano_veiculo = input("Insira o ano do carro: \t")
              if ano_veiculo.isnumeric():
                data_em_texto = int(time.strftime("%Y"))
                ano_veiculo = int(ano_veiculo)
                if ano_veiculo > 1807 and ano_veiculo <= data_em_texto: # verifica o ano do modelo é um ano válido
                  data_revisão = str(time.strftime("%d/%m/%Y, %H:%M:%S"))
                  print(f'O carro entrou para revisão em {data_revisão}')
                  dados_proprietario = (f'{nome_proprietario} - {modelo_veiculo}')
                  lista_proprietario_veiculo.append(dados_proprietario)

                  controle_exclusao = input("Deseja realizar outro agendamento? (Digite 's' ou 'S' para sair) \n")
                  if len(controle_exclusao) == 1:
                    if controle_exclusao == "n" or controle_exclusao == "N" or controle_exclusao == "S" or controle_exclusao == "s":
                      if controle_exclusao.upper() == "N":
                        print("Saíndo da inserção de receita...")
                        break
                  else:
                    print("Erro! Caracteres inválidos \n")
                else:
                  print("Ano inválido! Modelo muito antigo")
              else:
                print("Ano inválido")
            else:
              print("Dados inválidos")
          else:
            print("Modelo inválido")
      elif escolha_usuario == 2: # visualização de dados do dicionário
          if lista_proprietario_veiculo == lista_vazia: # verificando se existe algo na lista_proprietario_veiculo
              print("Erro! Não há carros agendados\n")
          else:
            for lista in lista_proprietario_veiculo:
                agenda_revisao["Dados proprietario"] = lista
                agenda_revisao["Hora revisão"] = data_revisão
          
          for chave, valor in agenda_revisao.items():
            print(f'{chave} - {valor}')
      else:
        print("Opção Inválida")
    else:
      print("Erro! Opção inválida")
  else:
    print("Erro! Digito inválido")
