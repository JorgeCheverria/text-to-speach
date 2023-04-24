from gtts import gTTS
import pygame
import os


def hablar(text,tipo='default'):
    #text = "Hola, estoy aquí para ayudarte a sintetizar texto a voz en Python."
    speech = gTTS(text=text, tld='com.mx', lang='es', slow=False, lang_check=False,)
    # Eliminar el archivo "speech.mp3" si existe
    if os.path.exists(f'{tipo}.mp3'):
        os.remove(f'{tipo}.mp3')
    speech.save(f"{tipo}.mp3")
    os.chmod(f'{tipo}.mp3', 0o777)

    # Inicializar pygame
    pygame.init()

    # Cargar el archivo de audio
    pygame.mixer.music.load(f'{tipo}.mp3')

    # Reproducir el archivo de audio
    pygame.mixer.music.play()

    # Esperar a que termine la reproducción
    while pygame.mixer.music.get_busy():
        pygame.time.Clock().tick(10)

""" hablar('Marque 1.... no pasa preventa....'
       +'Marque 2....pedido no entregado....'
       +'Marque 3....pedidos incompletos....'
       +'Marque 4....novedades con productos....'
       +'Marque 5....otros reportes....',
       'arca_opcion_novedad_novedades_pedidos') """
       
hablar('¡Por favor elige una de nuestra siguientes opciones'
       +'!',
       'arca_repite_menu_anterior')