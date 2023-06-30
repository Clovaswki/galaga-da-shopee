import pygame
from utils.criar_frames import criar_frames
from settings import *

class Tela_inicial:

    def __init__(self, contador_frames):
        # Inicialização das variáveis
        self.largura = tela.get_width()
        self.altura = tela.get_height()
        self.frames = criar_frames('img/frames_tela_inicial/', self.largura, self.altura)
        self.atual = 0
        self.sprite = self.frames[self.atual]

        # Carregamento da imagem do logo com transparência e textos
        self.imagem_logo = pygame.image.load("img/logo.png").convert_alpha()
        self.texto_aperte = pygame.image.load("img/texto_command.png").convert_alpha()
        self.texto_by = pygame.image.load("img/texto_by.png").convert_alpha()

        # Variáveis de controle do menu
        self.piscando = True
        self.tempo_atual = contador_frames
        self.cont_frames = contador_frames

    def iniciar(self):

        tela.blit(self.sprite, (0, 0))
        tela.blit(self.imagem_logo, (self.largura//2-131 , 10))

        if self.piscando:
            tela.blit(self.texto_aperte, (self.largura//2-186, 300))
        
        tela.blit(self.texto_by, (self.largura//2-93, 430))

        self.cont_frames+=1

        self.atualizar_frames()

    def atualizar_frames(self):
        # Atualização da animação de fundo
        ticks = pygame.time.get_ticks()

        if ticks%15==0:
            if self.atual == len(self.frames)-1:
                self.atual = 0
            else:
                self.atual+=1
        
        self.sprite = self.frames[self.atual]
        
        if (self.tempo_atual+60)==self.cont_frames:
            self.piscando = not self.piscando
            self.tempo_atual = self.cont_frames