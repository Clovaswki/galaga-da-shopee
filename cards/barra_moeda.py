from settings import *
import pygame

class Barra_moeda:

    def __init__(self):
        self.largura=120
        self.altura=50
        self.image = pygame.transform.scale(pygame.image.load("img/frames_moeda/moeda_10.png"), (30, 30))
        self.num_moedas = 0
        self.font = pygame.font.SysFont(None, 34)
        self.img_num_moedas = self.font.render(str(self.num_moedas), True, (255,255,255))
        self.barra_img = pygame.transform.scale(pygame.image.load('img/card.png'), (self.largura, self.altura))
        self.x = tela.get_width()-self.largura-20
        self.y = 10

    def criar_barra_moeda(self):
        tela.blit(self.barra_img, (self.x, self.y))
        tela.blit(self.image, (self.x+10,self.y+10))
        tela.blit(self.render_moedas(), (self.x+60, self.y+15))

    def render_moedas(self):
        return self.font.render(str(self.num_moedas), True, (255,255,255))

    def aumentar_moedas(self):
        self.num_moedas+=1

    def reset(self):
        self.num_moedas=0