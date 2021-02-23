import random

nomeSorteado = input("Digite seu nome: \t")
numero = input("Digite um numero: \t")

sorteio = random.randint(1, 100)
print(sorteio)
if numero.isnumeric():
  if numero == sorteio:
    print("Parabéns" + nomeSorteado + "você ganhou o sorteio")
  else:
    print("Que pena, não foi você o vencedor")
else:
  print("Erro!")