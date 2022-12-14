from pytube import YouTube
import os
from moviepy.editor import *
import requests

global __Variaveis
__Variaveis = {
    'titulo': '',
    'video': '',
    'playlist': []
}

def baixar_musica(link=str):
    global __Variaveis
    __Variaveis['titulo'] = YouTube(link).title
    
    def verificar():
        if os.path.exists('video.mp4'):
            os.remove('video.mp4')
        if os.path.exists(f"{__Variaveis['titulo']}.mp3"):
            os.remove(f"{__Variaveis['titulo']}.mp3")
            
    verificar()
    
    print('[+] Iniciando Download')
    print(f"[+] {__Variaveis['titulo']}")
    try:
        yt = YouTube(link).streams.filter(file_extension='mp4').first().download()
        if not os.path.exists('video.mp4'):
            print('[+] Iniciando processo de conversão..')
            os.rename(yt, 'video.mp4')
            vd = VideoFileClip('video.mp4')
            vd.audio.write_audiofile('audio.mp3')
            vd.close()
            os.rename('audio.mp3', f"{__Variaveis['titulo']}.mp3")
            os.remove('video.mp4')
            print('[+] Convertido!')
    except Exception as err:
        print(f'O erro está: {err}')


def pesquisar_video(nome=str):
    nome = nome.replace(' ', '+')
    pag = requests.get(f"https://www.youtube.com/results?search_query={nome}").text
    __Variaveis['video'] = str(pag).split('{"videoId":"')[1].split('"')[0]
    link = f"https://www.youtube.com/watch?v={__Variaveis['video']}"
    return link

def playlist(nome_playlist=str):
    global __Variaveis
    print('[+] Adicionando músicas à playlist...')
    try:
        while True:
            get_music = input('Digite o nome da música: ').strip().lower()
            if not get_music == 'baixar':
                __Variaveis['playlist'].append(pesquisar_video(get_music))
                if get_music == 'mostrar':
                    print('[+] Suas músicas são: ')
                    __Variaveis['playlist'].pop()
                    for i in range(len(__Variaveis['playlist'])):
                        print(f"{i} - {YouTube(__Variaveis['playlist'][i]).title}")
                elif get_music == 'excluir':
                    __Variaveis['playlist'].pop()
                    for c in range(len(__Variaveis['playlist'])):
                        print(f"{c} - {YouTube(__Variaveis['playlist'][c]).title}")
                    get_exclude = int(input('Digite o número da música que deseja excluir: '))
                    __Variaveis['playlist'].pop(get_exclude)
                    print(f'Música {get_exclude} excluída... Digite mostrar, para ver o como está a playlist!')
            else:
                with open(f'{nome_playlist}.txt', 'w') as music:
                    music.write(str(__Variaveis['playlist']).replace('[', '').replace(']', '').replace(',', '').replace('\'', '').replace(' ', '\n'))
                break
    except Exception as err:
        print(f'O erro está: {err}')
    
    def baixar_playlist():
        print('[+] Iniciando o download das músicas...')
        pl = open(f'{nome_playlist}.txt', 'r', encoding='utf-8')
        playlist = pl.readlines()
        for z in range(len(playlist)):
            baixar_musica(playlist[z])
        
        pl.close()
        
        get_input = input('[+] Deseja manter o arquivo da playlist?[S/N]: ').upper().strip()
        if not get_input[0] == 'S':
            os.remove(f'{nome_playlist}.txt')
    
    baixar_playlist()

playlist('megadeth')
