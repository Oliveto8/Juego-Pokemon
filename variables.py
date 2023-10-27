import pygame, sys
from imagenes_pokemon import*
from Pokemones import *

LARGO = 900
ALTO = 800

celeste = (52,152,219)
fondo = (215,219,221)
gris_oscuro = (52,73,94)

ventana = (LARGO, ALTO)

flag = True
nombre_pokemon = ""
bandera_sonido = True
input_active = False
inicio_finalizado = False

inicio = False


bandera_gen1 = True
bandera_gen2 = False
bandera_gen3 = False
bandera_gen4 = False
bandera_gen5 = False
bandera_gen6= False

rectangulo_imagenes = pygame.Rect((275,200), (350,350))

barra_blanca = pygame.Rect((LARGO // 2 - 200, 630), (400, 60))

rectangulo_generacion = pygame.Rect((20, 100), (180, 300))
rectangulo_generacionx = pygame.Rect((20, 180), (180, 220))
rectangulo_generacion1 = pygame.Rect((20, 100), (160, 50))
rectangulo_generacion1_2 = pygame.Rect((20, 120), (200, 30))
rectangulo_generacion1_3 = pygame.Rect((140, 100), (60, 30))
rectangulo_generacion2 = pygame.Rect((20, 150), (160, 50))
rectangulo_generacion3 = pygame.Rect((20, 200), (160, 50))
rectangulo_generacion4 = pygame.Rect((20, 250), (160, 50))
rectangulo_generacion5 = pygame.Rect((20, 300), (160, 50))
rectangulo_generacion6 = pygame.Rect((20, 350), (160, 50))
rectangulo_generacion6_2 = pygame.Rect((20, 350), (200, 30))
rectangulo_generacion6_3 = pygame.Rect((140, 350), (60, 50))

rectangulo_dificultad = pygame.Rect((20, 440), (180, 150))
rectangulo_dificultadx = pygame.Rect((20, 500), (180, 90))
rectangulo_dificultad1 = pygame.Rect((20, 440), (160, 50))
rectangulo_dificultad2 = pygame.Rect((20, 490), (160, 50))
rectangulo_dificultad3 = pygame.Rect((20, 540), (160, 50))

rectangulo_sonido = pygame.Rect((20, 630), (180, 60))
rectangulo_sonido_off = pygame.Rect((20, 630), (80, 60))
rectangulo_sonido_on = pygame.Rect((100, 630), (80, 60))

rectangulo_racha = pygame.Rect((700, 100), (180, 100))
rectangulo_mejor = pygame.Rect((700, 210), (180, 100))

rectangulo_anterior = pygame.Rect((700, 350), (180, 100))
rectangulo_mejor_tiempo = pygame.Rect((700, 460), (180, 120))
rectangulo_promedio = pygame.Rect((700, 590), (180, 100))

###BANDERAS###
imagen_1 = pygame.image.load("Pirmer Parcial\Banderas\Flag_of_France.svg.png")
imagen_1 = pygame.transform.scale(imagen_1,(32,15)) #ajustar imagen
bandera_francia = pygame.Rect((350, 770), (32, 15))

imagen_2 = pygame.image.load("Pirmer Parcial\Banderas\Flag_of_Great_Britain_(1707–1800).svg.png")
imagen_2 = pygame.transform.scale(imagen_2,(32,15)) #ajustar imagen
bandera_reinounido = pygame.Rect((392, 770), (32, 15))

imagen_3 = pygame.image.load("Pirmer Parcial\Banderas\Bandera_Nacional_de_España.png")
imagen_3 = pygame.transform.scale(imagen_3,(32,15)) #ajustar imagen
bandera_españa = pygame.Rect((434, 770), (32, 15))

imagen_4 = pygame.image.load("Pirmer Parcial\Banderas\Flag_of_Italy.svg.png")
imagen_4 = pygame.transform.scale(imagen_4,(32,15)) #ajustar imagen
bandera_italia = pygame.Rect((476, 770), (32, 15))

imagen_5 = pygame.image.load("Pirmer Parcial\Banderas\Bandera-de-Alemania-760x480.png")
imagen_5 = pygame.transform.scale(imagen_5,(32,15)) #ajustar imagen
bandera_alemania = pygame.Rect((518, 770), (32, 15))

