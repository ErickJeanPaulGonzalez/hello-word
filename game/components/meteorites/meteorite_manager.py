import time
import random
from game.components.meteorites.meteorite import Meteorite

class MeteoriteManager():
    
    def __init__(self):
        self.meteorites = []
        # Track the time of the last meteorite generated
        self.last_meteorite_time = time.time()  

    def update(self, game):
        self.add_meteorite()
        for meteorite in self.meteorites:
            meteorite.update(self.meteorites)
            
            if meteorite.rect.colliderect(game.player.rect):
                self.meteorites.remove(meteorite)
                game.playing = False
                break

    def draw(self, screen):
        for meteorite in self.meteorites:
            meteorite.draw(screen)

    def add_meteorite(self):
        # Adjusts random delay between meteors
        self.current_time = time.time()
        if len(self.meteorites) < 30 and self.current_time - self.last_meteorite_time > random.uniform(2.0, 3.0):
            meteorite = Meteorite()
            self.meteorites.append(meteorite)
            self.last_meteorite_time = self.current_time  # Updating the time of the last generated meteorite

    def generate_meteorite(self):
        self.new_meteorite = Meteorite()
        self.meteorite_group.add(self.new_meteorite)