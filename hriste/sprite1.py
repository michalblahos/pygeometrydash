import sys
import random
import pgzrun
from pgzero.builtins import *


rgen = random.Random()


WIDTH = 1000
HEIGHT = 1000

plomby = []
jelito = Actor("p_0")
jelito.rung = False
jelito.boty = 1000

def init():
    jelito.pos = (500, 900)
    jelito.smer_x = 0
    jelito.smer_y = 0
    jelito.boty = 0
    jelito.rung = True

    plomby.clear()
    for i in range(10):
        plomba = Actor("klic", pos=(random.randrange(0, 1000), 0))
        plomby.append(plomba)

        plomba = Actor("klic", pos=(random.randrange(0, 1000), -200))
        plomby.append(plomba)

        plomba = Actor("klic", pos=(random.randrange(0, 1000), -400))
        plomby.append(plomba)

        plomba = Actor("klic", pos=(random.randrange(0, 1000), -600))
        plomby.append(plomba)

        plomba = Actor("klic", pos=(random.randrange(0, 1000), -800))
        plomby.append(plomba)


def draw():
    screen.clear()
    if jelito.rung:
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
        plomba.x = random.randrange(0,1000)

def died():
    jelito.rung = False

def update():
    if not jelito.rung:
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

def on_key_down(key, mod, unicode):
    if key == keys.ESCAPE:
        exit()
    if key == keys.A or key == keys.LEFT:
        jelito.smer_x = -4
    if key == keys.D or key == keys.RIGHT:
        jelito.smer_x = 4
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


#def on_mouse_down(pos, button):
    #animate(jelito, pos=pos, tween="accelerate")

pgzrun.go()
