'''
import pygame

# Initialiser Pygame
pygame.init()

# Definer farger
green = (0, 146, 70)
white = (255, 255, 255)
red = (206, 17, 38)

# Størrelse på vinduet
width, height = 900, 600
flag_width = width // 3

# Opprett vindu
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('Italiensk flagg')

# Loop for å tegne flagget
running = True
while running:
    screen.fill(white)

    # Tegn de tre stripene
    pygame.draw.rect(screen, green, (0, 0, flag_width, height))
    pygame.draw.rect(screen, white, (flag_width, 0, flag_width, height))
    pygame.draw.rect(screen, red, (flag_width * 2, 0, flag_width, height))

    # Oppdater vindu
    pygame.display.flip()

    # Håndter hendelser
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

# Avslutt Pygame
pygame.quit()
'''

'''
import pygame as pg
import math as m

# Initialiserer/starter pygame
pg.init()

# Oppretter et vindu der vi skal "tegne" innholdet vårt
VINDU_BREDDE = 850
VINDU_HOYDE  = 700
vindu = pg.display.set_mode([VINDU_BREDDE, VINDU_HOYDE])


class Ball:
    def __init__(self, x, y, xFart, yFart, radius, farge, vindusobjekt):
        self.x = x
        self.y = y
        self.xFart = xFart
        self.yFart = yFart
        self.radius = radius
        self.farge = farge
        self.vindusobjekt = vindusobjekt

    def tegn(self):
        pg.draw.circle(self.vindusobjekt, self.farge, (self.x, self.y), self.radius)

    def flytt(self):
        if (self.x - self.radius) <= 0 or (self.x + self.radius) >= self.vindusobjekt.get_width():
            self.xFart = -self.xFart
        if (self.y - self.radius) <= 0 or (self.y + self.radius) >= self.vindusobjekt.get_height():
            self.yFart = -self.yFart
        
        self.x += self.xFart
        self.y += self.yFart


# Lager et Ball-objekt.
# Lager et Ball-objekt med x- og y-fart
ball1 = Ball(200, 200, 0.5, 0.8, 20, (255, 69, 0), vindu)
ball2 = Ball(100, 100, 0.4, 0.5, 20, (255, 69, 0), vindu)

def finnAvstand(ball1, ball2):
  xAvstand2 = (ball1.x - ball2.x)**2  # x-avstand i andre
  yAvstand2 = (ball1.y - ball2.y)**2  # y-avstand i andre
  avstand = m.sqrt(xAvstand2 + yAvstand2)

  return avstand

# Gjenta helt til brukeren lukker vinduet
fortsett = True
while fortsett:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            fortsett = False

    vindu.fill((0, 0, 0))

    ball1.tegn()
    ball2.tegn()
    
    avstand_mellom_ballene = finnAvstand(ball1, ball2)
    if avstand_mellom_ballene <= ball1.radius + ball2.radius:
        ball1.xFart, ball2.xFart = ball2.xFart, ball1.xFart
        ball1.yFart, ball2.yFart = ball2.yFart, ball1.yFart
    
    ball1.flytt()
    ball2.flytt()

    pg.display.flip()

pg.quit()

'''
import pygame as pg
import math as m
from pygame.locals import (K_UP, K_DOWN, K_LEFT, K_RIGHT)

# Initialiserer/starter pygame
pg.init()

# Oppretter et vindu der vi skal "tegne" innholdet vårt
VINDU_BREDDE = 500
VINDU_HOYDE  = 500
vindu = pg.display.set_mode([VINDU_BREDDE, VINDU_HOYDE])

class Ball:
  """Klasse for å representere en ball"""
  def __init__(self, x, y, fart, radius, farge, vindusobjekt):
    """Konstruktør"""
    self.x = x
    self.y = y
    self.fart = fart
    self.radius = radius
    self.farge = farge
    self.vindusobjekt = vindusobjekt
  
  def tegn(self):
    """Metode for å tegne ballen"""
    pg.draw.circle(self.vindusobjekt, self.farge, (self.x, self.y), self.radius) 

  def flytt(self, taster):
    """Metode for å flytte ballen"""
    if taster[K_UP]:
      self.y -= self.fart
    if taster[K_DOWN]:
      self.y += self.fart
    if taster[K_LEFT]:
      self.x -= self.fart
    if taster[K_RIGHT]:
      self.x += self.fart

# Lager et Ball-objekt
ball = Ball(200, 200, 0.1, 20, (255, 69, 0), vindu)

# Gjenta helt til brukeren lukker vinduet
fortsett = True
while fortsett:

    # Sjekker om brukeren har lukket vinduet
    for event in pg.event.get():
        if event.type == pg.QUIT:
            fortsett = False

    # Henter en ordbok med status for alle tastatur-taster
    trykkede_taster = pg.key.get_pressed()

    # Farger bakgrunnen lyseblå
    vindu.fill((135, 206, 235))

    # Tegner og flytter ballene
    ball.tegn()
    ball.flytt(trykkede_taster)

    # Oppdaterer alt innholdet i vinduet
    pg.display.flip()

# Avslutter pygame
pg.quit()