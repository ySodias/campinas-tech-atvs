a = input("Digite um número inteiro ")
if a.isnumeric():
  
  antecessor = (int(a)) - 1
  sucessor = (int(a)) + 1

  print("Seu número é "+str(a))
  print("O antecessor desse número é "+str(antecessor))
  print("O sucessor desse número é "+str(sucessor))
else:
  print("Erro!")