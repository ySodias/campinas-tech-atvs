print("Bem vindo a Feira Livre")

lista_frutas = ['maracujá', 'morango', 'maçã', 'laranja', 'banana', 'pera']

print("\n")
indice = 0
for fruta in lista_frutas:
    indice += 1
    print(f"{indice} - {fruta}")


#login
print("\n")
nome = input("Digite seu nome: ")
if nome.isnumeric():
  print("Erro!")
else:
  selecao_fruta = input("Selecione a fruta que deseja: \t")
  if selecao_fruta.isnumeric():
    if selecao_fruta == '1':
      print(f"Obrigado pela compra {nome} de maracujá")
    if selecao_fruta == '2':
      print(f"Obrigado pela compra {nome} de morango")
    if selecao_fruta == '3':
      print(f"Obrigado pela compra {nome} de maçã")
    if selecao_fruta == '4':
      print(f"Obrigado pela compra {nome} de laranja")
    if selecao_fruta == '5':
      print(f"Obrigado pela compra {nome} de banana")
    if selecao_fruta == '6':
      print(f"Obrigado pela compra {nome} de pera")
  else:
    print("Erro!")
  

