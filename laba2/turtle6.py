import turtle as t

t.shape('turtle')

def back ():
    t.penup()
    t.left(180)
    t.forward(m)
    t.right(90)
    t.forward(n)
    t.pendown()
def midle ():
    t.penup()
    t.right(90)
    t.forward(n)
    t.left(90)
    t.pendown()
def zero ():
    t.penup()
    t.forward(n)
    t.right(90)
    t.forward(m)
def nomber(no):
    for length, angle in d_fond[no]:
        t.left(angle)
        t.forward(length)

n = 30
m = n * 2
k = n * (2**0.5)
d_0 = [(n, 90), (n, -90), (m, -90), (n, -90), (n, -90)]
d_1 = [(k, 45), (m, -135)]
d_2 = [(n, 0), (n, -90), (k, -45), (n, 135)]
d_3 = [(n, 0), (k, -135), (n, 135), (k, -135)]
d_4 = [(n, -90), (n, 90), (n, 90), (m, 180)]
d_5 = [(n, 180), (n, 90), (n, 90), (n, -90), (n, -90)]
d_6 = [(k, -135), (n, 135), (n, -90), (n, -90), (n, -90)]
d_7 = [(n, 0), (k, -135), (n, 45)]
d_8 = [(n, -90), (n, -90), (n, -90), (n, -90), (n, 90), (n, 90), (n, 90)]
d_9 = [(n, 90), (n, -90), (n, -90), (n, -90), (n, 180), (k, -135)]
d_fond =[d_0, d_1, d_2, d_3, d_4, d_5, d_6, d_7, d_8, d_9]
nomber(1)
back()
nomber(4)
back()
midle()
nomber(1)
back()
nomber(7)
back()
t.penup()
t.forward(n)
midle()
nomber(0)
zero()
midle()
nomber(0)
