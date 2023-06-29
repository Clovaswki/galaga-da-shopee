from settings import *
from utils.criar_frames import criar_frames

class Tela_inicial:

    def __init__(self):
        self.largura = tela.get_width()
        self.altura = tela.get_height() 
        self.frames = criar_frames('img/frames_tela_inicial/', self.largura, self.altura)
        self.atual = 0
        self.sprite = self.frames[self.atual]

    def atualizar_frames(self, contador_frames):
        if self.atual == len(self.frames)-1:
            self.atual=0
        
        if contador_frames%6==0:
            self.atual+=1

        self.sprite = self.frames[self.atual]