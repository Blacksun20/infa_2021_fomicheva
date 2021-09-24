import turtle as t
from random import randint

number_of_turtles = 20
steps_of_time_number = 100

x = [randint(-200, 200) for i in range(number_of_turtles)]
y = [randint(-200, 200) for i in range(number_of_turtles)]

pool = [t.Turtle(shape = 'circle') for i in range (number_of_turtles)]
for unit in pool:
    unit.penup()
    vx = [randint(-5, 5) for i in range(number_of_turtles)]
    vy = [randint(-5, 5) for i in range(number_of_turtles)]
    
for i in range(steps_of_time_number):
    for k in range(number_of_turtles):
        pool[k].goto(x[k]+vx[k], y[k]+vy[k])
        x[k]+=vx[k]
        y[k]+=vy[k]
        if x[k]>=200 or x[k]<=-200:
            vx[k]=-vx[k]
        if y[k]>=200 or y[k]<=-200:
            vy[k]=-vy[k]
            
