import pygame

pygame.mixer.init()
pygame.init()
pygame.mixer.music.load('God only Knows - Secrets of the Goddess.mp3')

pygame.mixer.music.play(start=0)
pygame.event.wait()




