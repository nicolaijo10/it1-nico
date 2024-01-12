import pygame as pg
from pygame.locals import (K_UP, K_DOWN, K_LEFT, K_RIGHT)
import math as m

pg.init()

# Oppretter et vindu der vi skal "tegne" innholdet vårt
VINDU_BREDDE = 1920
VINDU_HOYDE  = 1080
vindu = pg.display.set_mode([VINDU_BREDDE, VINDU_HOYDE])

class objekter():
    def __init__(self, x, y, radius, farge, vindusobjekt, height, width):
        self.x = x
        self.y = y
        self.radius = radius
        self.farge = farge
        self.vindusobjekt = vindusobjekt
        self.height = height
        self.width = width

    def tegnCircle(self):
     pg.draw.circle(self.vindusobjekt, self.farge, (self.x, self.y), self.radius) 

    def tegnRectangle(self):
        pg.draw.rect(self.vindusobjekt, self.farge, self.height, self.width)

  
    def finnAvstand(self, annenBall):
        xAvstand2 = (self.x - annenBall.x)**2  # x-avstand i andre
        yAvstand2 = (self.y - annenBall.y)**2  # y-avstand i andre
        sentrumsavstand = m.sqrt(xAvstand2 + yAvstand2)

        radiuser = self.radius + annenBall.radius

        avstand = sentrumsavstand - radiuser

        return avstand


class Ball(objekter):
    def __init__(self, x, y, radius, height, width, farge, vindusobjekt, xFart, yFart):
        super().__init__(x, y, radius, height, width,  farge, vindusobjekt)
        self.xFart = xFart
        self.yFart = yFart

    def flytt(self):
        """Method to move the bouncing ball"""
        if ((self.x - self.radius) <= 0) or ((self.x + self.radius) >= self.vindusobjekt.get_width()):
            self.xFart = -self.xFart

        if ((self.y - self.radius) <= 0) or ((self.y + self.radius) >= self.vindusobjekt.get_height()):
            self.yFart = -self.yFart

        self.x += self.xFart
        self.y += self.yFart

class spiller(objekter):
  def __init__(self, x, y, radius, height, width, farge, vindusobjekt, fart):
    super().__init__(x, y, radius, height, width, farge, vindusobjekt)
    self.fart = fart

  def flytt(self, taster):
    """Metode for å flytte spilleren"""
    if taster[K_UP]:
      self.y -= self.fart
    if taster[K_DOWN]:
      self.y += self.fart


ball = Ball(200, 200, 20, 0, 0, (255,0,0), vindu, 2, 2)
spiller1 = spiller(50, 50, 0, 100, 50, (0, 0, 250), vindu, 2)

fortsett = True
while fortsett:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            fortsett = False

    trykkede_taster = pg.key.get_pressed()
    vindu.fill((92, 107, 192))

    ball.tegnCircle()
    ball.flytt()
    spiller1.tegnRectangle()
    spiller1.flytt(trykkede_taster)



    pg.display.flip()

pg.quit()