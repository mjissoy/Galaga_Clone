from typing import Any
import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
    def __init__(self, gc_settings, screen):

        super(Alien, self).__init__()
        self.screen = screen
        self.gc_settings = gc_settings

        self.image = pygame.image.load('EditionCourseBook\Galaga_Clone\Images\Ship_4.bmp')
        self.rect = self.image.get_rect()

        self.rect.x = self.rect.width
        self.rect.y = self.rect.height
        
        self.x = float(self.rect.x)

    def blitme(self):
        self.screen.blit(self.image, self.rect)
    
    def check_edges(self):
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right:
            return True
        elif self.rect.left <= 0:
            return True

    def update(self):
            self.x += (self.gc_settings.alien_speed_factor * self.gc_settings.fleet_direction)
            self.rect.x = self.x