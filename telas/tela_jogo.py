from settings import *
from functions_game import *
from random import randint

def tela_jogo(
        nave, 
        background, 
        lista_moedas, 
        lista_balas, 
        lista_asteroides, 
        lista_explosoes,
        taxa_frames_gerar_asteroide,
        contador_frames,
        lista_balas_inimigas,
        lista_naves_inimigas
        ):

    #sprite tela de fundo
    tela.blit(
        background.sprite, 
        (0, 0)  
    )
    #desenhar cards
    barra_vida.criar_barra_vida()
    barra_moeda.criar_barra_moeda()

    nave.criar_nave(contador_frames)

    if contador_frames>(FPS*60):
        #sera implementado depois de um minuto de jogo
        #criar balas inimigas a cada meio segundo
        if contador_frames%(FPS*0.5)==0:
            if len(lista_naves_inimigas)>0:
                criar_bala_inimiga(
                    lista_balas_inimigas, 
                    nave=lista_naves_inimigas[randint(0, len(lista_naves_inimigas)-1)]
                )
        #criar naves inimigas
        if contador_frames%(FPS*2)==0:
            criar_nave_inimiga(lista_naves_inimigas)

    else:
        #funcionara ate um minuto de jogo
        #criar asteroides de acordo a qtde de frames escolhidos
        if contador_frames%taxa_frames_gerar_asteroide==0:
            criar_asteroide(list_asteroides=lista_asteroides)

        
    #criar moeda a cada quant. de frames
    if contador_frames%(FPS*1)==0:
        gerar_moeda(lista_moedas)


    #desenhar naves inimigas
    for nave_inimiga in lista_naves_inimigas:
        nave_inimiga.criar_nave(nave)
        #colisao da nave inimiga com a nave do bem
        if nave_inimiga.rect.overlap(nave.rect, (nave.x-nave_inimiga.x, nave.y-nave_inimiga.y)):
            lista_naves_inimigas.remove(nave_inimiga)
            criar_explosao(lista_explosoes, nave_inimiga)
            nave.quant_vida = nave.quant_vida -1
            barra_vida.diminuir_vida()
            perder_vida_som.play()

    #desenhar balas inimigas
    for bal in lista_balas_inimigas:
        bal.gerar_bala()
        #colisao das balas inimigas com a nave do bem
        if bal.rect.overlap(nave.rect, (bal.x-nave.x, bal.y-nave.y)):
            lista_balas_inimigas.remove(bal)
            nave.quant_vida = nave.quant_vida -1
            barra_vida.diminuir_vida()
            perder_vida_som.play()

    #desenhar explosoes
    for exp in lista_explosoes:
        #se a explosao passar de 15 frames, deixa de existir
        if not exp.cont >= (FPS/4):
            exp.criar_explosao(contador_frames)

    #desenhar asteroides criados
    for ast in lista_asteroides:
        ast.criar_asteroide()
        
    #desenhar balas criadas
    for bal in lista_balas:
        bal.gerar_bala()
        #colisao das balas da nave do bem com as naves inimigas
        for nave_inimiga in lista_naves_inimigas:
            if bal.rect.overlap(
                nave_inimiga.rect, 
                (nave_inimiga.x-bal.x, nave_inimiga.y-bal.y)
            ):
                criar_explosao(lista_explosoes, nave_inimiga)
                lista_naves_inimigas.remove(nave_inimiga)
                lista_balas.remove(bal)

    #desenhar moedas criadas
    for moed in lista_moedas:
        moed.criar_moeda(contador_frames)

        #colisoes da nave com as moedas
        if nave.rect.overlap(moed.rect, (moed.x-nave.x, moed.y-nave.y)):
            lista_moedas.remove(moed)
            moeda_som.play()
            barra_moeda.aumentar_moedas()

    for ast in lista_asteroides:
        #colisoes da nave com os asteroides
        if ast.rect.overlap(nave.rect, (ast.x-nave.x, ast.y-nave.y)):
            lista_asteroides.remove(ast)
            nave.quant_vida = nave.quant_vida -1
            barra_vida.diminuir_vida()
            perder_vida_som.play()

        #colisoes da bala com os asteroides
        for bal in lista_balas:
            if bal.rect.overlap(ast.rect, (ast.x-bal.x, ast.y-bal.y)):
                criar_explosao(lista_explosoes, ast)
                lista_balas.remove(bal)
                if ast in lista_asteroides:
                    lista_asteroides.remove(ast)

    #checar se a vida acabou
    if nave.quant_vida == 0:
        lista_asteroides = []
        barra_vida.reset()
        barra_moeda.reset()
        pygame.mixer.music.stop()
        game_over_som.play()