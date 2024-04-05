import pygame
import sys
import random
import math


#Kilde: https://github.com/Rabbid76/PyGameExamplesAndAnswers/blob/master/documentation/pygame/pygame_movement_and_motion.md.
#Denne delen slet jeg med, men fant et stort biblotek av informasjon på en github side som hjalp meg
def move_to(pos, target_pos, vel):
    dx, dy = target_pos[0] - pos[0], target_pos[1]- pos[1]
    dist = math.hypot(dx, dy)
    if dist > 0:
        dx, dy = round(dx * vel / dist), round(dy * vel / dist)
        xyb = target_pos if dist < vel else [pos[0] + dx,  pos[1] + dy]  
    return xyb

class Objekt:
    def __init__(self, x, y, speed):
        self.x = x
        self.y = y
        self.speed = speed

    def move(self, key):
        if key[pygame.K_w]:
            self.y -= self.speed
        if key[pygame.K_s]:
            self.y += self.speed
        if key[pygame.K_a]:
            self.x -= self.speed
        if key[pygame.K_d]:
            self.x += self.speed

    def distance_to(self, target_x, target_y):
        return ((self.x - target_x) ** 2 + (self.y - target_y) ** 2) ** 0.5

    def draw(self, screen):
        pass

class Spiller(Objekt):
    def __init__(self):
        super().__init__(300, 200, 5)
        self.radius = 15

    def draw(self, screen):
        pygame.draw.circle(screen, (255, 255, 255), (self.x, self.y), self.radius)

    def attack(self, enemies):
        for enemy in enemies:
            if self.distance_to(enemy.x, enemy.y) < 150:
                enemies.remove(enemy)

class Enemy(Objekt):
    def __init__(self, Spiller):
        x = random.choice([random.randint(0, 600), random.randint(0, 400)])
        y = random.choice([random.randint(0, 600), random.randint(0, 400)])
        super().__init__(x, y, 2)
        self.radius = 10
        self.Spiller = Spiller

    def draw(self, screen):
        pygame.draw.circle(screen, (255, 0, 0), (self.x, self.y), self.radius)

    def update(self):
        self.x, self.y = move_to([self.x, self.y], [self.Spiller.x, self.Spiller.y], self.speed)


def main():
    pygame.init()
    screen = pygame.display.set_mode((600, 400))
    clock = pygame.time.Clock()

    Spiller1 = Spiller()
    enemies = []

    enemy_timer = 0

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    Spiller1.attack(enemies)

        screen.fill((0, 0, 0))
        Spiller1.draw(screen)
        Spiller1.move(pygame.key.get_pressed())

        for enemy in enemies:
            enemy.update()
            enemy.draw(screen)
            if Spiller1.distance_to(enemy.x, enemy.y) < Spiller1.radius + enemy.radius:
                pygame.quit()
                sys.exit()

        if enemy_timer % 100 == 0:
            enemies.append(Enemy(Spiller1))

        enemy_timer += 1

        pygame.display.flip()
        clock.tick(60)

if __name__ == "__main__":
    main()
