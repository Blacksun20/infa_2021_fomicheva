import pygame
from pygame.draw import *
from random import randint
pygame.init()

FPS = 2
screen = pygame.display.set_mode((1200, 900))

RED = (255, 0, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
GREEN = (0, 255, 0)
MAGENTA = (255, 0, 255)
CYAN = (0, 255, 255)
BLACK = (0, 0, 0)
COLORS = [RED, BLUE, YELLOW, GREEN, MAGENTA, CYAN]

score = 0

def new_ball():
    '''
    Создает параметры нового шарика с цетром в точке (х, у) и радиуса r, цвета color

    '''
    global x, y, r, color
    x = randint(100,700)
    y = randint(100,500)
    r = randint(30,50)
    color = COLORS[randint(0, 5)]
    
def draw_ball(screen, x, y, r, color):
    '''
    Рисует шарик с задаными параметрами на экране
    '''
    circle(screen, color, (x, y), r)

def count(event):
    '''
    Ведет подсчет очков (обрабатывает клик)

    '''
    global score
    if (event.pos[1] - y)**2+(event.pos[0] - x)**2 <= r**2:
        score +=1

pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True
        elif event.type == pygame.MOUSEBUTTONDOWN:
            count(event)
    new_ball()
    draw_ball(screen, x, y, r, color)
    pygame.display.update()
    screen.fill(BLACK)
print('Score =', score)

pygame.quit()