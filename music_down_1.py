from PyQt5 import QtCore, QtGui, QtWidgets
from pytube import YouTube
from moviepy.video.io.VideoFileClip import VideoFileClip
import os
from moviepy.editor import *
import threading
import urllib.request
import threading
import PySimpleGUI as sg

class Ui_MusicDownload(object):
    def setupUi(self, MusicDownload):
        global __Variaveis
        __Variaveis = {
            'Salvar': False,
            'Titulo': '',
            'Playlist': [],
            'Verificacao': 0
        }
        MusicDownload.setObjectName("MusicDownload")
        MusicDownload.setEnabled(True)
        MusicDownload.resize(1119, 613)
        MusicDownload.setMinimumSize(QtCore.QSize(800, 600))
        MusicDownload.setMaximumSize(QtCore.QSize(1920, 1080))
        font = QtGui.QFont()
        font.setFamily("Arial")
        MusicDownload.setFont(font)
        MusicDownload.setMouseTracking(False)
        icon = QtGui.QIcon("logo.png")
        icon.addPixmap(QtGui.QPixmap("logo.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        icon.addPixmap(QtGui.QPixmap("logo.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        icon.addPixmap(QtGui.QPixmap("logo.png"), QtGui.QIcon.Disabled, QtGui.QIcon.Off)
        icon.addPixmap(QtGui.QPixmap("logo.png"), QtGui.QIcon.Disabled, QtGui.QIcon.On)
        icon.addPixmap(QtGui.QPixmap("logo.png"), QtGui.QIcon.Active, QtGui.QIcon.Off)
        icon.addPixmap(QtGui.QPixmap("logo.png"), QtGui.QIcon.Active, QtGui.QIcon.On)
        icon.addPixmap(QtGui.QPixmap("logo.png"), QtGui.QIcon.Selected, QtGui.QIcon.Off)
        icon.addPixmap(QtGui.QPixmap("logo.png"), QtGui.QIcon.Selected, QtGui.QIcon.On)
        MusicDownload.setWindowIcon(icon)
        MusicDownload.setStyleSheet("")
        MusicDownload.setIconSize(QtCore.QSize(30, 30))
        self.centralwidget = QtWidgets.QWidget(MusicDownload)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.container_esquerda = QtWidgets.QFrame(self.centralwidget)
        self.container_esquerda.setMaximumSize(QtCore.QSize(240, 16777215))
        self.container_esquerda.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.container_esquerda.setFrameShadow(QtWidgets.QFrame.Raised)
        self.container_esquerda.setObjectName("container_esquerda")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.container_esquerda)
        self.verticalLayout.setObjectName("verticalLayout")
        self.imagem_logo = QtWidgets.QLabel(self.container_esquerda)
        self.imagem_logo.setMaximumSize(QtCore.QSize(16777215, 300))
        self.imagem_logo.setText("")
        self.imagem_logo.setPixmap(QtGui.QPixmap("logo.png"))
        self.imagem_logo.setScaledContents(True)
        self.imagem_logo.setObjectName("imagem_logo")
        self.verticalLayout.addWidget(self.imagem_logo)
        self.nome_do_programa = QtWidgets.QLabel(self.container_esquerda)
        self.nome_do_programa.setMaximumSize(QtCore.QSize(16777215, 250))
        self.nome_do_programa.setObjectName("nome_do_programa")
        self.verticalLayout.addWidget(self.nome_do_programa)
        self.versao_do_software = QtWidgets.QLabel(self.container_esquerda)
        self.versao_do_software.setMaximumSize(QtCore.QSize(16777215, 50))
        self.versao_do_software.setObjectName("versao_do_software")
        self.verticalLayout.addWidget(self.versao_do_software)
        self.horizontalLayout.addWidget(self.container_esquerda)
        self.container_direita = QtWidgets.QFrame(self.centralwidget)
        self.container_direita.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.container_direita.setFrameShadow(QtWidgets.QFrame.Raised)
        self.container_direita.setObjectName("container_direita")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.container_direita)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.corpo_frame = QtWidgets.QFrame(self.container_direita)
        self.corpo_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.corpo_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.corpo_frame.setObjectName("corpo_frame")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.corpo_frame)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.opcoes_para_escolha = QtWidgets.QTabWidget(self.corpo_frame)
        self.opcoes_para_escolha.setObjectName("opcoes_para_escolha")
        self.baixar_musica_pagina = QtWidgets.QWidget()
        self.baixar_musica_pagina.setObjectName("baixar_musica_pagina")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.baixar_musica_pagina)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.cabecalho_baixar_musica = QtWidgets.QLabel(self.baixar_musica_pagina)
        self.cabecalho_baixar_musica.setMaximumSize(QtCore.QSize(16777215, 50))
        self.cabecalho_baixar_musica.setObjectName("cabecalho_baixar_musica")
        self.verticalLayout_2.addWidget(self.cabecalho_baixar_musica)
        self.corpo_baixar_musica = QtWidgets.QFrame(self.baixar_musica_pagina)
        self.corpo_baixar_musica.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.corpo_baixar_musica.setFrameShadow(QtWidgets.QFrame.Raised)
        self.corpo_baixar_musica.setObjectName("corpo_baixar_musica")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.corpo_baixar_musica)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.entrada_de_musica = QtWidgets.QLineEdit(self.corpo_baixar_musica)
        self.entrada_de_musica.setMaximumSize(QtCore.QSize(500, 16777215))
        self.entrada_de_musica.setText("")
        self.entrada_de_musica.setObjectName("entrada_de_musica")
        self.verticalLayout_4.addWidget(self.entrada_de_musica, 0, QtCore.Qt.AlignHCenter)
        self.botao_baixar_musica = QtWidgets.QPushButton(self.corpo_baixar_musica)
        self.botao_baixar_musica.setMaximumSize(QtCore.QSize(220, 50))
        self.botao_baixar_musica.setStyleSheet("font: 75 12pt \"Arial\";\n"
"border-radios: 20px;")
        self.botao_baixar_musica.setObjectName("botao_baixar_musica")
        self.verticalLayout_4.addWidget(self.botao_baixar_musica, 0, QtCore.Qt.AlignHCenter)
        self.saida_status_musica = QtWidgets.QLabel(self.corpo_baixar_musica)
        self.saida_status_musica.setMaximumSize(QtCore.QSize(500, 100))
        self.saida_status_musica.setObjectName("saida_status_musica")
        self.verticalLayout_4.addWidget(self.saida_status_musica, 0, QtCore.Qt.AlignHCenter)
        self.verticalLayout_2.addWidget(self.corpo_baixar_musica)
        self.opcoes_para_escolha.addTab(self.baixar_musica_pagina, "")
        self.baixar_playlist_pagina = QtWidgets.QWidget()
        self.baixar_playlist_pagina.setObjectName("baixar_playlist_pagina")
        self.opcoes_para_escolha.addTab(self.baixar_playlist_pagina, "")
        self.doacoes = QtWidgets.QWidget()
        self.doacoes.setObjectName("doacoes")
        self.opcoes_para_escolha.addTab(self.doacoes, "")
        self.verticalLayout_3.addWidget(self.opcoes_para_escolha)
        self.horizontalLayout_2.addWidget(self.corpo_frame)
        self.horizontalLayout.addWidget(self.container_direita)
        MusicDownload.setCentralWidget(self.centralwidget)

        self.retranslateUi(MusicDownload)
        self.opcoes_para_escolha.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MusicDownload)
        
        self.botao_baixar_musica.clicked.connect(self.baixar_audio)
    
    def baixar_audio(self):
        link = self.search(self.entrada_de_musica.text())
        self.saida_status_musica.setText("Carregando o áudio...")
        self.saida_status_musica.setText(f"{str(YouTube(link).title)}")
        def baixando(self):
            try:
                if not os.path.exists('A.mp4'):
                    arquivo = YouTube(link).streams.filter(file_extension="mp4").first().download()
                    os.rename(arquivo, "A.mp4")
                    videoclip = VideoFileClip("A.mp4")
                    audioclip = videoclip.audio
                    audioclip.write_audiofile("audio.mp3")
                    audioclip.close()
                    videoclip.close()
                    os.remove('A.mp4')
                    os.rename('audio.mp3', f'{YouTube(link).title}.mp3')
                else:
                    os.remove('A.mp4')
            except Exception as err:
                print(f'O erro está: {err}')
                return False
            return True
        # Resolver problema de threading
        # threading.Thread(target=baixando, args=(link, )).start
        baixando(link)
    
    def search(self, pesquisa=str):
        global __Variaveis
        try:
            html = urllib.request.urlopen(f"https://www.youtube.com/results?search_query={pesquisa.replace(' ' , '+')}").read()
            Cod_link = str(html).split('"videoId":"')[1].split('","')[0]
            __Variaveis['Titulo'] = str(str(html).split('"title":{"runs":[{"text":"')[1].split('"}],"')[0])
            return f"https://youtu.be/{Cod_link}"
        except Exception as err:
            print(f'O erro está: {err}')
            return False

    def retranslateUi(self, MusicDownload):
        _translate = QtCore.QCoreApplication.translate
        MusicDownload.setWindowTitle(_translate("MusicDownload", "MuDown - Music Download"))
        self.nome_do_programa.setText(_translate("MusicDownload", "<html><head/><body><p align=\"center\"><span style=\" font-size:28pt;\">MuDown</span></p><p align=\"center\">Seja mais feliz, escute música</p></body></html>"))
        self.versao_do_software.setText(_translate("MusicDownload", "<html><head/><body><p align=\"center\"><span style=\" font-size:12pt;\">Versão - 1.0</span></p></body></html>"))
        self.cabecalho_baixar_musica.setText(_translate("MusicDownload", "<html><head/><body><p align=\"center\"><span style=\" font-size:18pt;\">Digite o nome da música</span></p></body></html>"))
        self.botao_baixar_musica.setText(_translate("MusicDownload", "Baixar Música"))
        self.saida_status_musica.setText(_translate("MusicDownload", "<html><head/><body><p align=\"center\"><span style=\" font-size:10pt;\">Saída de status do download da música</span></p></body></html>"))
        self.opcoes_para_escolha.setTabText(self.opcoes_para_escolha.indexOf(self.baixar_musica_pagina), _translate("MusicDownload", "Baixar Música"))
        self.opcoes_para_escolha.setTabText(self.opcoes_para_escolha.indexOf(self.baixar_playlist_pagina), _translate("MusicDownload", "Baixar Playlist"))
        self.opcoes_para_escolha.setTabText(self.opcoes_para_escolha.indexOf(self.doacoes), _translate("MusicDownload", "Doações"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MusicDownload = QtWidgets.QMainWindow()
    ui = Ui_MusicDownload()
    ui.setupUi(MusicDownload)
    MusicDownload.show()
    sys.exit(app.exec_())
