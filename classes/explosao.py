from utils.criar_frames import criar_frames
from settings import *
import pygame

class Explosao:

    def __init__(self, obj):
        self.largura = obj.largura
        self.altura = obj.altura
        self.frames = criar_frames('img/frames_asteroide/', self.largura, self.altura)
        self.atual = 0
        self.sprite = self.frames[self.atual]
        self.x = obj.x
        self.y = obj.y
        self.cont = 0#gerenciar o tempo de existencia da explosao

    def criar_explosao(self, contador_frames):
        tela.blit(self.sprite, (self.x, self.y))
        self._atualizar_frames(contador_frames)
        self.cont+=1

    def _atualizar_frames(self, contador_frames):
        if self.atual == len(self.frames)-1:
            self.atual = 0

        if contador_frames%10==0:
            self.atual+=1

        self.sprite = self.frames[self.atual]