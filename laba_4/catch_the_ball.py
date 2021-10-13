import pygame
from pygame.draw import *
from random import randint
pygame.init()

player = input('Enter your name:')

FPS = 60
width = 1200
height = 900
field = (width, height)
screen = pygame.display.set_mode(field)

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
           balls.append(new_ball())
           give_speed()
           score +=1
    for box in boxes:
        if(event.pos[0]-(box[1]+box[3]/2))**2+(event.pos[1]-(box[2]+box[3]/2))**2<=box[3]**2/2:
            boxes.remove(box)
            boxes.append(new_box())
            give_speed()
            score+=2
            
def gen_speed(object_t, index):
    '''
    Создает скорости для шариков и квадратиков

    '''
    vx = randint(-1, 1)
    vy = randint(-1, 1)
    object_t[index].append(vx)
    object_t[index].append(vy)
    
def give_speed():
    '''
    Присваивает скорости шарикам и квадратикам

    '''
    for ball in balls:
        gen_speed(balls, balls.index(ball))
    for box in boxes:
        gen_speed(boxes, boxes.index(box))
        
def move_balls():
    '''
    Описывает движение шариков

    '''
    for ball in balls:
        for t in range(time):
            ball[0]+=ball[4]
            ball[1]+=ball[5]
            if ball[0]<ball[2]+1 or ball[0]>=width-ball[2]:
                ball[4]*=-1
            if ball[1]<=ball[2]+1 or ball[1]>=height-ball[2]:
                ball[5]*=-1
                
def new_box():
    '''
    Создает параметры квадратика (m, n) - левый угол, l - длина стороны

    '''
    m = randint(100, 700)
    n = randint(100, 500)
    l = randint(30, 50)
    color = COLORS[randint(0,5)]
    return[color, m, n, l]

def draw_box():
    '''
    Рисует квадратик

    '''
    for box in boxes:
        rect(screen, box[0], (box[1], box[2], box[3], box[3]))
        
def move_boxes():
    '''
    Описывает движение квадратиков

    '''
    for box in boxes:
        box[1]+=box[4]
        box[2]+=box[5]
        if box[1]<1 or box[1]>=width-box[3]:
            box[4]*=-1
        if box[2]<1 or box[2]>=height-box[3]:
            box[5]*=-1

pygame.display.update()
clock = pygame.time.Clock()
finished = False
nomber_balls = randint(5, 10)
nomber_boxes = randint(5, 10)
balls = [new_ball() for n in range(nomber_balls)]
boxes = [new_box() for n in range(nomber_boxes)]
time = 8
play_time = 60000
give_speed()

while not finished:
    clock.tick(FPS)
    if pygame.time.get_ticks() >= play_time:
        finished = True
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True
        elif event.type == pygame.MOUSEBUTTONDOWN:
            count(event)
    draw_ball()
    draw_box()
    move_balls()
    move_boxes()
    pygame.display.update()
    screen.fill(BLACK)
print('Nice work,', player, '! Your score ', score)
result = str((player, score))
f = open('scores.txt', 'a')
f.write(result)
f.close()

pygame.quit()