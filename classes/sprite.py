import pygame
import os

#classe pronta para ser herdada em classes que usam sprites como animação
class Sprite:

    def __init__(self):
        self.atual = 0
        self.frames = ['']
        self.taxa_frames = 10
        self.cont_frames = 0
        self.sprite = self.frames[self.atual]

    #ler pasta dos frames, criar objetos pygames, 
    # armazenar em array
    def criar_frames(self, path, largura, altura):
        files = os.listdir(path)
        frames=[]
        for file in files:
            frame = pygame.image.load(path+file)
            frame = pygame.transform.scale(frame, (largura, altura))
            frames.append(frame)
        self.frames = frames

    def atualizar_frames(self):

        self.cont_frames+=1

        if self.atual == len(self.frames)-1:
            self.atual=0
        
        if self.cont_frames%self.taxa_frames==0:
            self.atual+=1

        self.sprite = self.frames[self.atual]