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

#фонь#
rect(screen, light_blue, (0, 0, 600, 450))
polygon(screen, light_green, [(0, 440), (50, 430), (100, 425), (300, 425), (305, 430), (310, 440), (310, 470), (315, 480), (315, 520), (600, 520), (600, 900), (0, 900)])
polygon(screen, grey, [(0, 440), (0, 380), (100, 190), (150,290), (200, 200), (310, 370), (400, 190), (450, 240), (600, 100), (600, 520),(315, 520), (315, 480), (310, 470), (310, 440), (305, 430), (300, 425), (100, 425), (50, 430)])
lines(screen, black, False,[(0, 440), (50, 430), (100, 425), (300, 425), (305, 430), (310, 440), (310, 470), (315, 480), (315, 520), (600, 520)])
lines(screen, black, False, [(0, 380), (100, 190), (150,290), (200, 200), (310, 370), (400, 190), (450, 240), (600, 100)], 1)
#клумба#
circle(screen, green, (450, 700), 100)
#лама#
ellipse(screen, white, (100, 600, 150, 50))
ellipse(screen, white, (215, 500, 35, 120))
ellipse(screen, white, (215, 480, 50, 33))
ellipse(screen, white, (215, 630, 18, 50))
ellipse(screen, white, (215, 675, 18, 50))
ellipse(screen, white, (215, 715, 25, 13))
ellipse(screen, white, (195, 620, 18, 50))
ellipse(screen, white, (195, 665, 18, 50))
ellipse(screen, white, (195, 705, 25, 13))
ellipse(screen, white, (130, 630, 18, 50))
ellipse(screen, white, (130, 675, 18, 50))
ellipse(screen, white, (130, 715, 25, 13))
ellipse(screen, white, (103, 615, 18, 50))
ellipse(screen, white, (103, 655, 18, 50))
ellipse(screen, white, (103, 695, 25, 13))
circle(screen, purple, (238, 493), 11)
circle(screen, black, (240, 493), 5)
ellipse(screen, white, (230, 489, 10, 5))
polygon(screen, white, [(205, 485), (210, 495), (225, 488)])
polygon(screen, white, [(213, 475), (218, 485), (233, 478)])
#цветочек 1#
circle(screen, yellow, (430, 650), 10)
ellipse(screen, white, (425, 655, 18, 10))
ellipse(screen, white, (415, 655, 18, 10))
ellipse(screen, white, (415, 640, 10, 18))
ellipse(screen, white, (435, 640, 10, 18))
ellipse(screen, white, (425, 635, 18, 10))
ellipse(screen, white, (415, 635, 18, 10))
#цветочек 2#
circle(screen, yellow, (400, 700), 10)
ellipse(screen, white, (395, 705, 18, 10))
ellipse(screen, white, (385, 705, 18, 10))
ellipse(screen, white, (385, 690, 10, 18))
ellipse(screen, white, (405, 690, 10, 18))
ellipse(screen, white, (395, 685, 18, 10))
ellipse(screen, white, (385, 685, 18, 10))
#цветочек 3#
circle(screen, yellow, (430, 750), 10)
ellipse(screen, white, (425, 755, 18, 10))
ellipse(screen, white, (415, 755, 18, 10))
ellipse(screen, white, (415, 740, 10, 18))
ellipse(screen, white, (435, 740, 10, 18))
ellipse(screen, white, (425, 735, 18, 10))
ellipse(screen, white, (415, 735, 18, 10))
#цветочек 4#
circle(screen, yellow, (500, 730), 10)
ellipse(screen, white, (495, 735, 18, 10))
ellipse(screen, white, (485, 735, 18, 10))
ellipse(screen, white, (485, 720, 10, 18))
ellipse(screen, white, (505, 720, 10, 18))
ellipse(screen, white, (485, 715, 18, 10))
ellipse(screen, white, (495, 715, 18, 10))
#цветочек 5#
circle(screen, yellow, (490, 670), 10)
ellipse(screen, white, (485, 675, 18, 10))
ellipse(screen, white, (475, 675, 18, 10))
ellipse(screen, white, (475, 660, 10, 18))
ellipse(screen, white, (495, 660, 10, 18))
ellipse(screen, white, (475, 655, 18, 10))
ellipse(screen, white, (485, 655, 18, 10))
        
pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()