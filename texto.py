import pygame, sys
from variables import *

pygame.init()

fuente50 = pygame.font.SysFont('Cantora One', 50)
fuente30 = pygame.font.SysFont('Cantora One', 30)
fuente25 = pygame.font.SysFont('Cantora One', 25)

#texto
texto = fuente50.render("Who's That Pokémon?", True, "white")
rect_texto = texto.get_rect()
rect_texto.midbottom = (LARGO // 2, 140)

#texto 2
texto2 = fuente25.render("I don't know!", True, "white")
rect_texto2 = texto2.get_rect()
rect_texto2.midbottom = (LARGO // 2, 735)

#texto 3
texto3 = fuente30.render("Generation", True, "white")
rect_texto3 = texto3.get_rect()
rect_texto3.midbottom = (100, 100)

#texto 4
texto4 = fuente30.render("Difficulty", True, "white")
rect_texto4 = texto4.get_rect()
rect_texto4.midbottom = (100, 440)

#texto 5
texto5 = fuente30.render("Sound", True, "white")
rect_texto5 = texto5.get_rect()
rect_texto5.midbottom = (100, 630)

#texto 6
texto6 = fuente30.render("Streak", True, "white")
rect_texto6 = texto6.get_rect()
rect_texto6.midbottom = (800, 100)

#texto 7
texto7 = fuente30.render("Time", True, "white")
rect_texto7 = texto7.get_rect()
rect_texto7.midbottom = (800, 350)

###GENERACIONES###
gen1 = fuente25.render("Gen 1", True, "white")
rectangulo_gen1 = gen1.get_rect()
rectangulo_gen1.center = rectangulo_generacion1.center

gen2 = fuente25.render("Gen 2", True, "white")
rectangulo_gen2 = gen2.get_rect()
rectangulo_gen2.center = rectangulo_generacion2.center

gen3 = fuente25.render("Gen 3", True, "white")
rectangulo_gen3 = gen3.get_rect()
rectangulo_gen3.center = rectangulo_generacion3.center

gen4 = fuente25.render("Gen 4", True, "white")
rectangulo_gen4 = gen4.get_rect()
rectangulo_gen4.center = rectangulo_generacion4.center

gen5 = fuente25.render("Gen 5", True, "white")
rectangulo_gen5 = gen5.get_rect()
rectangulo_gen5.center = rectangulo_generacion5.center

gen6 = fuente25.render("Gen 6", True, "white")
rectangulo_gen6 = gen6.get_rect()
rectangulo_gen6.center = rectangulo_generacion6.center

###DIFICULTAD###
facil = fuente25.render("Easy", True, "white")
rectangulo_facil = facil.get_rect()
rectangulo_facil.center = rectangulo_dificultad1.center

medio = fuente25.render("Normal", True, gris_oscuro)
rectangulo_medio = medio.get_rect()
rectangulo_medio.center = rectangulo_dificultad2.center

dificil = fuente25.render("Difficult", True, "white")
rectangulo_dificil = dificil.get_rect()
rectangulo_dificil.center = rectangulo_dificultad3.center

###SONIDO##
off = fuente25.render("Of f", True, "white")
rectangulo_off = off.get_rect()
rectangulo_off.center = rectangulo_sonido_off.center

on = fuente25.render("On", True, "white")
rectangulo_on = on.get_rect()
rectangulo_on.center = rectangulo_sonido_on.center

###RACHA###
racha_actual = fuente25.render("Current", True, "white")
rectangulo_racha_actual = racha_actual.get_rect()
rectangulo_racha_actual.center = (800,120)

racha_actual_util = fuente50.render(f"{contador}", True, "white")
rectangulo_racha_actual_util = racha_actual_util.get_rect()
rectangulo_racha_actual_util.center = (800,160)


racha_mejor = fuente25.render("Best", True, "white")
rectangulo_racha_mejor = racha_mejor.get_rect()
rectangulo_racha_mejor.center = (800,230)

racha_mejor_util = fuente50.render(f"{acumulador_best}", True, "white")
rectangulo_racha_mejor_util = racha_mejor_util.get_rect()
rectangulo_racha_mejor_util.center = (800,270)

###TIEMPO###
tiempo_anterior = fuente25.render("Previous", True, "white")
rectangulo_tiempo_anterior = tiempo_anterior.get_rect()
rectangulo_tiempo_anterior.center = (800,370)

tiempo_mejor = fuente25.render("Best", True, "white")
rectangulo_tiempo_mejor = tiempo_mejor.get_rect()
rectangulo_tiempo_mejor.center = (800,480)

promedio = fuente25.render("Average", True, "white")
rectangulo_promedio_tiempo = promedio.get_rect()
rectangulo_promedio_tiempo.center = (800, 610)