import pygame.sprite

from settings import *

class Entity(pygame.sprite.Sprite):
    def __init__(self, pos, frames, groups):
        super().__init__(groups)

        #graphics
        self.frames_indice, self.frames = 0, frames

        # sprite setup
        self.image = self.frames['down'][self.frames_indice]
        self.rect = self.image.get_frect(center = pos)

class Player(Entity):
    def __init__(self, pos, frames, groups):
        super().__init__(pos, frames, groups)

        self.direction = vector()


    def input(self):
        keys = pygame.key.get_pressed()
        input_vector = vector()
        if keys[pygame.K_UP]:
            input_vector.y -= 1
        if keys[pygame.K_DOWN]:
            input_vector.y += 1
        if keys[pygame.K_LEFT]:
            input_vector.x -= 1
        if keys[pygame.K_RIGHT]:
            input_vector.x += 1
        self.direction = input_vector


    def mouvement(self, dt):
        self.rect.center += self.direction * 2500 * dt

    def update(self, dt):
        self.input()
        self.mouvement(dt)
