from Valor import Valor
from Fruta import Fruta

nome = input("Digite seu nome: ")
lista_compras_frutas = []
lista_compras_valor = []


valor = 0
if nome.isnumeric():
  print("Erro")
else:
  if len(nome) > 1:
    while True:

      fruta1 = Fruta('Maracujá', 9.50)
      fruta2 = Fruta('Morango', 3.00)
      fruta3 = Fruta('Maçã', 7.00)
      fruta4 = Fruta('Laranja', 10.00)
      fruta5 = Fruta('Banana', 4.00)
      fruta6 = Fruta('Pera', 8.00)

      frutas = []

      frutas.append(fruta1)
      frutas.append(fruta2)
      frutas.append(fruta3)
      frutas.append(fruta4)
      frutas.append(fruta5)
      frutas.append(fruta6)
      
      indice= 0
      for fruta in frutas:
        indice += 1
        print(f'{indice} - {fruta.nome} - {fruta.preco}')
        lista_compras_frutas.append(fruta.nome)
        lista_compras_valor.append(fruta.preco)
        
     

        
      escolha_cliente = input("Qual das opções acima vai querer? \n") 
      if escolha_cliente.isnumeric():
        escolha_cliente = int(escolha_cliente)
        print(f"A fruta escolhida {lista_compras_frutas[escolha_cliente-1]} no valor {lista_compras_valor[escolha_cliente-1]} cada\n")
      
      quantidade = input("Quantas irá querer? \n")

      if quantidade.isnumeric():
        quantidade = float(quantidade)
        valor = lista_compras_valor[escolha_cliente-1]*quantidade

        print(f"O valor da sua compra é {valor}")
      
      deseja_mais_alguma_coisa = input("Deseja mais alguma coisa? Digite S(sim) ou N(não)")
      if deseja_mais_alguma_coisa.isnumeric():
        print("Erro! Carácteres inválidos")
      else:
        if deseja_mais_alguma_coisa.upper() == 'SIM' or deseja_mais_alguma_coisa.upper == 'S':
          print("Retomando lista de produtos... \n")
        else:
          break
      
  else:
    print("Erro! Nome inválido")
