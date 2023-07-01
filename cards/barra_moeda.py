import pygame
from settings import *

class Barra_moeda:

    def __init__(self):
        self.largura=278
        self.altura=30
        self.num_moedas = 0
        self.font = pygame.font.SysFont(None, 21)
        self.img_num_moedas = self.font.render(str(self.num_moedas), True, (0, 0, 0))
        self.barra_img = pygame.transform.scale(pygame.image.load('img/card_moedas.png'), (self.largura, self.altura))
        self.x = tela.get_width()-self.largura-10
        self.y = 10

    def criar_barra_moeda(self):
        tela.blit(self.barra_img, (self.x, self.y))
        tela.blit(self.render_moedas(), (self.x+self.largura-60, self.y+11))

    def render_moedas(self):
        return self.font.render(str(self.num_moedas), False, (0, 0, 0))

    def aumentar_moedas(self):
        self.num_moedas+=1

    def reset(self):
        self.num_moedas=0