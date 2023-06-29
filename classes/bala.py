import pygame
from settings import *
from classes.color import Color

class Bala:

    def __init__(self, nave_x, nave_y):
        self.largura = 10
        self.altura = 30
        self.x = nave_x+self.largura*2
        self.y = nave_y-self.altura
        self.img = pygame.transform.scale(pygame.image.load('img/bala.png'), (self.largura, self.altura))
        self.rect = pygame.mask.from_surface(self.img)
        self.velocidade_bala = 10

    def gerar_bala(self):
        tela.blit(self.img, (self.x, self.y))
        self.mover_bala()

    def mover_bala(self):
        self.y -= self.velocidade_bala