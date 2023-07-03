import pygame
from settings import *
from classes.color import Color

class Barra_moeda:

    def __init__(self):
        self.largura=100
        self.altura=30
        self.num_moedas = 0
        self.font = pygame.font.SysFont(None, 18)
        self.img_num_moedas = self.font.render(str(self.num_moedas), True, Color.black)
        self.barra_img = pygame.transform.scale(pygame.image.load('img/barra_moedas.png'), (self.largura, self.altura))
        self.x = tela.get_width()-self.largura
        self.y = 10

    def criar_barra_moeda(self):
        tela.blit(self.barra_img, (self.x, self.y))
        tela.blit(self.render_moedas(), (self.x+40, self.y+10))

    def render_moedas(self):
        return self.font.render(str(self.num_moedas), False, Color.white)

    def aumentar_moedas(self):
        self.num_moedas+=1

    def reset(self):
        self.num_moedas=0