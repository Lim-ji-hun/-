import pygame
import os
import sys


pygame.init()

w = 1600
h = w * (9/16)
screen = pygame.display.set_mode((w, h))
pygame.display.set_caption("Start Screen")

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

Cpath = os.path.dirname(__file__)
Fpath = os.path.join(Cpath, "font")
font_path = os.path.join(Fpath, "ingame_font.ttf")
title_font = pygame.font.Font(font_path, int(w / 10))
info_font = pygame.font.Font(font_path, int(w / 40))

title_text = title_font.render("My Rhythm Game", True, WHITE)
start_text = info_font.render("Press F to Start", True, WHITE)
exit_text = info_font.render("Press J to Quit", True, WHITE)

def draw_start_screen():
    screen.fill(BLACK)
    screen.blit(title_text, (w / 2 - title_text.get_width() / 2, h / 4))
    screen.blit(start_text, (w / 2 - start_text.get_width() / 2, h / 2))
    screen.blit(exit_text, (w / 2 - exit_text.get_width() / 2, h / 1.5))
    pygame.display.flip()

def start_screen():
    running = True
    while running:
        draw_start_screen()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_f:
                    running = False
                elif event.key == pygame.K_j:
                    pygame.quit()
                    sys.exit()

start_screen()

os.system('python "C:/Users/home/Desktop/기말 과제/test_pygame.py"')

