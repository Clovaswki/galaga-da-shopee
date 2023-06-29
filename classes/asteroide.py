import pygame
from random import randint
from settings import tela

class Asteroide:

    def __init__(self):
        self.valor_aleatorio = randint(40, 60)
        self.largura = self.valor_aleatorio
        self.altura = self.valor_aleatorio
        self.x = randint(10, tela.get_width()-self.largura)
        self.y = -20
        self.img = pygame.transform.scale(pygame.image.load('img/asteroide.png'), (self.largura, self.altura))
        self.rect = pygame.mask.from_surface(self.img)

    def criar_asteroide(self):
        tela.blit(self.img, (self.x, self.y))
        self.movimentar_asteroide()

    def movimentar_asteroide(self):
        self.y += 5