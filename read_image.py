import pygame


class LevelImage:
    def __init__(self, fn):
        self.img = pygame.image.load(fn)
        self.col = -1

    def reset(self):
        self.col = -1

    def get_next(self):
        self.col += 1
        if self.col >= self.img.get_width():
            self.col = 0
        ret = []
        for y in range(1, self.img.get_height() - 1):
            pix = self.img.get_at((self.col, y))
            if pix[0] < 20 and pix[1] < 20 and pix[2] < 20:
                continue        # cerna znamena prazdny
            if pix[0] > 200 and pix[1] > 200 and pix[2] > 200:
                # bila znamena blok
                ret.append(("blok", y))
                continue
            if pix[0] > 200 and pix[1] < 20 and pix[2] < 20:
                ret.append(("spike", y))  # cervena - spike
                continue
            if pix[0] > 200 and pix[1] > 200 and pix[2] < 20:
                ret.append(("booster-1", y))  # zluta - odrazec
                continue
            if pix[0] < 20 and pix[1] > 200 and pix[2] < 20:
                ret.append(("skakmed", y))  # zelena - skakmed - skakadlo - medium
                continue
        return ret


def main():
    l = LevelImage("images/level3.png")
    for i in range(10):
        print(i, l.get_next())



if "__main__" == __name__:
    main()
