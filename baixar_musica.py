from pytube import YouTube
from moviepy.video.io.VideoFileClip import VideoFileClip
import os
from moviepy.editor import *
import threading
import urllib.request
from shutil import copy2

global __Variaveis
__Variaveis = {
    'Salvar': False,
    'Titulo': ''
}

def baixar_audio(link=str):
    """cole o link aqui"""
    print("Carregando o audio")
    arquivo = YouTube(link).streams.filter(file_extension="mp4").first().download()
    os.rename(arquivo, "A.mp4")
    videoclip = VideoFileClip("./A.mp4")
    audioclip = videoclip.audio
    audioclip.write_audiofile("audio.mp3")
    audioclip.close()
    videoclip.close()
    os.remove('A.mp4')

def search(pesquisa=str):
    global __Variaveis
    html = urllib.request.urlopen(f"https://www.youtube.com/results?search_query={pesquisa.replace(' ' , '+')}").read()
    Cod_link = str(html).split('"videoId":"')[1].split('","')[0]
    __Variaveis['Titulo'] = str(str(html).split('"title":{"runs":[{"text":"')[1].split('"}],"')[0])
    return f"https://youtu.be/{Cod_link}"   

baixar_audio(search('Calvaram meu gato'))
