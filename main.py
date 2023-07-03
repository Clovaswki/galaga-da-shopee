from pygame.locals import *
from sys import exit
import pygame

#congifurações globais
from settings import *

#functions do jogo
from functions_game import *

#telas
from telas.tela_inicial import Tela_inicial
from telas.tela_jogo import tela_jogo
from telas.tela_game_over import Tela_game_over

tela_escolhida = "tela_inicial"

#contar os frames durante a execuçao do jogo
contador_frames = 0

#instacia das telas
tela_inicial = Tela_inicial(contador_frames=contador_frames)
tela_game_over = Tela_game_over()

#instancias das classes
nave = Nave()
background = Background()

run = True

#delay na criacao de asteroides
taxa_frames_gerar_asteroide = 60

#lista de asteroides gerados
list_asteroides = []

#lista de balas geradas
lista_balas = []

#lista de moedas
lista_moedas = []

#lista de explosoes
lista_explosoes = []

#lista de balas inimigas
lista_balas_inimigas = []

#lista de naves inimigas
lista_naves_inimigas = []

while run:

    relogio.tick(FPS)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_f:
                if tela_escolhida=='main':
                    gerar_bala(lista_balas, nave.x, nave.y)
                    bala_som.play()
            if event.key == pygame.K_r:
                if tela_escolhida=="tela_inicial":
                    tela_escolhida = 'main'
                    pygame.mixer.music.load(musics["jogo"])
                    pygame.mixer.music.play(-1)
                    pygame.mixer.music.set_volume(.3)
        if event.type == pygame.MOUSEBUTTONDOWN:
            if tela_escolhida=='gameover':
                taxa_frames_gerar_asteroide = 60
                contador_frames = 0
                nave = Nave()
                list_asteroides = []
                lista_balas = []
                lista_moedas = []
                lista_balas_inimigas = []
                lista_naves_inimigas = []
                lista_explosoes = []
                if tela_game_over.click_btn_reset():
                    tela_escolhida="main"
                    pygame.mixer.music.play(-1)
                if tela_game_over.click_btn_tela_inicial():
                    tela_escolhida="tela_inicial"   
                    pygame.mixer.music.load(musics["tela_inicial"])
                    pygame.mixer.music.play(-1)

    #incrementar o contador
    contador_frames += 1
    
    if tela_escolhida=='main':

        #aumenta a densidade de asteroides a cada 10 segundos
        if contador_frames%(10*FPS)==0:
            if taxa_frames_gerar_asteroide/2 >= 5:
                taxa_frames_gerar_asteroide *= 0.5

        #checar se é game over
        if nave.quant_vida == 0:
            tela_escolhida = 'gameover'

        tela_jogo(
            nave=nave,
            background=background,
            lista_asteroides=list_asteroides,
            lista_balas=lista_balas,
            lista_moedas=lista_moedas,
            lista_explosoes=lista_explosoes,
            taxa_frames_gerar_asteroide=taxa_frames_gerar_asteroide,
            contador_frames=contador_frames,
            lista_balas_inimigas=lista_balas_inimigas,
            lista_naves_inimigas=lista_naves_inimigas
        )

    elif tela_escolhida=="gameover":
        tela_game_over.criar_game_over()
    else:
        tela_inicial.iniciar()

    background.atualizar_frames(contador_frames)
    pygame.display.update()
    pygame.display.flip()

exit()