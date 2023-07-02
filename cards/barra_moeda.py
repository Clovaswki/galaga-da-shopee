import pygame
from settings import *
from classes.color import Color

class Barra_moeda:

    def __init__(self):
        self.largura=278
        self.altura=30
        self.num_moedas = 0
        self.font = pygame.font.SysFont(None, 21)
        self.img_num_moedas = self.font.render(str(self.num_moedas), True, Color.black)
        self.barra_img = pygame.transform.scale(pygame.image.load('img/card_moedas.png'), (self.largura, self.altura))
        self.x = tela.get_width()-self.largura-10
        self.y = 10

    def criar_barra_moeda(self):
        tela.blit(self.barra_img, (self.x, self.y))
        tela.blit(self.render_moedas(), (self.x+80, self.y+11))

    def render_moedas(self):
        return self.font.render("Pontuação: "+str(self.num_moedas), False, Color.black)

    def aumentar_moedas(self):
        self.num_moedas+=1

    def reset(self):
        self.num_moedas=0