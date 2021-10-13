import pygame
from pygame.draw import *
from random import randint
pygame.init()

FPS = 60
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
    x = randint(100, 700)
    y = randint(100, 500)
    r = randint(30, 50)
    color = COLORS[randint(0, 5)]
    return [x, y, r, color]

    
def draw_ball():
    '''
    Рисует шарик с задаными параметрами на экране
    '''
    for ball in balls:
        circle(screen, ball[3], (ball[0], ball[1]), ball[2])

def count(event):
    '''
    Ведет подсчет очков (обрабатывает клик)

    '''
    global score
    for ball in balls:
       if (event.pos[1] - ball[1])**2+(event.pos[0] - ball[0])**2 <= ball[2]**2:
           balls.remove(ball)
           score +=1

pygame.display.update()
clock = pygame.time.Clock()
finished = False
nomber = randint(5, 10)
balls = [new_ball() for n in range(nomber)]

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True
        elif event.type == pygame.MOUSEBUTTONDOWN:
            count(event)
    draw_ball()
    pygame.display.update()
    screen.fill(BLACK)
print('Score =', score)

pygame.quit()