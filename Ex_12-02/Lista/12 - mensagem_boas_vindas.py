import random

print("Bem Vindo")

nome = input("Qual o seu nome? \n")

def elogio():

  msm = random.randint(1, 3)
  if msm == 1:
    print("Você é esperto")
  if msm == 2:
    print("Você é um ótimo dev")
  if msm == 3:
   print("Parabéns por ser esforçado")
  return elogio

print("Olá, "+nome)
elogio()
