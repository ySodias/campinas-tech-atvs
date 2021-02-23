produtos =  {'Vermelha - Carne bovina': 27.00, 'Azul - Carne Bife de Alcatra': 13.39, 'Amarelo - Pão de queijo': 15.85, 'Laranja -  Coxinha': 5}

usuario = input("Digite seu nome: \n")

print(f"Olá {usuario}! Temos em estoque os seguintes produtos com os respecitvos preços: \n")
while True:
  for produto, preco in produtos.items():
    print(produto, preco)

  compra = input("Deseja comprar alguma coisa? (Selecione o produto baseado em sua cor) \n")
  if compra.isnumeric():
    print("Erro! Digite a cor e não números")
  else:
    vermelho = 'vermelho'
    azul = 'azul'
    amarelo = 'amarelo'
    laranja = 'laranja'
    indice = 0
    if compra.upper() in vermelho.upper():
      for carne_vermelha, valor in produtos.items():
        print(f"Você escolheu {carne_vermelha} no valor de {valor} R$")
        indice += 1
        if indice == 1:
          break
    if compra.upper() in azul.upper():
      for carne_azul, valor in produtos.items():
        indice += 1
        if indice == 2:
          print(f"Você escolheu a cor {carne_azul} no valor de {valor} R$")
          break
    if compra.upper() in amarelo.upper():
      for comida_amarela, valor in produtos.items():
        indice += 1
        if indice == 3:
          print(f"Você escolheu a cor {comida_amarela} no valor de {valor} R$")
          break
    if compra.upper() in laranja.upper():
      for comida_laranja, valor in produtos.items():
        indice += 1
        if indice == 4:
          print(f"Você escolheu a cor {comida_laranja} no valor de {valor} R$")
          break
    comprar_mais = input("Deseja comprar mais alguma coisa? Pressione S para continuar")
    if comprar_mais.isnumeric():
      print("Erro!")
    else:
      if comprar_mais.upper() == 'S':
        break
      if comprar_mais.upper() == 'N':
        print("Fechando sistema...")
  break
    