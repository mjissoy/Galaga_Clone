from typing import Any
import pygame
from pygame.sprite import Group, Sprite

class Bullet(Sprite):

    def __init__(self, gc_settings, screen, ship):
        super().__init__()
        self.screen = screen

        self.rect = pygame.Rect(0, 0, gc_settings.bullet_width, gc_settings.bullet_height)
        self.rect.centerx = ship.rect.centerx
        self.rect.top = ship.rect.top

        self.y = float(self.rect.y)

        self.colour = gc_settings.bullet_color
        self.speed_factor = gc_settings.bullet_speed_factor
    
    def update(self):
        self.y -= self.speed_factor
        self.rect.y = self.y

    def draw_bullet(self):
        pygame.draw.rect(self.screen, self.colour, self.rect)