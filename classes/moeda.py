import pygame
from settings import *
from utils.criar_frames import criar_frames
from random import randint

class Moeda:
    
    def __init__(self):   
        self.frames = criar_frames('img/frames_moeda/', largura=30, altura=30)
        self.atual_index = 0
        self.number_frames = len(self.frames)
        self.sprite = self.frames[self.atual_index]
        self.rect = self.sprite.get_rect()
        self.x = randint(0, tela.get_width())
        self.y = -altura

    def criar_moeda(self, contador_frames):
        tela.blit(self.sprite, (self.x, self.y))
        self.atualizar_frames(contador_frames)
        self.rect = self.sprite.get_rect()   
        self.mover_moeda()

    def mover_moeda(self):
        self.y += 5
        self.rect.x = self.x
        self.rect.y = self.y

    def atualizar_frames(self, contador_frames):
        if contador_frames%7==0:
            self.atual_index+=1

        if self.atual_index==self.number_frames-1:
            self.atual_index=0

        self.sprite = self.frames[self.atual_index]