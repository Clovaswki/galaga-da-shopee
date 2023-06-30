import pygame
from settings import *
from utils.criar_frames import criar_frames

class Nave:

    def __init__(self):
        self.largura = 50
        self.altura = 50
        self.x = tela.get_width()//2-self.largura//2#posicionar no centro
        self.y = tela.get_height()-self.altura#posicionar no final
        self.quant_vida = 4
        self.frames = criar_frames('img/frames_nave/', self.largura, self.altura)
        self.atual = 0
        self.sprite = self.frames[self.atual]
        self.rect = pygame.mask.from_surface(self.sprite)

    def criar_nave(self, contador_frames):
        tela.blit(self.sprite, (self.x, self.y))
        self.mover_nave()
        self.atualizar_frames(contador_frames)

    def atualizar_frames(self, contador_frames):
        if self.atual==len(self.frames)-1:
            self.atual=0
        
        if contador_frames%(60/4)==0:
            self.atual+=1
        
        self.sprite= self.frames[self.atual]

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