import math

pi = math.pi
r = input("Insira o raio do círculo: ")

if r.isnumeric():
  r = float(r)
  a = str("%.2f" % (pi*(r*r)))
  p = str("%.2f" % (2*pi*r))

  print("A área do círculo é "+a)
  print("E o perimetro é "+p)
else:
  print("Erro!")