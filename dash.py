import sys
import random
import pgzrun
from pgzero.builtins import *

from read_image import LevelImage


WIDTH = 1400
HEIGHT = 1000


class Hra:
    def __init__(self):
        self.run = False
        self.jelito = Actor("player")
        self.jelito.up = 0
        self.jelito.pada = True
        self.injump = False
        self.init()
        
    def init(self):
        self.stred = 500
        self.stred_smer = 0
        self.pocitadlo = 0
        self.body = 0
        self.level = LevelImage("images/level3.png")
        self.level.reset()
        self.blocks = []
        self.podlaha = []
        self.spike = []
        self.boosters = []
        self.jelito.pos = (100, 850)
        self.jelito.smer_x = 0
        self.jelito.smer_y = 0
        self.skakmed = []
        for i in range(30):
            plomba = Actor("prekazka", pos=(i*50, 500))
            self.podlaha.append(plomba)

        self.run = True

    def draw(self):
        for i in self.podlaha:
            i.draw()
        for i in self.spike:
            i.draw()
        for i in self.blocks:
            i.draw()
        for i in self.boosters:
            i.draw()
        for i in self.skakmed:
            i.draw()
        self.jelito.draw()


    def update(self):
        if len(self.spike) > 0 and self.spike[0].x <= -50:
            del self.spike[0] 
        if len(self.boosters) > 0 and self.boosters[0].x <= -50:
            del self.boosters[0] 
        if len(self.skakmed) > 0 and self.skakmed[0].x <= -50:
            del self.skakmed[0]
        for i in self.spike:
            i.x -= 5

        for i in self.podlaha:
            i.x -= 5
            if i.x <= -50:
                i.x = 1450
        for i in self.boosters:
            i.x -= 5
        for i in self.skakmed:
            i.x -= 5
            i.angle += -10
        self.blocks = [i for i in self.blocks if i.x > -50]
        for i in self.blocks:
            i.x -= 5

        self.naraz()
        self.update_jelito()

        self.dalsi_sloupec()

    def dalsi_sloupec(self):
        if self.podlaha[0].x % 50 == 0:
            sloupec = self.level.get_next()
            for (typ, y) in sloupec:
                if typ == "blok":
                    bl = Actor("block", midtop=(1450, 50*y))
                    self.blocks.append(bl)
                if typ == "spike":
                    s = Actor("bodak", midbottom=(1450, 50*y+50))
                    self.spike.append(s)
                if typ == "booster-1":
                    s = Actor("booster", midbottom=(1450, 50*y+50))
                    self.boosters.append(s)
                if typ == "skakmed":
                    s = Actor("skakadlo-medium", midbottom=(1450, 50*y+50))
                    self.skakmed.append(s)
    def jump(self):
        if self.jelito.up <= 0 and not self.jelito.pada:
            self.jelito.up = 100

    def update_jelito(self):
        # TODO: zjistime, zda jsme nenarazili na smrt
        if self.jelito.up > 0:
            self.jelito.y -= 5
            self.jelito.up -= 5
        else:   
            dolu = self.o_kolik_dolu()
            if dolu > 0:
                if dolu > 5:
                    dolu = 5
                self.jelito.y += dolu
            
                self.jelito.pada = True
            else:
                self.jelito.pada = False
                if self.injump:
                    self.jump() 
        self.boost()

    def boost(self):
        for i in self.boosters:
            if self.jelito.right >= i.left and self.jelito.right <= i.right:
                if self.jelito.colliderect(i):
                    print(">>>>>> trefa jo?")
                    self.jelito.up = 200
        
    def naraz(self):
        for i in self.blocks:
            if self.jelito.right >= i.left and self.jelito.right <= i.right:
                if self.jelito.colliderect(i):
                    if self.jelito.bottom <= i.top:
                        pass
                    else:
                        self.kill()
        for i in self.spike:
            if self.jelito.right >= i.left and self.jelito.right <= i.right:
                if self.jelito.colliderect(i):
                    print(f"Kill se spike {i.left} {i.right}")
                    self.jelito.image = "zelenej"
                    self.kill()
                else:
                    print(f"--- No-kill se spike {i.left} {i.right}")
                    self.jelito.image = "player"
        
    def kill(self):
        print("kill")
        self.run = False

    def o_kolik_dolu(self):
        dolu = 0
        dolu2 = -1
        if self.jelito.bottom < 950:
            dolu = 950 - self.jelito.bottom
        for i in self.blocks:
            if i.x >= self.jelito.x - 25 and i.x <= self.jelito.x + 25:
                if i.top == self.jelito.bottom:
                    return 0
                if i.top > self.jelito.bottom:
                    d = i.top - self.jelito.bottom
                    if d < dolu2 or dolu2 == -1:
                        dolu2 = d
        if dolu2 > 0:
            return dolu2
        return dolu    


hra = Hra()

        
def draw():
    screen.clear()
    if not hra.run:
        screen.draw.text("Press 1 to start", pos=(100, 200))
    
    hra.draw()
        
    screen.draw.text(f"Body: ${hra.body}", pos=(100, 100))
    screen.draw.text(f"${hra.jelito.pos}", pos=(100, 120))
    screen.draw.line((hra.jelito.left, 0), (hra.jelito.left, 1000), (0, 255, 0))
    screen.draw.line((hra.jelito.right, 0), (hra.jelito.right, 1000), (0, 255, 0))


def update():
    if not hra.run:
        return
    hra.update()


def on_key_down(key, mod, unicode):
    if key == keys.ESCAPE:
        exit()
    if key == keys.K_1:
        hra.init()
    if key == keys.SPACE:
        hra.injump = True
        hra.jump()


def on_key_up(key, mod):
    if key == keys.SPACE:
        hra.injump = False


pgzrun.go()
