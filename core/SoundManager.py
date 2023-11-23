import pygame
import os

class SoundManager:
    def __init__(self):
        pygame.mixer.init()
        self.sounds = {}

    def load_sounds_from_folder(self, folder_path):
        for filename in os.listdir(folder_path):
            if filename.endswith(".wav") or filename.endswith(".mp3"):
                name = os.path.splitext(filename)[0]
                sound_path = os.path.join(folder_path, filename)
                sound = pygame.mixer.Sound(sound_path)
                self.sounds[name] = sound
                return print(f"Sound loaded: {name}")
        print("Not a valid path.")

    def play_sound(self, name, loops=0, maxtime=0, fade_ms=0):
        sound = self.sounds.get(name)
        if sound:
            sound.play(loops=loops, maxtime=maxtime, fade_ms=fade_ms)
        else:
            print("Error: Sound not found. Have you loaded the sound?")