import pygame

class BulletManager:
    
    def __init__(self):
        self.bullet = []
        self.enemy_bullets = []
        self.player_bullets = []
        self.meteorites = []
    
    def update(self, game):
        bullets_to_remove = []
        enemies_to_remove = []
        meteorites_to_remove = []
        
        for bullet in self.enemy_bullets:
            bullet.update(self.enemy_bullets)
            
            if bullet.rect.colliderect(game.player.rect) and bullet.owner == "enemy":
                self.enemy_bullets.remove(bullet)
                game.death_count += 1
                game.playing = False
                pygame.time.delay(1000)
                break
            
        for bullet in self.player_bullets:
            bullet.update(self.player_bullets)
            
            for enemy in game.enemy_manager.enemies:
                if bullet.rect.colliderect(enemy.rect) and bullet.owner == "player":
                    bullets_to_remove.append(bullet)
                    enemies_to_remove.append(enemy)
                    game.update_score()
                    print("kill enemy ")
        
            for meteorite in game.meteorite_manager.meteorites:
                if bullet.rect.colliderect(meteorite.rect) and bullet.owner == "player":
                    bullets_to_remove.append(bullet)
                    meteorites_to_remove.append(meteorite)
                    game.update_score()
                    print("kill asteroide ")
        
        for bullet in bullets_to_remove:
            if bullet in self.player_bullets:
                self.player_bullets.remove(bullet)
        
        for enemy in enemies_to_remove:
            if enemy in game.enemy_manager.enemies:
                game.enemy_manager.enemies.remove(enemy)
                
        for meteorite in meteorites_to_remove:
            if meteorite in game.meteorite_manager.meteorites:
                game.meteorite_manager.meteorites.remove(meteorite)
        
    def draw(self, screen):
        for bullet in self.enemy_bullets:
            bullet.draw(screen)
        
        for bullet in self.player_bullets:
            bullet.draw(screen)
            
    def add_bullet(self, bullet):
        if bullet.owner == "enemy" and len(self.enemy_bullets) <= 2:
            self.enemy_bullets.append(bullet)
        
        elif bullet.owner == "player":
            self.player_bullets.append(bullet)
        
        elif bullet.owner == "meteorite":  
            self.player_bullets.append(bullet)
            
    def reset(self):
        self.bullet = []
        self.enemy_bullets = []
        self.player_bullets = []
        self.meteorites = []