import pygame
from pygame.locals import *

WIDTH = 400
HEIGHT = 300

# colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# initialize Pygame
pygame.init()

screen = pygame.display.set_mode((WIDTH, HEIGHT))
screen_rect = screen.get_rect()


class Player(pygame.sprite.Sprite):
    def __init__(self):
        super(Player, self).__init__()
        self.size = (20, 20)
        self.surf = pygame.Surface(self.size)
        self.surf.fill(GREEN)
        self.rect = self.surf.get_rect(center=(WIDTH/2, HEIGHT/2))
        self.acc_down = 0.3
        self.new_acc_down = 0.0
        self.gravity = 0.2
        self.speed = 4

    # FIRST SUCCESSFUL GRAVITY SIM! LET'S GO!
    def fall(self):
        self.new_acc_down = self.new_acc_down + self.acc_down + self.gravity
        self.rect.move_ip(0, self.new_acc_down)

    def move(self, pressed):
        if pressed[K_LEFT] or pressed[K_a]:
            self.rect.move_ip(-self.speed, 0)
        if pressed[K_RIGHT] or pressed[K_d]:
            self.rect.move_ip(self.speed, 0)
        
    def update(self, get_pressed_keys):
        self.move(get_pressed_keys)
        self.fall()


player = Player()

clock = pygame.time.Clock()

running = True
while running:
    screen.fill(WHITE)

    pressed_keys = pygame.key.get_pressed()

    for event in pygame.event.get():
        if event.type == QUIT:
            running = False

    screen.blit(player.surf, player.rect)
    player.update(pressed_keys)
    player.rect.clamp_ip(screen_rect)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
