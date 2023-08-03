import tkinter as tk

from gtts import gTTS
import pygame
import os

def hablar():
    text = text_to_speach.get()
    tipo = recording.get()
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

gui = tk.Tk(className="Text to speach")
gui.geometry("500x250")

greeting = tk.Label(text="Text To Speach")
greeting.pack()

label_recording = tk.Label(text="Name Recording")
recording = tk.Entry()
label_recording.pack()
recording.pack()

label_text = tk.Label(text="Text")
text_to_speach = tk.Entry()
label_text.pack()
text_to_speach.pack()

button = tk.Button(
    text="Generate recording",
    width=25,
    height=5,
    bg="gray",
    fg="white",
    command=hablar
)
button.pack()

window = tk.mainloop()