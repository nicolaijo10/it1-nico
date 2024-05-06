
#Kilde: https://github.com/Rabbid76/PyGameExamplesAndAnswers/blob/master/documentation/pygame/pygame_movement_and_motion.md

import pygame
import random

# Konstantar for skjermstørrelse
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600

class Game:
    def __init__(self):
        self.objects = []
        self.lives = 10

    def spawn_object(self):
        # Legg til eit nytt fallande objekt på ein tilfeldig x-posisjon
        x = random.randint(0, SCREEN_WIDTH)
        speed = random.randint(4, 10)
        self.objects.append(FallingObject(x, speed))

    def update(self):
        # Oppdater alle fallende objekter
        for obj in self.objects:
            obj.update()
            # Fjern objektet hvis det er utenfor skjermen, her sjekker den bare at objected sin Y verdi altså opp og ned plasseringen, er høyere enn screen høyden
            if obj.y > SCREEN_HEIGHT:
                #Her fjerner den object hvis den da faller under linjen
                self.objects.remove(obj)
                # Reduser livet til spilleren
                self.lives -= 1

    def check_collisions(self, crosshair):
        for obj in self.objects:
            if crosshair.get_rect().colliderect(obj.get_rect()):
                print("Kollisjon!")
                # Spill lydfilen 'thump.wav' Jeg måtte ta hele pathen til fil locasjonen
                pygame.mixer.Sound('IT2/start/Proove19.04.24/thump.wav').play()
                # Fjern objektet
                self.objects.remove(obj)

class Crosshair:
    def __init__(self):
        self.x = SCREEN_WIDTH / 2
        self.y = SCREEN_HEIGHT / 2

    def draw(self, screen):
        # Teikn siktekrysset
        pygame.draw.line(screen, (255, 255, 255), (self.x - 10, self.y), (self.x + 10, self.y), 2)
        pygame.draw.line(screen, (255, 255, 255), (self.x, self.y - 10), (self.x, self.y + 10), 2)
    
    def get_rect(self):
        return pygame.Rect(self.x - 10, self.y - 10, 20, 20)

class FallingObject:
    def __init__(self, x, speed):
        self.x = x
        self.y = 0
        self.speed = speed

    def update(self):
        # Flytt objektet nedover
        self.y += self.speed

    def draw(self, screen):
        # Tegn objektet som ein firkant
        pygame.draw.rect(screen, (255, 0, 0), pygame.Rect(self.x - 10, self.y - 10, 20, 20))

    def get_rect(self):
        return pygame.Rect(self.x - 10, self.y - 10, 20, 20)

'''
Game loop og hovudprogram
'''

pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
clock = pygame.time.Clock()

# Lag ein font
font = pygame.font.Font(None, 36)

game = Game()
crosshair = Crosshair()

running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Oppdater siktekryssets posisjon til museposisjonen
    crosshair.x, crosshair.y = pygame.mouse.get_pos()

    # Her endret jeg tallet slikt at det spawner mer om gangen. Jeg hadde tenkt å endre det slikt at det spawner mer etter som tiden går, men jeg får ikke tid nå
    if random.random() < 0.025:
        game.spawn_object()

    game.update()

    game.check_collisions(crosshair)

    # Avslutt spillet hvis det ikke er flere liv igjen
    if game.lives <= 0:
        running = False

    screen.fill((0, 0, 0))
    for obj in game.objects:
        obj.draw(screen)
    crosshair.draw(screen)

    # Teikn antall liv på skjermen
    lives_text = font.render(f"Lives: {game.lives}", True, (255, 255, 255))
    screen.blit(lives_text, (10, 10))

    pygame.display.flip()

    clock.tick(60)

pygame.quit()

