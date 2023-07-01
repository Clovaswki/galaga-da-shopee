from settings import *

class Tela_game_over:

    def __init__(self):
        self.largura = tela.get_width()
        self.altura = tela.get_height()
        self.logo = pygame.transform.scale(pygame.image.load('img/game_over/logo.png'), (169, 233))
        self.btn_reset = pygame.image.load('img/game_over/btn_reset.png')
        self.btn_tela_inicial = pygame.image.load('img/game_over/btn_tela_inicial.png')
        
        #rects buttons
        self.rect_btn_reset = self.btn_reset.get_rect()
        self.rect_btn_tela_inicial = self.btn_tela_inicial.get_rect()

        #posicoes btn reset
        self.btn_reset_x = self.largura//2-self.btn_reset.get_width()//2
        self.btn_reset_y = 350
        #posicoes btn tela inicial
        self.btn_tela_inicial_x = self.largura//2-self.btn_tela_inicial.get_width()//2
        self.btn_tela_inicial_y = 300

    def criar_game_over(self):
        tela.blit(self.logo, (self.largura//2-self.logo.get_width()//2, 30))
        tela.blit(self.btn_tela_inicial, (self.btn_tela_inicial_x, self.btn_tela_inicial_y))
        tela.blit(self.btn_reset, (self.btn_reset_x, self.btn_reset_y))

        #setar posicoes dos rects de acordo com a tela
        self.rect_btn_reset.x, self.rect_btn_reset.y = self.btn_reset_x, self.btn_reset_y
        self.rect_btn_tela_inicial.x, self.rect_btn_tela_inicial.y = self.btn_tela_inicial_x, self.btn_tela_inicial_y

    def click_btn_reset(self):
       return self.rect_btn_reset.collidepoint(pygame.mouse.get_pos())
        
    def click_btn_tela_inicial(self):
        return self.rect_btn_tela_inicial.collidepoint(pygame.mouse.get_pos())