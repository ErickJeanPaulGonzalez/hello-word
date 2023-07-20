import pygame
import random
from pygame.sprite import Sprite
from game.utils.constants import ENEMY_1, ENEMY_2, SCREEN_HEIGHT, SCREEN_WIDTH
from game.components.bullets.bullets import Bullet


class Enemy(Sprite):
    X_POS_LIST = [50, 100, 150, 200, 250, 300, 350, 400, 450, 500, 550]
    Y_POS = 20
    SPEED_Y = 1
    SPEED_X = 5
    MOV_X = {0: "left", 1: "right"}
    SHIP_WIDTH = 40 
    SHIP_HEIGHT = 60 
    IMAGE = {1: ENEMY_1, 2:ENEMY_2}
    
    def __init__(self, image = 1, speed_x = SPEED_X, speed_y = SPEED_Y, move_x_for = [30, 100] ):
        self.image = self.IMAGE[image]
        self.image = pygame.transform.scale(self.image, (self.SHIP_WIDTH, self.SHIP_HEIGHT))
        self.rect = self.image.get_rect()
        self.rect.x = self.X_POS_LIST[random.randint(0, 10)]
        self.rect.y = self.Y_POS
        self.speed_y = speed_y
        self.speed_x = speed_x
        self.movement_x = self.MOV_X[random.randint(0,1)]
        self.index = 0
        self.move_x_for = random.randint(move_x_for[0], move_x_for[1])
        self.type = "enemy"
        self.shooting_time = random.randint(30, 50)
    
    def update(self, ship, game):
        self.rect.y += self.speed_y
        
        #Shoot a bullet
        self.shoot(game.bullet_manager)
    
        #Move enemy to left or right
        if self.movement_x == "left":
            self.rect.x -= self.speed_x
        else:
            self.rect.x += self.speed_x

        self.change_movement_x()

        #remove ship whe it is outside of screeen 
        if self.rect.y >= SCREEN_HEIGHT:
            ship.remove(self)
    
    def draw(self, screen):
        screen.blit(self.image, (self.rect.x, self.rect.y))
        
    def change_movement_x(self):
        self.index += 1
        
        #Validate if ship go out from the screen 
        if (self.index >= self.move_x_for and self.movement_x == "right") or (self.rect.x >= SCREEN_WIDTH - self.SHIP_WIDTH):
            self.movement_x = "left"
            self.index = 0
        elif (self.index >= self.move_x_for and self.movement_x == "left") or self.rect.x <= 0:
            self.movement_x = "right"
            self.index = 0
        
    def shoot(self, bullet_manager):
        current_time = pygame.time.get_ticks()
        #if shooting time is less than current time, create a bullet object 
        current_time = pygame.time.get_ticks()
        if self.shooting_time <= current_time:
            bullet = Bullet(self) ##send enemy ship 
            bullet_manager.add_bullet(bullet)
            self.shooting_time += random.randint(30, 50)