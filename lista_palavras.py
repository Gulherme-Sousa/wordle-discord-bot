import re


def obter_lista_palavras():
  palavras = []

  with open("palavras.txt", 'r', encoding='utf-8') as arquivo:
    linhas = arquivo.readlines()

    for linha in linhas:
      palavra = linha.strip()
      if len(palavra) == 5 and re.match("^[a-z]{5}$", palavra):
        palavras.append(palavra)

  return palavras