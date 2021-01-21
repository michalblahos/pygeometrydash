import sys
import random
import pgzrun
from pgzero.builtins import *


rgen = random.Random()


WIDTH = 1000
HEIGHT = 1000

class Hra:
    def __init__(self):
        self.init()
        
    def init(self):
        self.stred = 500
        self.stred_smer = 0
        self.pocitadlo = 0
        self.run = False
        self.sirokost = 150

    def update_smer(self):
        self.stred += self.stred_smer
        if self.stred >= 900:
            self.stred_smer = -5
        if self.stred <= 100:
            self.stred_smer = 5
        self.pocitadlo += 1
        if self.pocitadlo % 100 == 0:
            self.stred_smer =  random.randrange(-4, 5)


hra = Hra()

plomby = []
jelito = Actor("p_0")
jelito.boty = 1000


def init():
    jelito.pos = (500, 900)
    jelito.smer_x = 0
    jelito.smer_y = 0
    jelito.boty = 0

    hra.init()
    hra.run = True

    plomby.clear()

    for i in range(52):
        plomba = Actor("fl_solid", pos=(hra.stred - hra.sirokost, i * 20))
        plomba.strana = -1
        plomby.append(plomba)
        plomba = Actor("fl_sand", pos=(hra.stred + hra.sirokost, i * 20))
        plomba.strana = 1
        plomby.append(plomba)

        
def draw():
    screen.clear()
    if hra.run:
        jelito.draw()
        for i in plomby:
            i.draw()
    else:
            screen.draw.text(f"Press 1 to start", pos=(100, 200))
    screen.draw.text(f"Body: ${jelito.boty}", pos=(100, 100))

def update_plomba(plomba):
    plomba.y += 5
    if plomba.y >= 1000:
        plomba.y = 0
        jelito.boty += 1
        plomba.x = hra.stred + plomba.strana*hra.sirokost

def died():
    hra.run = False

def update():
    if not hra.run:
        return
    jelito.x += jelito.smer_x
    jelito.y += jelito.smer_y

    if jelito.x >= 990:
        jelito.x = 990
    if jelito.x <= 10:
        jelito.x = 10

    for i in plomby:
        update_plomba(i)
        if jelito.colliderect(i):
            died()

    hra.update_smer()
    if hra.pocitadlo % 250 == 0:
        hra.sirokost -= 3

def on_key_down(key, mod, unicode):
    if key == keys.ESCAPE:
        exit()
    if key == keys.A:
        jelito.smer_x = -3
    if key == keys.D:
        jelito.smer_x = 3
    if key == keys.LEFT:
        jelito.smer_x = -6
    if key == keys.RIGHT:
        jelito.smer_x = 6
    if key == keys.K_1:
        init()
    #if key == keys.S:
     #   jelito.smer_y = 4
    #if key == keys.W:
      #  jelito.smer_y = -4

def on_key_up(key, mod):
    if key == keys.A or key == keys.LEFT:
        jelito.smer_x = 0
    if key == keys.D or key == keys.RIGHT:
        jelito.smer_x = 0
    #if key == keys.S:
       # jelito.smer_y = 0
   # if key == keys.W:
       # jelito.smer_y = 0



pgzrun.go()
