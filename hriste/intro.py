import sys
import random
import pgzrun
from pgzero.builtins import *


rgen = random.Random()



WIDTH = 1000
HEIGHT = 1000

def drawX():
    screen.clear()

    for i in (0, 1, 2, 3, 4, 5, 6, 7, 8, 9, ):
        screen.draw.line((0, i*10), (200, i*10), (255, i*20, 255))
        screen.draw.line((i*10, 0), (i*10, 200), (i*20 ,255, 255))

    for i in range(10):
        screen.draw.line((0, 0), (200, i*10), (255, i*20, 255))
        screen.draw.line((0, 0), (i*10, 200), (i*20 ,255, 255))




def ctverecek(x, y, i):
    color = (rgen.randint(0, 255), rgen.randint(0, 2), rgen.randint(0,2))
    

    screen.draw.line((x, y),(x, y+i), color)
    screen.draw.line((x, y+i),(x+i, y+i), color)
    screen.draw.line((x, y),(x+i, y), color)
    screen.draw.line((x+i, y),(x+i, y+i), color)


def draw():
    screen.clear()
    #ctverecek(999)
    #ctverecek(30)
   #ctverecek(10,10, 888)
    #ctverecek(20,120, 888)
    for i in range(1000):
#        ctverecek(rgen.randint(1, 500), rgen.randint(1, 500), rgen.randint(1, 500))
        ctverecek(i, i, i)


#    r=Rect((20, 20), (100, 100))
#    screen.draw.rect(r, (200, 20, 254))


pgzrun.go()
