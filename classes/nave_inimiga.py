from settings import * 
from random import randint
import pygame
from utils.criar_frames import criar_frames

class Nave_inimiga:

    def __init__(self):
        self.largura = 80
        self.altura = 77
        self.x = randint(0, tela.get_width()-self.largura)
        self.y = -self.altura
        self.velocidade = 2
        self.frames = criar_frames('img/frames_nave_inimiga/', self.largura, self.altura)
        self.atual = 0
        self.sprite = self.frames[self.atual]
        self.cont_frames = 0
        self.rect = pygame.mask.from_surface(self.sprite)

    def criar_nave(self, nave):
        tela.blit(self.sprite, (self.x, self.y))
        self.mover_nave(nave)
        self.atualizar_frames()

    def atualizar_frames(self):
        self.cont_frames+=1

        if self.atual == len(self.frames)-1:
            self.atual=0
        
        if self.cont_frames%15==0:
            self.atual+=1

        self.sprite = self.frames[self.atual]

    def mover_nave(self, nave):
        self.y += self.velocidade

        #mover nave inimiga de acordo com a posição x da nave do bem
        if self.x != nave.x and self.y <= nave.y:
            if self.x > nave.x:
                self.x -= self.velocidade
            else:
                self.x += self.velocidade