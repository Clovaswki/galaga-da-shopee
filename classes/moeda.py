from utils.criar_frames import criar_frames
from random import randint
from settings import *
import pygame

class Moeda:
    
    def __init__(self):   
        self.largura = 30
        self.altura = 30
        self.frames = criar_frames('img/frames_moeda/', largura=30, altura=30)
        self.atual_index = 0
        self.sprite = self.frames[self.atual_index]
        self.rect = pygame.mask.from_surface(self.sprite)
        self.x = randint(0, tela.get_width()-self.largura)
        self.y = -self.altura

    def criar_moeda(self, contador_frames):
        tela.blit(self.sprite, (self.x, self.y))
        self.atualizar_frames(contador_frames)
        self.mover_moeda()

    def mover_moeda(self):
        self.y += 5

    def atualizar_frames(self, contador_frames):
        if contador_frames%7==0:
            self.atual_index+=1

        if self.atual_index==len(self.frames)-1:
            self.atual_index=0

        self.sprite = self.frames[self.atual_index]
        self.rect = pygame.mask.from_surface(self.sprite)