import pygame
import os
import random
from Pokemones import *

# Directorio donde se encuentran las imágenes
imagenes_gen1 = 'Pirmer Parcial\\artwork\Gen1'
imagenes_gen2 = 'Pirmer Parcial\\artwork\Gen2'
imagenes_gen3 = 'Pirmer Parcial\\artwork\Gen3'
imagenes_gen4 = 'Pirmer Parcial\\artwork\Gen4'
imagenes_gen5 = 'Pirmer Parcial\\artwork\Gen5'
imagenes_gen6 = 'Pirmer Parcial\\artwork\Gen6'


# Crear un diccionario para almacenar los nombres de los Pokémon y sus rutas de imagen
pokemon_imagenes = {}


def cambiar_generacion(key,lista):
    for pokemon in key:
        # Los nombres de los archivos están numerados del 1 al 151
        numero_pokemon = key.index(pokemon) + 1
        nombre_archivo = f'{numero_pokemon}.png'
        ruta_imagen = os.path.join(lista, nombre_archivo)
        
        if os.path.exists(ruta_imagen):  # Verificar si el archivo existe
            pokemon_imagenes[pokemon] = pygame.image.load(ruta_imagen)
        else:
            print(f"Advertencia: No se encontró la imagen para {pokemon}")

cambiar_generacion(Primera,imagenes_gen1)
cambiar_generacion(Segunda,imagenes_gen2)
cambiar_generacion(Tercera,imagenes_gen3)
cambiar_generacion(Cuarta,imagenes_gen4)
cambiar_generacion(Quinta,imagenes_gen5)
cambiar_generacion(Sexta,imagenes_gen6)

# Obtener un Pokémon aleatorio y su imagen
pokemon_aleatorio = random.choice(Primera)
print(f"{pokemon_aleatorio}")
imagen_aleatoria = pokemon_imagenes[pokemon_aleatorio]






