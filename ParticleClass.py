import pygame
import math

WHITE = (255, 255, 255)
GREEN = (0, 128, 0)
BLUE = (0, 0, 255)
AQUA = (0, 255, 255)#CYAN
BLACK = (0, 0, 0)
FUCHSIA = (255, 0, 255)
GRAY = (128, 128, 128)
LIME = (0, 255, 0)
MAROON = (128, 0, 0)
NAVYBLUE = (0, 0, 128)
OLIVE = (128, 128, 0)
PURPLE = (128, 0, 128)
RED = (255, 0, 0)
SILVER = (192, 192, 192)
TEAL = (0, 128, 128)
WHITE = (255, 255, 255)
YELLOW = (255, 255, 0)
ORANGE = (255, 128, 0)
CYAN = (0, 255, 255) #AQUA
HOTPINK = (255, 105, 180)

class Particle(pygame.sprite.Sprite):
    def __init__(self,game, x, y):
        self.groups = game.active_sprite_list, game.particle_list        
        pygame.sprite.Sprite.__init__(self, self.groups)
        
        self.game = game
        
        self.x = x
        self.y = y
        
        self.image = pygame.Surface((5, 5))
        self.image.fill(BLACK)
        
        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y
        
    def get_rect(self):
        return self.rect
    
    #def set_rect(self):
    #    self.rect = pygame.Rect(self.x-self.size, self.y-self.size, self.size*2, self.size*2)

    #def delete(self, particleList):
    #    particleList.remove(self)

    #def update(self, display):
    #    pygame.draw.circle(display, self.color, (int(self.x), int(self.y)), self.size, self.thickness)
        
    def move(self):
        pass
        
    def update(self):
        pass
        
        
        