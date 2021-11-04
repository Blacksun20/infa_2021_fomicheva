import math
from random import choice, randint

import pygame


FPS = 30

RED = 0xFF0000
BLUE = 0x0000FF
YELLOW = 0xFFC91F
GREEN = 0x00FF00
MAGENTA = 0xFF03B8
CYAN = 0x00FFCC
BLACK = (0, 0, 0)
WHITE = 0xFFFFFF
GREY = 0x7D7D7D
PURPLE = (102, 0, 153)
GAME_COLORS = [RED, BLUE, YELLOW, GREEN, MAGENTA, CYAN]

WIDTH = 800
HEIGHT = 600


class Ball:
    def __init__(self, screen: pygame.Surface, x=40, y=450):
        """ Конструктор класса ball

        Args:
        x - начальное положение мяча по горизонтали
        y - начальное положение мяча по вертикали
        """
        self.screen = screen
        self.x = x
        self.y = y
        self.r = 10
        self.vx = 0
        self.vy = 0
        self.color = choice(GAME_COLORS)
        self.live = 30

    def move(self):
        """Переместить мяч по прошествии единицы времени.

        Метод описывает перемещение мяча за один кадр перерисовки. То есть, обновляет значения
        self.x и self.y с учетом скоростей self.vx и self.vy, силы гравитации, действующей на мяч,
        и стен по краям окна (размер окна 800х600).
        """
        g = 1
        k = 0.3
        time = 1
        for t in range(time):
            self.vy +=g
            if (self.x<=self.r+1 or self.x>=WIDTH - self.r -1):
                self.vx = -k*self.vx
                self.vy *= k
                self.x += self.vx
                self.y = self.y + self.vy + g/2
            elif (self.y<=self.r+1 or self.y>=HEIGHT - self.r -1):
                self.vy = -k*self.vy
                self.vx *= k
                self.x += self.vx
                self.y = self.y + self.vy + g/2
            else:
                self.x += self.vx
                self.y = self.y + self.vy + g/2

    def draw(self):
        pygame.draw.circle(
            self.screen,
            self.color,
            (self.x, self.y),
            self.r
        )

    def hittest(self, obj):
        """Функция проверяет сталкивалкивается ли данный обьект с целью, описываемой в обьекте obj.

        Args:
            obj: Обьект, с которым проверяется столкновение.
        Returns:
            Возвращает True в случае столкновения мяча и цели. В противном случае возвращает False.
        """
        if obj.type==Target:
            return (self.x - obj.x) ** 2 + (self.y - obj.y) ** 2 <= (self.r + obj.r) ** 2
        if obj.type == Box:
            return (self.x - obj.x) ** 2 + (self.y - obj.y) ** 2 <= (0.5 * obj.l * math.sqrt(2) + self.r) ** 2
        


class Gun:
    def __init__(self, screen):
        self.screen = screen
        self.f2_power = 10
        self.f2_on = 0
        self.an = 0
        self.color = GREY
        self.x = 40
        self.y = 450

    def fire2_start(self, event):
        self.f2_on = 1

    def fire2_end(self, event):
        """Выстрел мячом.

        Происходит при отпускании кнопки мыши.
        Начальные значения компонент скорости мяча vx и vy зависят от положения мыши.
        """
        global balls, bullet
        bullet += 1
        new_ball = Ball(self.screen)
        new_ball.r += 5
        if (event.pos[0] - 40)!=0:
            tg = -(event.pos[1] - 450)/(event.pos[0] - 40)
            self.an = math.atan(tg)
        new_ball.vx = self.f2_power * math.cos(self.an)
        new_ball.vy = - self.f2_power * math.sin(self.an)
        balls.append(new_ball)
        self.f2_on = 0
        self.f2_power = 10

    def targetting(self, event):
        """Прицеливание. Зависит от положения мыши."""
        if event:
             if (event.pos[0] - 40)!=0:
                 tg = -(event.pos[1] - 450)/(event.pos[0] - 40)
                 self.an = math.atan(tg)
        if self.f2_on:
            self.color = RED
        else:
            self.color = GREY

    def draw(self):
        pygame.draw.line(self.screen, self.color, (self.x, self.y), (self.x + math.cos(self.an) * self.f2_power, self.y - math.sin(self.an) * self.f2_power), 2)

    def power_up(self):
        if self.f2_on:
            if self.f2_power < 100:
                self.f2_power += 1
            self.color = RED
        else:
            self.color = GREY


class Target:
    def __init__ (self, screen):
        self.r = randint(5, 40)
        self.x = randint(self.r, WIDTH - self.r)
        self.y = randint(self.r, 0.8 * HEIGHT - self.r)
        self.color = RED
        self.is_alive = True
        self.screen = screen
        self.live = 1
        self.vx = randint(-1, 1)
        self.vy = randint(-1, 1)
        self.type = Target
    
    def move(self):
        for t in range(2):
            self.x += self.vx
            self.y += self.vy
            if self.x <= self.r or self.x >= WIDTH - self.r:
                self.vx = -self.vx
            if self.y <= self.r or self.y >= HEIGHT - self.r:
                self.vy = -self.vy

    def hit(self, points=1):
        """Попадание шарика в цель."""
        global score
        score += points

    def draw(self):
        pygame.draw.circle(self.screen, self.color, (self.x, self.y), self.r)
        
class Box:
    def __init__(self, screen):
        self.l = randint(10, 50)
        self.x = randint(self.l, WIDTH - self.l)
        self.y = randint(self.l, HEIGHT - self.l)
        self.x1 = self.x - 0.5*self.l
        self.y1 = self.y - 0.5*self.l
        self.color = PURPLE
        self.is_alive = True
        self.screen = screen
        self.live = 2
        self.vx = randint(-1, 1)
        self.vy = randint(-1, 1)
        self.type = Box
    
    def move(self):
        for t in range(2):
            self.x+=self.vx
            self.y+=self.vy
            if self.x1<=1 or self.x1>=self.l:
                self.vx = -self.vx
            if self.y1 <=1 or self.y1>=self.l:
                self.vy = -self.vy
    def hit(self, points = 2):
        global score
        score += points
    
    def draw(self):
        pygame.draw.rect(self.screen, self.color, (self.x1, self.y1, self.l, self.l))
    


pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
bullet = 0
balls = []
number_of_targets = 2
targets = []
box = Box(screen)
score = 0
for n in range(number_of_targets):
    targets.append(Target(screen))

clock = pygame.time.Clock()
gun = Gun(screen)
finished = False

while not finished:
    screen.fill(WHITE)
    gun.draw()
    for target in targets:
        target.draw()
    for b in balls:
        b.draw()
    box.draw()
    pygame.display.update()

    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True
        elif event.type == pygame.MOUSEBUTTONDOWN:
            gun.fire2_start(event)
        elif event.type == pygame.MOUSEBUTTONUP:
            gun.fire2_end(event)
        elif event.type == pygame.MOUSEMOTION:
            gun.targetting(event)
    for target in targets:
        target.move()
        for b in balls:
             b.move()
             if b.hittest(target) and target.live:
                target.live = 0
                targets.remove(target)
                target.hit()
                targets.append(Target(screen))
        box.move()
        for b in balls:
            if b.hittest(box) and box.live!=0:
                box.live-=1
            if box.live==0:
                box.hit()
                del box
                box = Box(screen)
    gun.power_up()
print(score)
pygame.quit()
