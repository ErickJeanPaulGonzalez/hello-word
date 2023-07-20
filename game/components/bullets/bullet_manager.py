import pygame
from game.utils.constants import SHIELD_TYPE

class BulletManager:
    def __init__(self):
        self.bullets = []
        self.enemy_bullets = []

    def update(self, game):
        # Update player bullets
        for bullet in self.bullets:
            bullet.update(self.bullets)
            # Verify collision between player bullet and enemies
            for enemy in game.enemy_manager.enemies:
                if bullet.rect.colliderect(enemy.rect) and bullet.owner != "enemy":
                    game.enemy_manager.enemies.remove(enemy)
                    game.score.update()
                    self.bullets.remove(bullet)
                    pygame.time.delay(100)
                    break

        # Update enemy bullets
        for bullet in self.enemy_bullets:
            bullet.update(self.enemy_bullets)
            # Verify collision between enemy bullet and player
            if bullet.rect.colliderect(game.player.rect) and bullet.owner == "enemy":
                self.enemy_bullets.remove(bullet)
                if game.player.power_up_type != SHIELD_TYPE:
                    game.death_count.update()
                    game.playing = False
                    pygame.time.delay(1000)
                    break


    def draw(self, screen):
        # Draw player bullets
        for bullet in self.bullets:
            bullet.draw(screen)

        # Draw enemy bullets
        for bullet in self.enemy_bullets:
            bullet.draw(screen)

    def add_bullet(self, bullet):
        # Adding bullets to player or enemy
        if bullet.owner == "player" and  len(self.bullets) < 2: # 2 bullets
            self.bullets.append(bullet)
        elif bullet.owner == "enemy" and len(self.enemy_bullets) < 1:
            self.enemy_bullets.append(bullet)
    
    def reset(self):
        self.bullets = []
        self.enemy_bullets = []