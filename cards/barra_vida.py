from utils.criar_frames import criar_frames
from settings import *

class Barra_vida:

    def __init__(self):
        self.frames = criar_frames('img/frames_barra_vida/', 167, 18)
        self.atual = 0
        self.image = self.frames[self.atual]

    def criar_barra_vida(self):
        tela.blit(self.image, (10,10))

    def diminuir_vida(self):

        if self.atual == len(self.frames)-1:
            self.atual = 0

        self.atual+=1
        self.image = self.frames[self.atual]

    def reset(self):
        self.atual=0
        self.image = self.frames[self.atual]