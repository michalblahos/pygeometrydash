import sys
import random
import pgzrun
from pgzero.builtins import *


rgen = random.Random()


WIDTH = 1000
HEIGHT = 1000

def draw():
    screen.clear()

    for i in range(0, 1000, 1):
        color = (rgen.randint(0, 255), rgen.randint(0, 255), rgen.randint(0,210))
        color = (i % 255, 0, 0)
        screen.draw.line((0, 1000-i), (i, 0), color)
        screen.draw.line((1000-i, 0), (1000, 1000-i), color)
        screen.draw.line((1000, 1000-i), (i, 1000), color)
        screen.draw.line((1000-i, 1000), (0, 1000-i), color)



def ctverecek(x, y, i):
    color = (rgen.randint(0, 255), rgen.randint(0, 2), rgen.randint(0,2))
    

    screen.draw.line((x, y),(x, y+i), color)
    screen.draw.line((x, y+i),(x+i, y+i), color)
    screen.draw.line((x, y),(x+i, y), color)
    screen.draw.line((x+i, y),(x+i, y+i), color)



pgzrun.go()
