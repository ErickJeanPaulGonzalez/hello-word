import pygame
import random
from game.components.power_ups.shield import Shield
from game.utils.constants import SPACESHIP_SHIELD

class PowerUpManager:
    def __init__(self):
        self.power_ups = []
        self.when_appears = random.randint(5000, 10000) # time to appears
        self.duration = random.randint(3, 5)

    def update(self, game):
        curret_time = pygame.time.get_ticks()

        # Generating power ups
        if len(self.power_ups) == 0 and curret_time >= self.when_appears:
            self.generate_power_up()

        # Update each power up
        for power_up in self.power_ups:
            power_up.update(game.game_speed, self.power_ups)
            if game.player.rect.colliderect(power_up.rect):
                power_up.start_time = pygame.time.get_ticks()
                game.player.power_up_type = power_up.type
                game.player.has_power_up = True
                game.player.time_with_power = power_up.start_time + (self.duration * 1000)
                # chamge player ship
                game.player.set_image(SPACESHIP_SHIELD, (65, 75))
                self.power_ups.remove(power_up)

    def draw(self, screen):
        for power_up in self.power_ups:
            power_up.draw(screen)

    def generate_power_up(self):
        power_up = Shield()
        self.when_appears += random.randint(5000, 10000)
        self.power_ups.append(power_up)

    def reset(self):
        self.power_ups = []
        self.when_appears = pygame.time.get_ticks()
        self.duration = random.randint(3, 5)