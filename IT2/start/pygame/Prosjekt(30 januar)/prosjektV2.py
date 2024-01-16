import pygame as pg
from pygame.locals import (K_UP, K_DOWN, K_RIGHT, K_LEFT)
import math as m

pg.init()

# Oppretter et vindu der vi skal "tegne" innholdet vårt
VINDU_BREDDE = 1000
VINDU_HOYDE = 1000
vindu = pg.display.set_mode([VINDU_BREDDE, VINDU_HOYDE])

class objekter():
    def __init__(self, x, y, radius, farge, vindusobjekt, size):
        self.x = x
        self.y = y
        self.radius = radius
        self.farge = farge
        self.vindusobjekt = vindusobjekt
        self.width, self.height = size

    def tegnCircle(self):
        pg.draw.circle(self.vindusobjekt, self.farge, (self.x, self.y), self.radius)

    def tegnRectangle(self):
        rect = (self.x, self.y, self.width, self.height)
        pg.draw.rect(self.vindusobjekt, self.farge, rect)

    def finnAvstand(self, annetObjekt):
        """Metode for å finne avstanden til en annen ball eller spiller"""
        xAvstand2 = (self.x - annetObjekt.x) ** 2  # x-avstand i andre
        yAvstand2 = (self.y - annetObjekt.y) ** 2  # y-avstand i andre
        sentrumsavstand = m.sqrt(xAvstand2 + yAvstand2)

        radiuser = self.radius + annetObjekt.radius

        avstand = abs(sentrumsavstand - radiuser)

        return avstand

    def kollisjon(self, annetObjekt):
        """Metode for å sjekke kollisjon med et annet objekt"""
        return self.finnAvstand(annetObjekt) <= 0

class Ball(objekter):
    def __init__(self, x, y, radius, farge, vindusobjekt, xFart, yFart):
        super().__init__(x, y, radius, farge, vindusobjekt, (0, 0))  # Corrected order
        self.xFart = xFart
        self.yFart = yFart

    def flytt(self, spiller):
        """Method to move the bouncing ball"""
        if ((self.x - self.radius) <= 0) or ((self.x + self.radius) >= self.vindusobjekt.get_width()):
            self.xFart = -self.xFart

        if ((self.y - self.radius) <= 0) or ((self.y + self.radius) >= self.vindusobjekt.get_height()):
            self.yFart = -self.yFart

      
        self.x += self.xFart
        self.y += self.yFart

class Spiller(objekter):
    def __init__(self, x, y, radius, height, width, farge, vindusobjekt, fart):
        super().__init__(x, y, radius, farge, vindusobjekt, (height, width))
        self.fart = fart

    def flytt(self, taster):
        """Metode for å flytte spilleren"""
        if taster[K_UP]:
            self.y -= self.fart
        if taster[K_DOWN]:
            self.y += self.fart
        if taster[K_RIGHT]:
            self.x += self.fart
        if taster[K_LEFT]:
            self.x -= self.fart
            


ball = Ball(200, 200, 20, (255, 0, 0), vindu, 0, 0)
spiller1 = Spiller(120, 50, 0, 20, 130, (0, 0, 250), vindu, 2)

fortsett = True
while fortsett:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            fortsett = False

    trykkede_taster = pg.key.get_pressed()
    vindu.fill((92, 107, 192))

    ball.tegnCircle()
    ball.flytt(spiller1)
    spiller1.tegnRectangle()
    spiller1.flytt(trykkede_taster)

    avstand = spiller1.finnAvstand(ball)
    if avstand <= 10:
        # Just for testing, you can adjust the factor based on your preference
        ball.xFart *= -1.0
        ball.yFart *= 1.0

    print(avstand)
    pg.display.flip()

pg.quit()
