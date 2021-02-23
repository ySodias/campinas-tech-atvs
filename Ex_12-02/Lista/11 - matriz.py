matriz = [['0', '1', '2', '3', '4', '5', '6', '7', '8', '9'], ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9'], ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9'], ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9'], ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9'], ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9'], ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9'], ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9'], ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9'], ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']]

busca = input("Qual número deseja buscar na matriz? ")
i = 0
j = 0
isencontrado = False
controle = False
controle_busca = int(busca)
if controle_busca > 9:
  controle = True

for l in matriz:
    for c in l:
        if busca == c:
          print(f"encontrou o {c} em ({i},{j})") 
        j += 1
    if isencontrado:
      break
    i += 1
    j = 0

if (isencontrado == False) and (controle == True):
  print("Dados não encontrado")