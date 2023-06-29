import pygame
from pygame.locals import *
import os

#configurar tela
largura = 640
altura = 480
tela = pygame.display.set_mode((largura, altura))

#inicializando a lib
pygame.init()
pygame.display.set_caption("Galaga da shoope")
pygame.mixer.music.set_volume(.1)

#music
pygame.mixer.music.load('music/galaga_music.mp3')
pygame.mixer.music.play(-1)

#som disparo da nave
bala_som = pygame.mixer.Sound("music/bala.wav")
bala_som.set_volume(.3)

#som de coleta de moeda
moeda_som = pygame.mixer.Sound("music/moeda.wav")
moeda_som.set_volume(.08)

#configuracao FPS
relogio = pygame.time.Clock()
FPS = 60

#contar os frames durante a execuçao do jogo
contador_frames = 0

#game over
game_over_img = pygame.image.load('img/over.png')
game_over_img = pygame.transform.scale(game_over_img, (300, 250))