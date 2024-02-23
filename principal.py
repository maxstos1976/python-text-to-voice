''' 1. Texto a Voz
La idea de este proyecto es convertir un artículo existente en un archivo de audio reproducible 
en formato mp3. Para ello puedes hacer uso de bibliotecas existenes como nltk (kit de 
herramientas de lenguaje natural), newspaper3k y gtts (puedes seguir las instrucciones de 
instalación de pip).
Puedes crear un programa al que proporcionarle una URL de un artículo a convertir para 
luego manejar la conversión de texto a voz 


Aula de NLTK ( https://www.youtube.com/watch?v=siVUal-TeMc )
# Baixa os recursos do idioma português
import nltk
nltk.download('punkt')
nltk.download('floresta')
nltk.download('averaged_perceptron_tagger')
nltk.download('maxent_ne_chunker')
nltk.download('words')
'''
import numpy
import nltk
import pyglet
from gtts import gTTS
import os
from newspaper import Article


#Limpar tela
os.system('cls')

#--UTILIZANDO A BIBLIOTECA NEWSPAPER-------------------------------------------------------
# URL do artigo que você deseja extrair
# url = 'https://www.example.com/seu-artigo'
url = 'https://www.vortexmag.net/os-5-mais-belos-poemas-de-sempre-escritos-em-portugues/'

# Criar um objeto Article e passar a URL
article = Article(url)

# Baixar e analisar o artigo
article.download()
article.parse()

# Imprimir informações do artigo
print("Título:", article.title)
print("Autores:", article.authors)
print("Data de Publicação:", article.publish_date)
print("Texto do Artigo:")
texto = article.text
print(texto)


# UTILIZANDO A BIBLIOTECA NLTK-------------------------------------------------
# utiliza o nltk para dividir o texto em frases.
utilizarNLTK = False
if utilizarNLTK == True:
    frases = nltk.tokenize.sent_tokenize(texto, language='portuguese')
    #print(frases)

    # utiliza o nltk para transformar o texto em tokens (PALAVRAS). 
    tokens = nltk.word_tokenize(texto,language='portuguese')
    #print(tokens)

    # Ele da a classe gramatical de cada palavra 
    # lista em: http://cs.nyu.edu/grishman/jet/guide/PennPOS.html )
    classes = nltk.pos_tag(tokens)
    #print(classes)

    # nltk devolve uma entidade... detecta se dada palavra é uma pessoa, empresa etc...
    entidades = nltk.chunk.ne_chunk(classes)
    #print(entidades)


#--UTILIZANDO A BIBLIOTECA GTTS ----------------------------------------------------------
#texto = article.text
linguagem = 'pt-br'

#Cria uma instancio do objeto gTTS com o texto e o idioma definidos
tts = gTTS(text=texto, lang=linguagem)

filename = "speech.mp3"
os.remove(filename) # Remove se o arquivo ja existe
print("Salvando arquivo em MP3...")
tts.save(filename) #Salva o arquivo de audio no formato mp3
print("Finalizado o salvamento!")



#-- UTILIZANDO A BIBLIOTECA pyglet---------------------------------------------------------
# Reproduz o arquivo de audio usando a biblioteca pyglet
print("Carregando arquivo de som...")
music = pyglet.media.load(filename)
print("Executando arquivo de som...")
music.play()

pyglet.app.run() # Mantem o programa em execucao enquanto o audio esta sendo reproduzido

