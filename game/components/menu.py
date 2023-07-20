import pygame
from game.utils.constants import FONT_STYLE, SCREEN_HEIGHT, SCREEN_WIDTH

class Menu:
    HALF_SCREEN_WIDTH = SCREEN_WIDTH // 2
    HALF_SCREEN_HEIGHT = SCREEN_HEIGHT //2
    def __init__(self, message, screen ):
        screen.fill((255, 0,0))
        self.font = pygame.font.Font(FONT_STYLE, 30)
        self.text = self.font.render(message, True, (0, 0, 0))
        self.text_rect = self.text.get_rect()
        self.text_rect.center = (self.HALF_SCREEN_WIDTH, self.HALF_SCREEN_HEIGHT)
        #modificate
        self.font_text = pygame.font.Font(FONT_STYLE, 30)
        self.text_scores = self.font_text.render(message, True, (0, 0, 0))
        self.text_scores_rect = self.text_scores.get_rect()
        self.text_scores_rect.center = (self.HALF_SCREEN_WIDTH , self.HALF_SCREEN_HEIGHT)
        
        #modificate
        
    def update(self, game):
        pygame.display.update()
        self.handle_events_on_menu(game)
    
    def draw(self, screen):
        screen.blit(self.text,self.text_rect )
        
    def handle_events_on_menu(self, game):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game.playing = False 
                game.running = False
            elif event.type == pygame.KEYDOWN:
                game.run()
    
    def reset_screen_color(self, screen):
        screen.fill((255, 255, 255))
        
    def update_message(self, message):
        self.text = self.font.render(message, True, (0,0,0))
        self.text_rect = self.text.get_rect()
        self.text_rect.center = (self.HALF_SCREEN_WIDTH, self.HALF_SCREEN_HEIGHT)
        print("put")
        #modificate
    def update_scores(self, message, screen, position):
        self.text_scores = self.font.render(message, True, (0, 0, 0))
        self.text_scores_rect = self.text_scores.get_rect()
        self.text_scores_rect.center = (position)
        screen.blit(self.text_scores, self.text_scores_rect)
        #modificate
        print("per")