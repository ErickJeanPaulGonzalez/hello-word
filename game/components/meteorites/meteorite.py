import pygame
import random
from pygame.sprite import Sprite
from game.utils.constants import SCREEN_HEIGHT, METEORITE

class Meteorite(Sprite):
    X_POS_LIST = (50, 100, 150, 200, 250, 300, 350, 400, 450, 500, 550, 600, 650, 700, 750, 800, 850, 900, 950, 1000, 1050, 1100)
    Y_POS = 0 - 80
    MOV_X ={
        0: "left",
        1: "right"
    }

    def __init__(self):
        
        self.meteorite = METEORITE
        self.img_aleatoria = random.randrange(3)
        if self.img_aleatoria == 0:
            self.image_meteorite  = pygame.transform.scale(self.meteorite, (80, 80))
            self.radius = 40
        if self.img_aleatoria == 1:
            self.image_meteorite  = pygame.transform.scale(self.meteorite, (50, 50))
            self.radius = 25
        if self.img_aleatoria == 2:
            self.image_meteorite  = pygame.transform.scale(self.meteorite, (25, 25))
            self.radius = 12
        self.rect = self.image_meteorite.get_rect()
        
        self.rect.x = self.X_POS_LIST[random.randint(0, 21)]
        self.rect.y = self.Y_POS

        self.speed_y = random.randrange(1, 6)
        self.speed_x = random.randrange(1, 6)
        self.movement_x = self.MOV_X[random.randint(0, 1)]
        self.index = 0
        self.move_x_for = random.randint(0, 1100)

    def update(self, meteorite):
        self.rect.y += self.speed_y
            
        # Move meteorite to left or right
        if self.movement_x == "left":
            self.rect.x -= self.speed_x
        else:
            self.rect.x += self.speed_x

        # Remove meteorite when it is outside of screen
        if self.rect.y >= SCREEN_HEIGHT:
            meteorite.remove(self)
        
        # Update rotation angle
        self.index += 1
        if self.index >= 360:
            self.index = 0 

    def draw(self, screen):
        # Rotating the meteorite
        rotated_meteorite = pygame.transform.rotate(self.image_meteorite, self.index)
        screen.blit(rotated_meteorite, (self.rect.x, self.rect.y))