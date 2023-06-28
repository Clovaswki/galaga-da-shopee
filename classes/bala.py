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
        self.get_rect = self.img.get_rect()
        self.velocidade_bala = 10

    def gerarBala(self):
        tela.blit(self.img, (self.x, self.y))
        self.get_rect.x, self.get_rect.y = self.x, self.y
        self.moverBala()
        return self.get_rect

    def moverBala(self):

        self.y -= self.velocidade_bala
