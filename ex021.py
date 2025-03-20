'''
Exercício 021
Resolução Rafael Costa
============================================
Faça um programa em Python que abra e repro-
duza o áudio de um arquivo MP3.
============================================
'''

import pygame

# Inicializa o mixer
pygame.mixer.init()

# Carrega o arquivo MP3
pygame.mixer.music.load("amor_fe.mp3")

# Reproduz o áudio
pygame.mixer.music.play()

# Mantém o programa rodando enquanto o áudio toca
input("Pressione Enter para sair...")