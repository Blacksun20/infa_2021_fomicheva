import turtle as t
t.shape('turtle')
inp = open('shrift.txt', 'r')

def back ():
    t.penup()
    t.left(180)
    t.forward(60)
    t.right(90)
    t.forward(30)
    t.pendown()
def midle():
    t.penup()
    t.right(90)
    t.forward(30)
    t.left(90)
    t.pendown()
def zero():
    t.penup()
    t.forward(30)
    t.right(90)
    t.forward(60)
def nomber(no):
    for length, angle in d_fond[no]:
        t.left(angle)
        t.forward(length)

d_0=eval(inp.readline().rstrip())
d_1 = eval(inp.readline().rstrip())
d_2 = eval(inp.readline().rstrip())
d_3 = eval(inp.readline().rstrip())
d_4 = eval(inp.readline().rstrip())
d_5 = eval(inp.readline().rstrip())
d_6 = eval(inp.readline().rstrip())
d_7 = eval(inp.readline().rstrip())
d_8 = eval(inp.readline().rstrip())
d_9 = eval(inp.readline().rstrip())

d_fond = [d_0, d_1, d_2, d_3, d_4, d_5, d_6, d_7, d_8, d_9]

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
t.forward(30)
midle()
nomber(0)
zero()
midle()
nomber(0)

