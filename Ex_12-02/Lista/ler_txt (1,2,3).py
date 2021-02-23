"""
    Programa para ler arquivos txt, que são os exigidos para os 3 primeiros exercícios da lista
"""

import io



print("============ Buscando arquivos TXT ============ \n")
print("=======================//====================== \n")
buscaArquivo = input("Digite o nome do arquivo: \n")
arquivo = open(buscaArquivo+".txt", "r", encoding="utf-8") #caminho do arquivo

print(arquivo.read())