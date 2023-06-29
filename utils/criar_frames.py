import pygame
import os

#ler pasta dos frames, criar objetos pygames, 
# armazenar em array e descrever a logica de atualizacao de frames do background
def criar_frames(path, largura, altura):
    files = os.listdir(path)
    frames=[]
    for file in files:
        background = pygame.image.load(path+file)
        background = pygame.transform.scale(background, (largura, altura))
        frames.append(background)
    return frames 