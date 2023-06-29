import pygame
import os

#ler pasta dos frames, criar objetos pygames, 
# armazenar em array
def criar_frames(path, largura, altura):
    files = os.listdir(path)
    frames=[]
    for file in files:
        frame = pygame.image.load(path+file)
        frame = pygame.transform.scale(frame, (largura, altura))
        frames.append(frame)
    return frames 