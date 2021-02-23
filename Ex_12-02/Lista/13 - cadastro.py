print("Bem vindo viajante!")

nome = input("Insira seu nome: ")

if nome.isnumeric():
    print("Erro")
else:
    opcoes = {"Fortaleza": 1166, "Rio de Janeiro": 212, "Curitiba": 633}
    for opcao in opcoes:
        print("{0:20} {1:6.2f}".format(opcao, opcoes[opcao]))

    escolha_cliente = input("Qual sua opção? ")
    if escolha_cliente == '1':
        print("Seu destino é Fortaleza no valor de 1166")
    if escolha_cliente == '2':
        print("Seu destino é Rio de Janeiro no valor de 212")
    if escolha_cliente == '3':
        print("Seu destino é Curitiba no valor de 633")

