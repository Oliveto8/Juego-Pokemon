import pygame, sys
import random
import csv
from pygame.locals import *
from variables import *
from texto import *
from inicio import *
from Pokemones import *
from imagenes_pokemon import *

pygame.init()
pygame.mixer.init()

#Crear ventana
screen = pygame.display.set_mode(ventana) # resolucion de la pantalla (width, height)
pygame.display.set_caption("Pokémon Guess")

#Icono 
icono = pygame.image.load("Pirmer Parcial\Recursos\Poké_Ball_icon.png.png")
pygame.display.set_icon(icono)

#Musica
pygame.mixer.music.load("Pirmer Parcial\Recursos\Y2meta.app - Chill & Relaxing Pokémon Music Mix (128 kbps).mp3")
pygame.mixer.music.set_volume(0.2)
pygame.mixer.music.play()


mostrar_pantalla_inicio()

while flag:
    lista_eventos = pygame.event.get()
    
    for event in lista_eventos:
        if event.type == pygame.QUIT:
            flag = False

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and inicio == False:                  
                input_active = not input_active
                if input_active:
                    
                    inicio_finalizado = True
                    inicio = True
                    transicion_blanco()
        if inicio_finalizado == True:

#--------------Barra blanca de texto
            if event.type == pygame.MOUSEBUTTONDOWN: 
                if event.button == 1 and barra_blanca.collidepoint(event.pos):  # Clic derecho
                    input_active = True
            elif event.type == pygame.KEYDOWN and inicio_finalizado == True:
                
                if input_active:
                    if event.key == pygame.K_RETURN:
                        input_active = False
                    elif event.key == pygame.K_BACKSPACE:
                        nombre_pokemon = nombre_pokemon[:-1]
                    else:
                        # Controlar la longitud del texto en relación con el ancho del rectángulo
                        if nombre_pokemon == "" or fuente50.size(nombre_pokemon)[0] < barra_blanca.width + 30 :
                            nombre_pokemon += event.unicode
                            if nombre_pokemon.lower() == pokemon_aleatorio:

                                contador += 1
                                racha_actual_util = fuente50.render(f"{contador}", True, "white")
                                nombre_pokemon = ""
                                if contador > acumulador_best:
                                    acumulador_best = contador
                                    racha_mejor_util = fuente50.render(f"{acumulador_best}", True, "white")
                                
                                while True:
                                    
                                    gen_aleatoria = random.randint(1, 6)
                                    match gen_aleatoria:
                                        case 1:
                                            if bandera_gen1 == True :
                                                pokemon_aleatorio = random.choice(Primera)
                                                print(f"{pokemon_aleatorio}")
                                                imagen_aleatoria = pokemon_imagenes[pokemon_aleatorio]
                                                break
                                            else:
                                                gen_aleatoria = random.randint(1, 6)
                                        case 2:
                                            if bandera_gen2 == True:
                                                pokemon_aleatorio = random.choice(Segunda)
                                                print(f"{pokemon_aleatorio}")
                                                imagen_aleatoria = pokemon_imagenes[pokemon_aleatorio]
                                                break
                                            else:
                                                gen_aleatoria = random.randint(1, 6)
                                        case 3:
                                            if bandera_gen3 == True:
                                                pokemon_aleatorio = random.choice(Tercera)
                                                print(f"{pokemon_aleatorio}")
                                                imagen_aleatoria = pokemon_imagenes[pokemon_aleatorio]
                                                break
                                            else:
                                                gen_aleatoria = random.randint(1, 6)
                                        case 4:
                                            if bandera_gen4 == True:
                                                pokemon_aleatorio = random.choice(Cuarta)
                                                print(f"{pokemon_aleatorio}")
                                                imagen_aleatoria = pokemon_imagenes[pokemon_aleatorio]
                                                break
                                            else:
                                                gen_aleatoria = random.randint(1, 6)
                                        case 5:
                                            if bandera_gen5 == True:
                                                pokemon_aleatorio = random.choice(Quinta)
                                                print(f"{pokemon_aleatorio}")
                                                imagen_aleatoria = pokemon_imagenes[pokemon_aleatorio]
                                                break
                                            else:
                                                gen_aleatoria = random.randint(1, 6)
                                        case 6:
                                            if bandera_gen6 == True:
                                                pokemon_aleatorio = random.choice(Sexta)
                                                print(f"{pokemon_aleatorio}")
                                                imagen_aleatoria = pokemon_imagenes[pokemon_aleatorio]
                                                break
                                            else:
                                                gen_aleatoria = random.randint(1, 6)

#------------Activar o desactivar sonido
            if event.type == pygame.MOUSEBUTTONDOWN:  
                if event.button == 1 and rectangulo_sonido_off.collidepoint(event.pos) and bandera_sonido == True:  # Clic derecho
                    bandera_sonido = False
                    pygame.mixer.music.pause()
                elif event.button == 1 and rectangulo_sonido_on.collidepoint(event.pos) and bandera_sonido == False:  # Clic derecho
                    bandera_sonido = True
                    pygame.mixer.music.unpause()

