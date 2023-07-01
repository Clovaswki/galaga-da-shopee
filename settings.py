import pygame
from pygame.locals import *

#configurar tela
largura = 640
altura = 480
tela = pygame.display.set_mode((largura, altura))

#inicializando a lib
pygame.init()
pygame.display.set_caption("Galaga da shoope")
pygame.mixer.music.set_volume(.1)

#classes
from classes.nave import Nave
from classes.asteroide import Asteroide
from classes.bala import Bala
from classes.background import Background
from classes.moeda import Moeda
from cards.barra_vida import Barra_vida
from cards.barra_moeda import Barra_moeda
from classes.explosao import Explosao
from classes.nave_inimiga import Nave_inimiga
from classes.bala_inimiga import Bala_inimiga

musics = {
    "tela_inicial": 'music/musica_tela_inicial.mp3', 
    "jogo": 'music/galaga_music.mp3'
}

#musica da tela inicial
pygame.mixer.music.load(musics["tela_inicial"])
pygame.mixer.music.play(-1)

#cards
barra_vida = Barra_vida()
barra_moeda = Barra_moeda()

#som disparo da nave
bala_som = pygame.mixer.Sound("music/bala.wav")
bala_som.set_volume(.3)

#som de coleta de moeda
moeda_som = pygame.mixer.Sound("music/moeda.wav")
moeda_som.set_volume(.08)

#som de perda de vida
perder_vida_som = pygame.mixer.Sound("music/perda_vida.wav")
perder_vida_som.set_volume(.1)

#som game over
game_over_som = pygame.mixer.Sound('music/game_over.wav')
game_over_som.set_volume(.2)

#configuracao FPS
relogio = pygame.time.Clock()
FPS = 60