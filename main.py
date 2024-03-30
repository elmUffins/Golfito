import pygame
from pygame import *

pygame.init()

screen_w = 1000
screen_h = 1000

screen = pygame.display.set_mode((screen_w, screen_h))
pygame.display.set_caption("Golfito")

# Game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((255, 255, 255))
    pygame.display.flip()

pygame.quit()
