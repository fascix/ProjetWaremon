import pygame.sprite

from settings import *
from support import import_image
from entities import *

class AllSprites(pygame.sprite.Group):
    def __init__(self):
        super().__init__()
        self.display_surface = pygame.display.get_surface()
        self.offset = vector()
        self.ombre_surf = import_image('..', 'graphics', 'other', 'ombre')

    def draw(self, player_center):
        self.offset.x = -(player_center[0] - WINDOW_WIDTH /2)
        self.offset.y = -(player_center[1] - WINDOW_HEIGHT /2)

        bg_sprite = [sprite for sprite in self if sprite.z < WORLD_LAYERS['main']]
        main_sprite = sorted([sprite for sprite in self if sprite.z == WORLD_LAYERS['main']], key=lambda sprite: sprite.y_sort)
        fg_sprite = [sprite for sprite in self if sprite.z > WORLD_LAYERS['main']]

        for layer in (bg_sprite, main_sprite, fg_sprite):
            for sprite in layer:
                if isinstance(sprite, Player):
                    self.display_surface.blit(self.ombre_surf, sprite.rect.topleft + self.offset + vector(25, 120))
                if isinstance(sprite, Dresseur):
                    self.display_surface.blit(self.ombre_surf, sprite.rect.topleft + self.offset + vector(40, 110))
                self.display_surface.blit(sprite.image, sprite.rect.topleft + self.offset)