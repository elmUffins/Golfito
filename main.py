import pygame

pygame.init()

screen_w = 1000
screen_h = 500

screen = pygame.display.set_mode((screen_w, screen_h))
pygame.display.set_caption("Golfito")

tile_size = 50

bg_img = pygame.image.load("images/back.png")
grass_img = pygame.image.load("images/grass.png")
dirt_img = pygame.image.load("images/dirt.png")

# Draw Grid Function
def draw_grid():
    for line in range(0, 20):
        pygame.draw.line(screen, (0, 0, 0), (0, line * tile_size), (screen_w, line * tile_size))
        pygame.draw.line(screen, (0, 0, 0), (line * tile_size, 0), (line * tile_size, screen_h))


# World data and class
world_data = \
    [

    ]

class World():
    def __init__(self, data):
        self.tile_list = []

        dirt_img = pygame.image.load("images/dirt.png")
        grass_img = pygame.image.load("images/grass.png")

        for row in range(len(data)):
            for col in range(len(data[row])):
                if data[row][col] == 1:
                    img = pygame.transform.scale(dirt_img, (tile_size, tile_size))
                    img_rect = img.get_rect()
                    img_rect.x = col * tile_size
                    img_rect.y = row * tile_size
                    tile = (img, img_rect)
                    self.tile_list.append(tile)
                if data[row][col] == 2:
                    img = pygame.transform.scale(grass_img, (tile_size, tile_size))
                    img_rect = img.get_rect()
                    img_rect.x = col * tile_size
                    img_rect.y = row * tile_size
                    tile = (img, img_rect)
                    self.tile_list.append(tile)

    def draw(self):
        for tile in self.tile_list:
            screen.blit(tile[0], tile[1])

world = World(world_data)

# Game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.blit(bg_img, (0, 0))
    world.draw()

    draw_grid()
    pygame.display.flip()

pygame.quit()
