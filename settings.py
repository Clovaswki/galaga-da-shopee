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

#music
pygame.mixer.music.load('galaga_music.mp3')
pygame.mixer.music.play(-1)

#som disparo da nave
bala_som = pygame.mixer.Sound("bala.wav")
bala_som.set_volume(.2)

#configuracao FPS
relogio = pygame.time.Clock()
FPS = 60

#background
background = pygame.image.load('img/space.jpg')
background = pygame.transform.scale(background, (tela.get_width(), tela.get_height()))

#game over
game_over_img = pygame.image.load('img/over.png')
game_over_img = pygame.transform.scale(game_over_img, (300, 250))