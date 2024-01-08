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

import pygame as pg

# Initialiserer/starter pygame
pg.init()

# Oppretter et vindu der vi skal "tegne" innholdet vårt
VINDU_BREDDE = 500
VINDU_HOYDE  = 500
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
ball = Ball(250, 250, 0.1, 0.3, 20, (255, 69, 0), vindu)


# Gjenta helt til brukeren lukker vinduet
fortsett = True
while fortsett:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            fortsett = False

    vindu.fill((135, 206, 235))

    ball.tegn()
    ball.flytt()

    pg.display.flip()

pg.quit()

