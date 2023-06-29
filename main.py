from pygame.locals import *
from sys import exit
import pygame

#congifurações globais
from settings import *

#functions do jogo
from functions_game import *

#instancias das classes
nave = Nave()
background = Background()

#cards
barra_vida = Barra_vida()
barra_moeda = Barra_moeda()

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

#lista de explosoes
lista_explosoes = []

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
                if colide:
                    colide = False
                    taxa_frames_gerar_asteroide = 60
                    contador_frames = 0
                    nave = Nave()
                    pygame.mixer.music.play(-1)
            if event.key == pygame.K_f:
                gerar_bala(lista_balas, nave.x, nave.y)
                bala_som.play()

    #incrementar o contador
    contador_frames += 1

    if not colide:

        #desenhar cards
        barra_vida.criar_barra_vida()
        barra_moeda.criar_barra_moeda()

        #criar moeda a cada quant. de frames
        if contador_frames%(FPS*1)==0:
            gerar_moeda(lista_moedas)

        nave.criar_nave()

        #aumenta a densidade de asteroides a cada 10 segundos
        if contador_frames%(10*FPS)==0:
            if taxa_frames_gerar_asteroide > 5:
                taxa_frames_gerar_asteroide = taxa_frames_gerar_asteroide/2

        #criar asteroides de acordo a qtde de frames escolhidos
        if contador_frames%taxa_frames_gerar_asteroide==0:
            criar_asteroide(list_asteroides)

        #desenhar explosoes
        for exp in lista_explosoes:
            #se a explosao passar de 15 frames, deixa de existir
            if not exp.cont >= (FPS/4):
                exp.criar_explosao(contador_frames)

        #desenhar asteroides criados
        for ast in list_asteroides:
            ast.criar_asteroide()
        
        #desenhar balas criadas
        for bal in lista_balas:
            bal.gerar_bala()

        #desenhar moedas criadas
        for moed in lista_moedas:
            moed.criar_moeda(contador_frames)

            #colisoes da nave com as moedas
            if nave.rect.overlap(moed.rect, (moed.x-nave.x, moed.y-nave.y)):
                lista_moedas.remove(moed)
                moeda_som.play()
                barra_moeda.aumentar_moedas()

        for ast in list_asteroides:
            #colisoes da nave com os asteroides
            if ast.rect.overlap(nave.rect, (ast.x-nave.x, ast.y-nave.y)):
            # if nave.get_rect.colliderect(ast.get_rect):
                list_asteroides.remove(ast)
                nave.quant_vida = nave.quant_vida -1
                barra_vida.diminuir_vida()
                if nave.quant_vida == 0:
                    list_asteroides = []
                    colide = True
                    barra_vida.reset()
                    barra_moeda.reset()
                    pygame.mixer.music.stop()
            #colisoes da bala com os asteroides
            for bal in lista_balas:
                if bal.rect.overlap(ast.rect, (ast.x-bal.x, ast.y-bal.y)):
                    criar_explosao(lista_explosoes, ast.largura, ast.altura, ast.x, ast.y)
                    lista_balas.remove(bal)
                    if ast in list_asteroides:
                        list_asteroides.remove(ast)
    
    else:
        tela.blit(game_over_img, (tela.get_width()//2-150, tela.get_height()//2-125))

    background.atualizar_frames(contador_frames)
    pygame.display.update()
    pygame.display.flip()

exit()