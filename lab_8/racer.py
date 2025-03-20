import pygame
import sys
from pygame.locals import *
import random
import time

pygame.init()

FPS = 60
FramePerSec = pygame.time.Clock()


BLUE = (0, 0, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

SCREEN_WIDTH = 400
SCREEN_HEIGHT = 600
SPEED = 5
SCORE = 0

pygame.mixer.music.load('./Lab_8/Ace of Base - Happy Nation.mp3')
pygame.mixer.music.play(-1)


font = pygame.font.SysFont("Verdana", 60)
font_small = pygame.font.SysFont("Verdana", 20)
game_over = font.render("Game Over", True, BLACK)


background = pygame.image.load("./Lab_8/AnimatedStreet.png")


screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
screen.fill(WHITE)
pygame.display.set_caption("RACER")


class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("./Lab_8/Enemy.png")
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(40, SCREEN_WIDTH - 40), 0)
        self.mask = pygame.mask.from_surface(self.image)

    def move(self):
        global SCORE
        self.rect.move_ip(0, SPEED)
        if self.rect.bottom > SCREEN_HEIGHT:
            SCORE += 1
            self.rect.top = 0
            self.rect.center = (random.randint(40, SCREEN_WIDTH - 40), 0)


class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.transform.scale(pygame.image.load(
            "./Lab_8/Player1.png"), (100, 110))
        self.rect = self.image.get_rect()
        self.rect.center = (200, 500)
        self.mask = pygame.mask.from_surface(self.image)

    def move(self):
        klav = pygame.key.get_pressed()
        if klav[K_LEFT] and self.rect.left > 0:
            self.rect.move_ip(-9, 0)
        if klav[K_RIGHT] and self.rect.right < SCREEN_WIDTH:
            self.rect.move_ip(9, 0)


class Coins(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("./Lab_8/coins.png")
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(20, SCREEN_WIDTH - 20), 0)

    def move(self):
        self.rect.move_ip(0, SPEED // 2)
        if self.rect.top > SCREEN_HEIGHT:
            self.rect.top = 0
            self.rect.center = (random.randint(20, SCREEN_WIDTH - 20), 0)


P1 = Player()
E1 = Enemy()
C = Coins()

coins = pygame.sprite.Group()
coins.add(C)

enemies = pygame.sprite.Group()
enemies.add(E1)

all_sprites = pygame.sprite.Group()
all_sprites.add(P1)
all_sprites.add(E1)

INC_SPEED = pygame.USEREVENT + 1
pygame.time.set_timer(INC_SPEED, 2000)


while True:
    for event in pygame.event.get():
        if event.type == INC_SPEED:
            SPEED += 0.5
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    screen.blit(background, (0, 0))
    scores = font_small.render(str(SCORE), True, BLACK)
    screen.blit(scores, (10, 10))

    for entity in all_sprites:
        entity.move()
        screen.blit(entity.image, entity.rect)

    for coin in coins:
        coin.move()
        screen.blit(coin.image, coin.rect)
    if pygame.sprite.spritecollide(P1, enemies, False, pygame.sprite.collide_mask):
        pygame.mixer.music.stop()
        pygame.mixer.music.load('./Lab_8/crash.wav')
        pygame.mixer.music.play()
        time.sleep(1.5)

        screen.fill(WHITE)
        screen.blit(game_over, (30, 250))
        res_scores = font.render("Score: " + str(SCORE), True, BLACK)
        screen.blit(res_scores, (20, 200))
        pygame.display.update()

        for entity in all_sprites:
            entity.kill()
        time.sleep(3)
        pygame.quit()
        sys.exit()

    if pygame.sprite.spritecollideany(P1, coins):
        pygame.mixer.Sound('./Lab_8/coinss.mp3').play()
        SCORE += 1
        C.rect.top = 0
        C.rect.center = (random.randint(20, SCREEN_WIDTH - 20), 0)

    pygame.display.update()
    FramePerSec.tick(FPS)

