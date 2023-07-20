import pygame
from pygame.sprite import Sprite
from game.utils.constants import BULLET, BULLET_ENEMY, SCREEN_HEIGHT

class Bullet(Sprite):
    BULLET_SIZE = pygame.transform.scale(BULLET, (10, 20))
    BULLET_ENEMY_SIZE = pygame.transform.scale(BULLET_ENEMY, (9, 32))
    BULLETS = {"player": BULLET_SIZE, "enemy": BULLET_ENEMY_SIZE}
    SPEED = 20

    def __init__(self, spaceship):
        self.image = self.BULLETS[spaceship.type]
        self.rect = self.image.get_rect()
        self.rect.center = spaceship.rect.center
        self.owner = spaceship.type

    def update(self, bullets):
        # Verify if bullet belongs to player or enemy
        if self.owner == "player":
            self.rect.y -= self.SPEED
        else:
            self.rect.y += self.SPEED

        # Remove bullet if it is outside of the screen
        if self.rect.y >=SCREEN_HEIGHT or self.rect.y < 0:
            bullets.remove(self)

    def draw(self, screen):
        screen.blit(self.image, (self.rect.x, self.rect.y))