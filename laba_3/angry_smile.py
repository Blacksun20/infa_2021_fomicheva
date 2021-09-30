import pygame
from pygame.draw import *

pygame.init()

FPS = 30
screen = pygame.display.set_mode((400, 400))

yellow = (255, 255, 0)
red = (255, 0, 0)
black = (0, 0, 0)

circle( screen, yellow, (200, 200), 150)
circle(screen, red, (150, 150), 30)
circle(screen, red, (250, 150), 30)
circle(screen, black, (155, 150), 15)
circle(screen, black, (245, 150), 15)
polygon(screen, black, [(130, 265), (280, 265), (280, 290), (130, 290)])
polygon(screen, black, [(210, 135), (300, 100), (295, 85), (205, 120)])
polygon(screen, black, [(190, 135), (100, 100), (95, 85), (185, 120)])

pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()