#-------------Cambio Generaciones
            if event.type == pygame.MOUSEBUTTONDOWN: 
                if event.button == 1 and rectangulo_generacion1.collidepoint(event.pos) and bandera_gen1 == False:
                    bandera_gen1 = True
                elif event.button == 1 and rectangulo_generacion1.collidepoint(event.pos) and bandera_gen1 == True:
                    bandera_gen1 = False
                if event.button == 1 and rectangulo_generacion2.collidepoint(event.pos) and bandera_gen2 == True:
                    bandera_gen2 = False
                elif event.button == 1 and rectangulo_generacion2.collidepoint(event.pos) and bandera_gen2 == False:
                    bandera_gen2 = True
                if event.button == 1 and rectangulo_generacion3.collidepoint(event.pos) and bandera_gen3 == True:
                    bandera_gen3 = False
                elif event.button == 1 and rectangulo_generacion3.collidepoint(event.pos) and bandera_gen3 == False:
                    bandera_gen3 = True
                if event.button == 1 and rectangulo_generacion4.collidepoint(event.pos) and bandera_gen4 == True:
                    bandera_gen4 = False
                elif event.button == 1 and rectangulo_generacion4.collidepoint(event.pos) and bandera_gen4 == False:
                    bandera_gen4 = True
                if event.button == 1 and rectangulo_generacion5.collidepoint(event.pos) and bandera_gen5 == True:
                    bandera_gen5 = False
                elif event.button == 1 and rectangulo_generacion5.collidepoint(event.pos) and bandera_gen5 == False:
                    bandera_gen5 = True
                if event.button == 1 and rectangulo_generacion6.collidepoint(event.pos) and bandera_gen6 == True:
                    bandera_gen6 = False
                elif event.button == 1 and rectangulo_generacion6.collidepoint(event.pos) and bandera_gen6 == False:
                    bandera_gen6 = True
                if event.button == 1 and rect_texto2.collidepoint(event.pos):
                    bandera_nolose = False
                    flag = False
                    print("Juego Finalizado")


            screen.fill(fondo)

            pygame.draw.rect(screen, gris_oscuro, rectangulo_generacion, 0, 15) #Barra generacion
            pygame.draw.rect(screen, gris_oscuro, rectangulo_generacionx, 0, 15) #Barra generacionx

            pygame.draw.rect(screen, gris_oscuro, rectangulo_dificultad, 0, 15) #Barra dificultad
            pygame.draw.rect(screen, gris_oscuro, rectangulo_dificultadx, 0, 15) #Barra dificultad
            pygame.draw.rect(screen, "white", rectangulo_dificultad2) #Barra dificultad


            if bandera_gen1 == True:
                pygame.draw.rect(screen, "white", rectangulo_generacion1, 0, 15) #Barra generacion
                pygame.draw.rect(screen, "white", rectangulo_generacion1_2) #Barra generacion
                pygame.draw.rect(screen, "white", rectangulo_generacion1_3) #Barra generacion
                gen1 = fuente25.render("Gen 1", True, gris_oscuro)
            else:
                pygame.draw.rect(screen, gris_oscuro, rectangulo_generacion1, 0, 15)
                gen1 = fuente25.render("Gen 1", True, "white")

            if bandera_gen2 == True:
                pygame.draw.rect(screen, "white", rectangulo_generacion2) #Barra generacion
                gen2 = fuente25.render("Gen 2", True, gris_oscuro)
            else:
                pygame.draw.rect(screen, gris_oscuro, rectangulo_generacion2, 0, 15)
                gen2 = fuente25.render("Gen 2", True, "white")

            if bandera_gen3 == True:
                pygame.draw.rect(screen, "white", rectangulo_generacion3) #Barra generacion
                gen3 = fuente25.render("Gen 3", True, gris_oscuro)
            else:
                pygame.draw.rect(screen, gris_oscuro, rectangulo_generacion3, 0, 15)
                gen3 = fuente25.render("Gen 3", True, "white")

            if bandera_gen4 == True:
                pygame.draw.rect(screen, "white", rectangulo_generacion4) #Barra generacion
                gen4 = fuente25.render("Gen 4", True, gris_oscuro)
            else:
                pygame.draw.rect(screen, gris_oscuro, rectangulo_generacion4, 0, 15)
                gen4 = fuente25.render("Gen 4", True, "white")

            if bandera_gen5 == True:
                pygame.draw.rect(screen, "white", rectangulo_generacion5) #Barra generacion
                gen5 = fuente25.render("Gen 5", True, gris_oscuro)
            else:
                pygame.draw.rect(screen, gris_oscuro, rectangulo_generacion5, 0, 15)
                gen5 = fuente25.render("Gen 5", True, "white")

            if bandera_gen6 == True:
                pygame.draw.rect(screen, "white", rectangulo_generacion6, 0, 15) #Barra generacion
                pygame.draw.rect(screen, "white", rectangulo_generacion6_2) #Barra generacion
                pygame.draw.rect(screen, "white", rectangulo_generacion6_3) #Barra generacion
                gen6 = fuente25.render("Gen 6", True, gris_oscuro)
            else:
                pygame.draw.rect(screen, gris_oscuro, rectangulo_generacion6, 0, 15)
                gen6 = fuente25.render("Gen 6", True, "white")



            pygame.draw.rect(screen, "white", rectangulo_sonido, 0, 15) #Barra sonido

            if bandera_sonido == True:
                pygame.draw.rect(screen, "white", rectangulo_sonido_off, 0, 15) #Barra sonido on
                pygame.draw.rect(screen, gris_oscuro, rectangulo_sonido_on, 0, 15) #Barra sonido on
                off = fuente25.render("Of f", True, gris_oscuro)
                on = fuente25.render("On", True, "white")
            else:
                pygame.draw.rect(screen, gris_oscuro, rectangulo_sonido_off, 0, 15) #Barra sonido off
                pygame.draw.rect(screen, "white", rectangulo_sonido_on, 0, 15) #Barra sonido off
                on = fuente25.render("On", True, gris_oscuro)
                off = fuente25.render("Of f", True, "white")

            pygame.draw.rect(screen, gris_oscuro, rectangulo_racha, 0, 15) #Barra racha
            pygame.draw.rect(screen, gris_oscuro, rectangulo_mejor, 0, 15) #Barra mejor

            pygame.draw.rect(screen, gris_oscuro, rectangulo_anterior, 0, 15) #Barra anterior
            pygame.draw.rect(screen, gris_oscuro, rectangulo_mejor_tiempo, 0, 15) #Barra mejor tiempo
            pygame.draw.rect(screen, gris_oscuro, rectangulo_promedio, 0, 15) #Barra mejor tiempo


            pygame.draw.rect(screen, celeste, (175, 50, 550, 700), 0, 10) #Rectangulo celeste
            pygame.draw.rect(screen, "white", barra_blanca, 0, 10) #Barra para escribir
            

            font = pygame.font.Font(None, 50) # Barra blanca
            nombre_pokemon = nombre_pokemon.lstrip().lower() # Barra blanca
            input_text = font.render(nombre_pokemon, True, "black") # Barra blanca
            
            input_text_rect = input_text.get_rect() # Barra blanca
            input_text_rect.center = barra_blanca.center # Barra blanca

            screen.blit(texto, rect_texto) # cual es este pokemon
            screen.blit(texto2, rect_texto2) # no lo se

            screen.blit(texto3, rect_texto3) # generacion
            screen.blit(texto4, rect_texto4) # dificultad
            screen.blit(texto5, rect_texto5) # sonido
            screen.blit(texto6, rect_texto6) # racha
            screen.blit(texto7, rect_texto7) # tiempo

            screen.blit(input_text, input_text_rect) # texto rectangulo

            screen.blit(imagen_1, bandera_francia)
            screen.blit(imagen_2, bandera_reinounido)
            screen.blit(imagen_3, bandera_españa)
            screen.blit(imagen_4, bandera_italia)
            screen.blit(imagen_5, bandera_alemania)

            screen.blit(gen1, rectangulo_gen1.topleft) # gen 1
            screen.blit(gen2, rectangulo_gen2.topleft) # gen 2
            screen.blit(gen3, rectangulo_gen3.topleft) # gen 3
            screen.blit(gen4, rectangulo_gen4.topleft) # gen 4
            screen.blit(gen5, rectangulo_gen5.topleft) # gen 5
            screen.blit(gen6, rectangulo_gen6.topleft) # gen 6

            screen.blit(facil, rectangulo_facil.topleft) # facil
            screen.blit(medio, rectangulo_medio.topleft) # medio
            screen.blit(dificil, rectangulo_dificil.topleft) # dificl

            screen.blit(off, rectangulo_off.topleft) # off
            screen.blit(on, rectangulo_on.topleft) # on
            
            screen.blit(racha_actual, rectangulo_racha_actual.topleft)
            screen.blit(racha_actual_util, rectangulo_racha_actual_util.topleft)  

            screen.blit(racha_mejor, rectangulo_racha_mejor.topleft)
            screen.blit(racha_mejor_util, rectangulo_racha_mejor_util.topleft)

            screen.blit(tiempo_anterior, rectangulo_tiempo_anterior.topleft)
            screen.blit(tiempo_mejor, rectangulo_tiempo_mejor.topleft)
            screen.blit(promedio, rectangulo_promedio_tiempo.topleft)

            
            imagen_aleatoria.fill("black", None, special_flags = pygame.BLEND_RGBA_MULT) # Oscurecer imagenes
            screen.blit(imagen_aleatoria, rectangulo_imagenes) # imagenes pokemones

            pygame.display.flip()
            reloj.tick(60)

pygame.quit()