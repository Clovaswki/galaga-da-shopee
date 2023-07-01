from settings import *

class Bala_inimiga:

    def __init__(self, nave):
        self.largura = 10
        self.altura = 30
        self.x = nave.x+(nave.largura//2)-self.largura+2
        self.y = nave.y+nave.altura-10
        self.img = pygame.transform.scale(pygame.image.load('img/bala_inimiga.png'), (self.largura, self.altura))
        self.velocidade_bala = 8
        self.rect = pygame.mask.from_surface(self.img)
    
    def gerar_bala(self):
        tela.blit(self.img, (self.x, self.y))
        self.mover_bala()

    def mover_bala(self):
        self.y += self.velocidade_bala