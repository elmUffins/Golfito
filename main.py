import pygame
import math

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
#def draw_grid():
#    for line in range(0, 20):
#        pygame.draw.line(screen, (0, 0, 0), (0, line * tile_size), (screen_w, line * tile_size))
#        pygame.draw.line(screen, (0, 0, 0), (line * tile_size, 0), (line * tile_size, screen_h))

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
class Ball:
    def __init__(self, x, y):
        img = pygame.image.load("images/golfball.png")
        self.image = pygame.transform.scale(img, (20, 20))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.position = pygame.math.Vector2(self.rect.x, self.rect.y)
        self.vel_x = 0
        self.vel_y = 0
        self.bounce_factor = 0.7
        self.gravity = 1
        self.terminal_velocity = 15
        self.friction = 0.1
        if self.vel_y == 0 and self.vel_x == 0:
            self.thrown = False
        elif self.vel_y != 0 or self.vel_x != 0:
            self.thrown = True


    def update(self):
        # Apply gravity
        self.vel_y += self.gravity
        if self.vel_y > self.terminal_velocity:
            self.vel_y = self.terminal_velocity

        # Update position
        self.position.y += self.vel_y
        self.rect.topleft = self.position

        # Screen collision
        if self.rect.x == 0 or self.rect.x == 1000:
            self.vel_x *= -1
        
        if self.rect.y == 0 or self.rect.y == 500:
            self.vel_y *= -1
        
 
        # Collision detection
        for tile in world.tile_list:
            if self.rect.colliderect(tile[1]):
                if self.vel_y > 0:  # Falling down
                    self.position.y = tile[1].top - self.rect.height
                elif self.vel_y < 0:  # Moving up
                    self.position.y = tile[1].bottom

                self.rect.topleft = self.position

                # Apply bounce factor
                self.vel_y *= -self.bounce_factor

                # If the velocity is very low after bouncing, apply friction to stop the ball
                if abs(self.vel_y) < 1:
                    self.vel_y = 0

        # Apply friction to slow down the ball's horizontal movement
        if abs(self.vel_x) > 0:
            self.vel_x -= self.friction if self.vel_x > 0 else -self.friction
            if abs(self.vel_x) < self.friction:
                self.vel_x = 0

        # Update the position based on horizontal velocity
        self.position.x += self.vel_x

        # Update the rect position
        self.rect.topleft = self.position
        screen.blit(self.image, self.rect)


    
    def putt(self):
        if self.vel_x == 0 and self.vel_y == 0:
            self.thrown = False
        
        if self.thrown == False:
            mousepos = pygame.mouse.get_pos()
            ballpos = ball.rect.center
            distance_x = mousepos[0] - ballpos[0]
            distance_y = mousepos[1] - ballpos[1]
            
            self.vel_x += (0.05 * distance_x)
            self.vel_y += (0.15 * distance_y)
            
            self.thrown == True


ball = Ball(100, 250)
world = World(world_data)

# Game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                ball.putt()

    clock.tick(60)
    screen.blit(bg_img, (0, 0)) 
    world.draw()
    ball.update()
    #draw_grid()

    mousepos = pygame.mouse.get_pos()
    ballpos = ball.rect.center

    distance1 = abs(ballpos[0] - mousepos[0])
    distance2 = abs(ballpos[1] - mousepos[1])

    if ball.thrown == False:
        pygame.draw.line(screen, (255, 0, 0), ballpos, mousepos, 3)

    

    pSurface = font.render(f"Position: {ball.position}", True, (255, 255, 255))
    vSurface = font.render(f"Velocity: {ball.vel_x, ball.vel_y}", True, (255, 255, 255))
    mSurface = font.render(f"Mouse position: {mousepos}", True, (255, 255, 255))
    dSurface = font.render(f"Distance: {distance1, distance2}", True, (255, 255, 255))

    screen.blit(pSurface, (10, 10))
    screen.blit(vSurface, (10, 40))
    screen.blit(mSurface, (10, 70))
    screen.blit(dSurface, (10, 100))

    pygame.display.flip()

pygame.quit()
