number = []
number.append(int(input("Digite o primeiro número: \t")))
number.append(int(input("Digite o segundo número: \t")))
number.append(int(input("Digite o terceiro número: \t")))
number.append(int(input("Digite o quarto número: \t")))

soma_number = 0

for x in number:
  soma_number += x
  
print (soma_number/len(number))