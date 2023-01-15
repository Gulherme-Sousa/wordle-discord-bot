import nltk

nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')
from lista_palavras import obter_lista_palavras

def obter_palavras_filtradas():
  palavras = obter_lista_palavras()
  filtradas = nltk.word_tokenize(' '.join(palavras))
  
  palavras_categorizadas = nltk.pos_tag(filtradas) # Categorizar palavras como nome, verbo, etc
  palavras_sem_pessoas = [
    word[0]
    for word in palavras_categorizadas
    if word[1] != 'NNP'
  ]
  return palavras_sem_pessoas