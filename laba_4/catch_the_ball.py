import pygame
from pygame.draw import *
import model as mod
pygame.init()
mod.init()

player = input('Enter your name:')

FPS = 60
screen = pygame.display.set_mode(mod.field)



    
def draw_ball():
    '''
    Рисует шарик с задаными параметрами на экране
    '''
    for ball in mod.balls:
        circle(screen, ball[3], (ball[0], ball[1]), ball[2])



def draw_box():
    '''
    Рисует квадратик

    '''
    for box in mod.boxes:
        rect(screen, box[0], (box[1], box[2], box[3], box[3]))
        
    
pygame.display.update()
clock = pygame.time.Clock()
finished = False
play_time = 60000


while not finished:
    clock.tick(FPS)
    if pygame.time.get_ticks() >= play_time:
        finished = True
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mod.count(event)
    draw_ball()
    draw_box()
    mod.move_balls()
    mod.move_boxes()
    pygame.display.update()
    screen.fill(mod.WHITE)
print('Nice work,', player, '! Your score ', mod.score)
result = str((player, mod.score))
f = open('scores.txt', 'a')
f.write(result)
f.close()

pygame.quit()