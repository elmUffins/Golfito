import pygame

pygame.init()

screen_w = 1000
screen_h = 500

screen = pygame.display.set_mode((screen_w, screen_h))
pygame.display.set_caption("Golfito")

tile_size = 50

bg_img = pygame.image.load("images/back.png")

#Game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.blit(bg_img, (0, 0))

    pygame.display.flip()

pygame.quit()
