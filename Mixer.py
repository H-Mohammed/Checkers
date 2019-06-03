# This is used to play sounds and music #
import pygame


class Music:
    def __init__(self):
        self.music_directory = 'music'
        self.music = ""
        pygame.mixer.music.set_endevent(444)

    # Method gets the end of a song #
    @staticmethod
    def at_end():
        end_of_song = pygame.mixer.music.get_endevent(444)
        if end_of_song:
            return True
        return False

    # Method gets if the music player is streaming #
    @staticmethod
    def get_busy():
        return pygame.mixer.music.get_busy()

    # Method plays a music #
    def play(self):
        pygame.mixer.music.load(self.music)
        pygame.mixer.music.play(0)

    # Method sets music to be played
    def set_sound(self, name):
        self.music = 'music/' + name + '.mp3'

    # Method sets the volume of music player
    @staticmethod
    def set_volume(volume):
        pygame.mixer.music.set_volume(volume)
