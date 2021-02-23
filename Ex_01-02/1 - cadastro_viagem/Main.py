from Destino import Destino

destino1 = Destino('São Paulo', 200.00)
destino2 = Destino('Curitiba', 180.00)
destino3 = Destino('Rio de Janero', 300.00)

lista_destino = []

lista_destino.append(destino1)
lista_destino.append(destino2)
lista_destino.append(destino3)

info_viajante_nome = input("Qual seu nome?")
if info_viajante_nome.isnumeric():
    print("Erro!")
if len(info_viajante_nome) > 1: 
    while True:

        indice = 0
        for produto in lista_destino:
            indice += 1
            print(f'{indice} - {produto.destino}  no valor de  {produto.preco}')
            if indice == 1:
                destino1 = produto.destino
                preco1 = produto.preco
            if indice == 2:
                destino2 = produto.destino
                preco2 = produto.preco
            if indice == 3:
                destino3 = produto.destino
                preco3 = produto.preco

        opcao = input("Qual destino você deseja ir? \n")
        if opcao.isnumeric():
            if opcao == '1':
                print(f'Você deseja ir para {destino1}? Por {preco1}')
                preco2 = 0
                preco3 = 0
            if opcao == '2':
                print(f'Você deseja ir para {destino2}? Por {preco2}')
                preco1 = 0
                preco3 = 0
            if opcao == '3':
                print(f'Você deseja ir para {destino3}? Por {preco3}')
                preco2 = 0
                preco1 = 0
        
        precos = preco1 + preco2 + preco3
        lista_preco = [precos]

        for preco in lista_preco:
            preco = float(preco)
        ida_ou_volta = input(f'Deseja comprar passagem somente de Ida, de Volta ou Ida e Volta?')
        numero_passagens = input(f'Deseja comprar quantas passagens?')
        
        if numero_passagens.isnumeric(): 
            numero_passagens = int(numero_passagens)
            if numero_passagens >= 1:
                if ida_ou_volta.isnumeric():
                    print("Erro")
                    break
                elif ida_ou_volta.upper() == 'IDA E VOLTA':
                        preco_final = (preco*2)*numero_passagens
                        print(f"O valor da sua compra é {preco_final} \n")
                elif ida_ou_volta.upper() == 'IDA' or ida_ou_volta.upper() =='VOLTA':
                    preco_final = preco*numero_passagens
                    print(f"O valor da sua compra é {preco_final} \n")
        else:
            break

        continuar_compra = input(f'Deseja comprar mais alguma passagem senhor(a) {info_viajante_nome}? Digite Sim ou Não')
        if continuar_compra.isnumeric():
            if continuar_compra.upper() == 'N' or continuar_compra.upper() == 'NÃO' or continuar_compra.upper() == 'NAO':
                print("Obrigado por escolher nossa empresa! Tenha um bom dia, fechando sistema...")
                break







