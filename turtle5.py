import turtle as t
from random import *

t.shape('turtle')
for i in range(100):
    t.forward(randint(0, 40))
    t.left(randint(0, 360))
