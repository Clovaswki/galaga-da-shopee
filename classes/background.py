from settings import *
from utils.criar_frames import criar_frames
import pygame

class Background:

    def __init__(self):   
        self.frames = criar_frames('img/frames_background/', tela.get_width(), tela.get_height())
        self.atual_index = 0
        self.number_frames = len(self.frames)
        self.sprite = self.frames[0]
    
    def atualizar_frames(self, contador_frames):
        if contador_frames%7==0:
            self.atual_index+=1

        if self.atual_index==self.number_frames-1:
            self.atual_index=0

        self.sprite = self.frames[self.atual_index]