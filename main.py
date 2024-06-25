import pygame

pygame.init()
pygame.font.init()

screen_w = 1000
screen_h = 500

screen = pygame.display.set_mode((screen_w, screen_h))
pygame.display.set_caption("Golfito")
pygame.display.set_icon(pygame.image.load("images/golfball.png"))
font = pygame.font.Font(None, 36)
clock = pygame.time.Clock()

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
world_data = [
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
]

# World class
class World():
    def __init__(self, data):
        self.tile_list = []

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


# Ball class
class Ball():
    def __init__(self, x, y):
        img = pygame.image.load("images/golfball.png")
        self.image = pygame.transform.scale(img, (20, 20))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.position = pygame.math.Vector2(self.rect.x, self.rect.y)
        self.vel_x = 0
        self.vel_y = 0
        self.acc_y = 1
        self.bounce_factor = 0.7


    def update(self):

        self.rect.topleft = self.position
        screen.blit(self.image, self.rect)

        # Collision detection
        for tile in world.tile_list:
            if self.rect.colliderect(tile[1]):
                self.vel_y *= -self.bounce_factor
                self.position.y = tile[1].top - self.rect.height


        # Gravity
        self.vel_y += self.acc_y
        if self.vel_y > 10:
            self.vel_y = 10
        self.position.y += self.vel_y



ball = Ball(100, 250)
world = World(world_data)

# Game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    clock.tick(60)
    screen.blit(bg_img, (0, 0))
    world.draw()
    ball.update()
    draw_grid()

    pSurface = font.render(f"Position: {ball.position}", True, (255, 255, 255))
    vSurface = font.render(f"Velocity: {ball.vel_x, ball.vel_y}", True, (255, 255, 255))
    screen.blit(pSurface, (10, 10))
    screen.blit(vSurface, (10, 40))

    pygame.display.flip()

pygame.quit()
