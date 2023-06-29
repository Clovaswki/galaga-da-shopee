import pygame
from settings import tela

class Nave:

    def __init__(self):
        self.largura = 50
        self.altura = 50
        self.x = tela.get_width()//2-self.largura//2#posicionar no centro
        self.y = tela.get_height()-self.altura#posicionar no final
        self.img = pygame.transform.scale(pygame.image.load('img/nave.png'), (self.largura, self.altura))
        self.rect = pygame.mask.from_surface(self.img)
        self.quant_vida = 3

    def criar_nave(self):
        tela.blit(self.img, (self.x, self.y))
        self.mover_nave()

    def mover_nave(self):
        
        keys = pygame.key.get_pressed()

        if keys[pygame.K_w]:
            if self.y != 0:
                self.y -= 5
        if keys[pygame.K_s]:
            if self.y != tela.get_height()-self.altura:
                self.y += 5
        if keys[pygame.K_a]:
            if self.x != 0:
                self.x -= 5
        if keys[pygame.K_d]:
            if self.x != tela.get_width()-self.largura:
                self.x += 5 