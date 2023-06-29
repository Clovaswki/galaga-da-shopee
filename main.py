from pygame.locals import *
from sys import exit
import pygame

#classes
from classes.nave import Nave
from classes.asteroide import Asteroide
from classes.color import Color
from classes.bala import Bala
from classes.background import Background
from classes.moeda import Moeda

#congifurações globais
from settings import *

#instancias das classes
nave = Nave()
background = Background()

run = True

#delay na criacao de asteroides
taxa_frames_gerar_asteroide = 60

#boleano de controle: verifica quando colide
colide = False

#lista de asteroides gerados
list_asteroides = []

#lista de balas geradas
lista_balas = []

#lista de moedas
lista_moedas = []

def criar_asteroide():
    ast = Asteroide()
    list_asteroides.append(ast)
    deletar_asteroide()

def deletar_asteroide():
    limite_asteroide = 20
    if len(list_asteroides)>=limite_asteroide:
        list_asteroides.remove(list_asteroides[0])

def gerar_bala(nave_x, nave_y):
    bala = Bala(nave_x, nave_y)
    lista_balas.append(bala)
    apagar_bala()

def apagar_bala():
    limite_balas = 20
    if len(lista_balas)>=limite_balas:
        lista_balas.remove(lista_balas[0])

def gerar_moeda():
    moeda = Moeda()
    lista_moedas.append(moeda)
    deletar_moeda()

def deletar_moeda():
    limite_moedas = 20
    if len(lista_moedas)>=limite_moedas:
        lista_moedas.remove(lista_moedas[0])

while run:

    tela.blit(
        background.sprite, 
        (0, 0)
    )
    relogio.tick(FPS)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                colide = False
                taxa_frames_gerar_asteroide = 60
                contador_frames = 0
            if event.key == pygame.K_f:
                gerar_bala(nave.x, nave.y)
                bala_som.play()

    #incrementar o contador
    contador_frames += 1

    if not colide:

        if contador_frames%FPS*3==0:
            gerar_moeda()

        nave.criarNave()

        #aumenta a densidade de asteroides a cada 10 segundos
        if contador_frames%(10*FPS)==0:
            if taxa_frames_gerar_asteroide > 5:
                taxa_frames_gerar_asteroide = taxa_frames_gerar_asteroide/2

        #criar asteroides de acordo a qtde de frames escolhidos
        if contador_frames%taxa_frames_gerar_asteroide==0:
            criar_asteroide()
        
        #desenhar asteroides criados
        for ast in list_asteroides:
            ast.criarAsteroide()
        
        #desenhar balas criadas
        for bal in lista_balas:
            bal.gerarBala()

        #desenhar moedas criadas
        for moed in lista_moedas:
            moed.criar_moeda(contador_frames)

            #colisoes da nave com as moedas
            if nave.get_rect.colliderect(moed.rect):
                lista_moedas.remove(moed)
                moeda_som.play()


        for ast in list_asteroides:
            #colisoes da nave com os asteroides
            if nave.get_rect.colliderect(ast.get_rect):
                nave = Nave()
                list_asteroides = []
                colide = True
                pygame.mixer.music.stop()
            #colisoes da bala com os asteroides
            for bal in lista_balas:
                if bal.get_rect.colliderect(ast.get_rect):
                    lista_balas.remove(bal)
                    if ast in list_asteroides:
                        list_asteroides.remove(ast)

    else:
        tela.blit(game_over_img, (tela.get_width()//2-150, tela.get_height()//2-125))

    background.atualizar_frames(contador_frames)

    pygame.display.update()
    pygame.display.flip()

exit()