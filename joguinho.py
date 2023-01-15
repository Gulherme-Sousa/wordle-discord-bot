from dicionario_pt import obter_palavras_filtradas
import random
import time


lista_palavras = obter_palavras_filtradas()

def obter_palavra_aleatoria():  
  print(f"Total de palavras: {len(lista_palavras)}")
  random.seed(time.time())
  palavra = random.choice(lista_palavras)
  return palavra

###########
VITORIA = 1
DERROTA = 2
EM_ANDAMENTO = 3
ERRO = 4

class Joguinho:
  def __init__(self):
    self.resetar()

  
  def resetar(self):
    self.tentativas = 5
    self.palavra = None
    self.em_execucao = False

  
  def iniciar(self):
    self.palavra = obter_palavra_aleatoria()
    self.em_execucao = True
    self.proximidade = ""

  
  def vitoria(self):
    print("voce é fera !!!!")
    self.resetar()

  
  def derrota(self):
    print("voce é ruim !!!!")
    self.resetar()
    

  def tentativa(self, chute):
    print(chute, self.palavra)
    
    if not self.em_execucao:
      print("Não está com jogo em andamento")
      return ERRO

    if len(chute) != len(self.palavra):
      print("Não pode palavra com tamanho diferente!!")
      return ERRO

    if chute not in lista_palavras:
      print("Não existe essa palavra!!")
      return ERRO

    self.tentativas -= 1

    same_position = []
    common_letters = []
  
    for i in range(len(self.palavra)):
        if self.palavra[i] == chute[i]:
            same_position.append(self.palavra[i])
        if self.palavra[i] in chute:
            common_letters.append(self.palavra[i])

    aux = chute
    for letter in same_position:
        aux = aux.replace(letter, "X")
    
    for letter in common_letters:
        aux = aux.replace(letter, "O")
    
    for letter in set(aux):
        if letter not in ["X","O"] :
            aux = aux.replace(letter, "-")

    self.proximidade = aux
    print(self.proximidade)

    if self.palavra == chute:
      self.vitoria()
      return VITORIA

    if self.tentativas == 0:
      self.derrota()
      return DERROTA

    return EM_ANDAMENTO
    