import pygame
#set background music
#background_sound=pygame.mixer.music.load('INSERT SONG HERE')
##set Sound Effects
pygame.mixer.init(44100, -16, 2, 2048)
sword_sound_1=pygame.mixer.Sound('Sounds/master sword.wav')
sword_sound_2=pygame.mixer.Sound('Sounds/golden sword.wav')
jump_sound=pygame.mixer.Sound('Sounds/bounce.wav')
i_got_hit_sound=pygame.mixer.Sound('Sounds/link hurt.wav')
Enemy_got_hit_sound=pygame.mixer.Sound('Sounds/enemy hit.wav')
bow_sound = pygame.mixer.Sound('Sounds/hammer pound.wav')
walk_sound = pygame.mixer.Sound('Sounds/boomerang.wav')
death_sound= pygame.mixer.Sound('Sounds/link dies.wav')

pygame.mixer.music.load('Sounds/Hollow_Knight_Mantis_Lords.wav')
pygame.mixer.Sound.get_volume(Enemy_got_hit_sound)

