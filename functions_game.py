from settings import *

#limite de objetos
_limite = 20

'''
padrao de projeto:

funcao criar objeto
funcao deletar objeto apos um determinado tempo
'''

def criar_asteroide(list_asteroides):
    ast = Asteroide()
    list_asteroides.append(ast)
    deletar_asteroide(list_asteroides)

def deletar_asteroide(list_asteroides):
    if len(list_asteroides)>=_limite:
        list_asteroides.remove(list_asteroides[0])

def gerar_bala(lista_balas, nave_x, nave_y):
    bala = Bala(nave_x, nave_y)
    lista_balas.append(bala)
    apagar_bala(lista_balas)

def apagar_bala(lista_balas):
    if len(lista_balas)>=_limite:
        lista_balas.remove(lista_balas[0])

def gerar_moeda(lista_moedas):
    moeda = Moeda()
    lista_moedas.append(moeda)
    deletar_moeda(lista_moedas)

def deletar_moeda(lista_moedas):
    if len(lista_moedas)>=_limite:
        lista_moedas.remove(lista_moedas[0])

def criar_explosao(lista_explosoes, obj):
    explosao = Explosao(obj=obj)
    lista_explosoes.append(explosao)
    deletar_explosao(lista_explosoes)

def deletar_explosao(lista_explosoes):
    if len(lista_explosoes)>=3:
        lista_explosoes.remove(lista_explosoes[0])

def criar_bala_inimiga(lista_balas_inimigas, nave):
    bala = Bala_inimiga(nave)
    lista_balas_inimigas.append(bala)
    deletar_bala_inimiga(lista_balas_inimigas)

def deletar_bala_inimiga(lista_balas_inimigas):
    if len(lista_balas_inimigas)>=10:
        lista_balas_inimigas.remove(lista_balas_inimigas[0])

def criar_nave_inimiga(lista_naves_inimigas):
    nave = Nave_inimiga()
    lista_naves_inimigas.append(nave)
    deletar_nave_inimiga(lista_naves_inimigas)

def deletar_nave_inimiga(lista_naves_inimigas):
    if len(lista_naves_inimigas)>=10:
        lista_naves_inimigas.remove(lista_naves_inimigas[0])