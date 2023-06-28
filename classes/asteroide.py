import pygame
from random import randint
from settings import tela
from classes.color import Color

class Asteroide:

    def __init__(self):
        self.valor_aleatorio = randint(40, 60)
        self.largura = self.valor_aleatorio
        self.altura = self.valor_aleatorio
        self.x = randint(10, tela.get_width())
        self.y = -20
        self.img = pygame.transform.scale(pygame.image.load('img/asteroide.png'), (self.largura, self.altura))
        self.get_rect = self.img.get_rect()

    def criarAsteroide(self):
        rect = tela.blit(self.img, (self.x, self.y))
        self.movimentarAsteroide()
        self.get_rect.x = self.x
        self.get_rect.y = self.y
        return rect
    
    def movimentarAsteroide(self):
        self.y += 5