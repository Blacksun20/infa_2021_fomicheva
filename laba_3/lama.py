import pygame
from pygame.draw import *

pygame.init()

FPS = 30
screen = pygame.display.set_mode((600, 900))

white = (255, 255, 255)
light_green = (152, 255, 152)
grey = (172, 172, 172)
light_blue = (192, 255, 255)
yellow = (255, 255, 0)
purple = (255, 128, 255)
black = (0, 0, 0)
green = (51, 255, 0)

#Функции для рисования всякой всячины

#Функции для рисования Ламы
def draw_lama(surface, color, eye_color, x, y, lama_width, lama_height):
    '''
    Функция рисует ламу по частям тела
    surface - объект pygame.Surface
    color - цвет шерсти Ламы
    eye_color - цвет глаза Ламы
    x, y -координаты центра Ламы
    lama_width, lama_height - ширина и высота Ламы
    '''
    
    draw_body(surface, color, x - lama_width // 2, y, lama_width * 9 // 10, lama_height // 5)

    draw_neck(surface, color, x + lama_width // 5, y - lama_height * 2 // 5, lama_width // 5, lama_height * 48 // 100)

    draw_head(surface, color, x + lama_width // 5, y - lama_height * 48 // 100, lama_width * 10 // 33, lama_height * 132 // 1000)

    if lama_width >= lama_height:
        draw_eye(surface, color, x + lama_width * 56 // 165, y - lama_height * 107 // 250, lama_width * 11 // 165)
    else:
        draw_eye(surface, eye_color, x + lama_width * 56 // 165, y - lama_height * 107 // 250, lama_height * 11 // 250)

    for coordinates in ((x + lama_width * 33 // 165, y + lama_height * 3 // 25), (x + lama_width * 13 // 165, y + lama_height * 2 // 25), (x - lama_width * 52 // 165, y + lama_height * 3 // 25), (x - lama_width * 79 // 165, y + lama_height * 3 // 25)):
        draw_leg(surface, color, coordinates[0], coordinates[1], lama_width * 6 // 55, lama_height // 5)
        
def draw_leg(surface, color, x, y, width, height):
    '''
    Функция рисует ногу Ламы
    surface - объект pygame.Surface
    color - цвет ноги
    x, y - координаты левого верхнего края ноги Ламы
    width, height - ширина и высота ноги Ламы
    '''
    ellipse(surface, color, (x, y, width, height))
    ellipse(surface, color, (x, y + height * 9 // 10, width, height))
    ellipse(surface, color, (x, y + height * 17 // 10, width * 25 // 18, height * 13 // 50))

def draw_body(surface, color, x, y, width, height):
    '''
    Функция рисует тело Ламы
    surface - объект pygame.Surface
    color - цвет тела Ламы
    x, y - координаты левого верхнего края тела
    width, height - ширина и высота тела Ламы
    '''
    ellipse(surface, color, (x, y, width, height))

def draw_neck(surface, color, x, y, width, height):
    '''
    Функция рисует шею ламы
    surface - объект pygame.Surface
    color - цвет шеи Ламы
    x, y - координаты левого верхнего края шеи Ламы
    width, height - ширина и высота шеи Ламы
    '''
    ellipse(surface, color, (x, y, width, height))

def draw_head(surface, color, x, y, width, height):
    '''
    Функция рисует голову и ушки Ламы
    surface - объект pygame.Surface
    color - цвет головы и ушек Ламы
    x, y - координаты левого верхнего края головы Ламы
    width, height - ширина и высота головы Ламы
    '''
    ellipse(surface, color, (x, y, width, height))
    polygon(surface, color, [(x - width // 5, y + height * 5 // 33), (x - width // 10, y + height * 15 // 33), (x + width // 5, y + height * 8 // 33)])
    polygon(surface, color, [(x - width // 25, y - height * 5 // 33), (x + width * 3 // 50, y + height * 5 // 33), (x + width * 9 // 25, y - height * 2 // 33)])

def draw_eye(surface, color, x, y, eye_size):
    '''
    Функция рисует глаз Ламы
    surface - объект pygame.Surface
    color - цвет глаза Ламы
    x, y - координаты центра глаза Ламы
    eye_size - радиус галаза Ламы
    '''
    circle(surface, color, (x, y), eye_size)
    circle(surface, black, (x + 1, y), eye_size // 2)
    ellipse(surface, white, (x - eye_size * 8 // 11, y + eye_size * 4 // 11, eye_size - 1, eye_size // 2))


#Функции для рисования клумбы со цветами
def draw_island(surface, color, flower_color, x, y, size):
    '''
    Функция рисует клумбу вместе с цветочками
    surface - объект pygame.Surface
    color - цвет травы клумбы
    flower_color - цвет лепестков цветов
    x, y - координаты центра клумбы
    size - радиус клумбы
    '''
    circle(screen, green, (x, y), size)
    for coordinates in ((x - size // 5, y - size // 2), (x - size // 2, y), (x - size // 5, y + size // 2), (x + size // 2, y + size * 3 // 10), (x + size * 2 // 5, y - size * 3 // 10)):
        x = coordinates[0]
        y = coordinates[1]
        draw_flower(screen, flower_color, x, y, size // 10)
        
def draw_flower(surface, color, x, y, middle_size):
    '''
    Функция рисует цветочек
    surface - обект pegame.Surface
    color - цвет лепестков цветка
    x, y, координаты центра цветка
    middle_size - радиус центральной части цветка
    '''
    range_1 = middle_size // 2
    range_2 = range_1 * 3
    petal_width = middle_size
    petal_height = (middle_size * 18) // 10
    
    circle(surface, yellow, (x, y), middle_size)
    for petal_x in (x - range_1, x - range_2):
        draw_petal(surface, color, petal_x, y + range_1, petal_height, petal_width)
        draw_petal(surface, color, petal_x, y - range_2, petal_height, petal_width)
    for petal_x in (x - range_2, x + range_1):
        draw_petal(surface, color, petal_x, y - middle_size, petal_width, petal_height)



def draw_petal(surface, color, x, y, width, height):
    '''
    Функция рисует лепесток для цветочка
    surface - объект pygame.Surface
    color - цвет лепестка
    x, y - координаты левой верхней части лепестка
    width, height - щирина и высота лепестка
    '''
    ellipse(surface, color, (x, y, width, height))

    
#фонь#
rect(screen, light_blue, (0, 0, 600, 450))
polygon(screen, light_green, [(0, 440), (50, 430), (100, 425), (300, 425), (305, 430), (310, 440), (310, 470), (315, 480), (315, 520), (600, 520), (600, 900), (0, 900)])
polygon(screen, grey, [(0, 440), (0, 380), (100, 190), (150,290), (200, 200), (310, 370), (400, 190), (450, 240), (600, 100), (600, 520),(315, 520), (315, 480), (310, 470), (310, 440), (305, 430), (300, 425), (100, 425), (50, 430)])
lines(screen, black, False,[(0, 440), (50, 430), (100, 425), (300, 425), (305, 430), (310, 440), (310, 470), (315, 480), (315, 520), (600, 520)])
lines(screen, black, False, [(0, 380), (100, 190), (150,290), (200, 200), (310, 370), (400, 190), (450, 240), (600, 100)], 1)

#клумба#
draw_island(screen, green, white, 450, 700, 100)

#Лама
draw_lama(screen, white, purple, 182, 600, 165, 250)

       
pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()
