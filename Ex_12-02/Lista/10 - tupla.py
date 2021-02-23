a = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20)
print("Busque um valor dentro dessa lista: \n")

print(a)
b = input("Digite qual número deseja buscar: \t")
if b.isnumeric():
  b = int(b)
  if b <= 20:
    c = str(a[b-1])
    print("O valor que você buscou foi "+c)
  else:
    print("Erro! O número não se encontra na lista.")
else:
  print("Erro! Você não digitou um número")