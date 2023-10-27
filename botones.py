import pygame, sys
from pygame.locals import *
from variables import *
from texto import *
from inicio import *
from Pokemones import *
from imagenes_pokemon import *


pygame.init()

bandera_gen1 = True
bandera_gen2 = False

def botones_generaciones():
  lista_eventos = pygame.event.get()
  for event in lista_eventos:
    if event.type == pygame.MOUSEBUTTONDOWN: 
      if event.button == 1 and rectangulo_generacion1.collidepoint(event.pos) and bandera_gen1 == False:
          bandera_gen1 = True
      elif event.button == 1 and rectangulo_generacion1.collidepoint(event.pos) and bandera_gen1 == True:
          bandera_gen1 = False
          
      if event.button == 1 and rectangulo_generacion2.collidepoint(event.pos) and bandera_gen2 == True:
          bandera_gen2 = False
      elif event.button == 1 and rectangulo_generacion2.collidepoint(event.pos) and bandera_gen2 == False:
          bandera_gen2 = True
