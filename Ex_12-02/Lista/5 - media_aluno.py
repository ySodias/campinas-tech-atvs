nomeAluno = input("Digite o nome do Aluno: \t")
notasAluno = []
notasAluno.append(int(input("Digite a nota de matemática: ")))
notasAluno.append(int(input("Digite a nota de português:  ")))
notasAluno.append(int(input("Digite a nota de história: ")))
notasAluno.append(int(input("Digite a nota de física: ")))

media_notasAluno = 0

for somaAluno in notasAluno:
  media_notasAluno += somaAluno
  
media = (media_notasAluno/len(notasAluno))


dadosAluno = {nomeAluno:media}

print(dadosAluno)