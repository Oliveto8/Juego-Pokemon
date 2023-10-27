import pygame, sys
import csv
from variables import *
from texto import *

pygame.init()

reloj = pygame.time.Clock()
pantalla = pygame.display.set_mode((ventana))
pantalla_inicial = pygame.display.set_mode(ventana)

pygame.display.set_caption('Ventana de Inicio')
play_game = pygame.Rect((LARGO // 2 - 200, 710), (400, 100))

def mostrar_pantalla_inicio():
    fondo_inico = pygame.image.load('Pirmer Parcial\Recursos\Fondo_inicio.png')
    pantalla_inicial.blit(fondo_inico, (0,0))  # Fondo blanco

    texto = fuente30.render('PRESS SPACE TO START', True, "white")
    pg = texto.get_rect()
    pg.center = play_game.center
    pantalla_inicial.blit(texto, pg.topleft)
    pygame.display.flip()

# Transición a blanco
def transicion_blanco():
    for alpha in range(0, 255, 15):  # Cambia la opacidad de 0 a 255 en pasos de 5
        superficie_blanca = pygame.Surface(ventana)
        superficie_blanca.fill(((215,219,221)))  # Fondo blanco
        superficie_blanca.set_alpha(alpha)  # Ajusta la opacidad

        pantalla.blit(superficie_blanca, (0, 0))  # Blit la superficie blanca
        pygame.display.flip()
        reloj.tick(100)

