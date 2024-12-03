import pygame.sprite

from settings import *

class Entity(pygame.sprite.Sprite):
    def __init__(self, pos, frames, groups, regard):
        super().__init__(groups)

        #graphics
        self.frames_indice, self.frames = 0, frames
        self.regard = regard

        # Mouvemenent :
        self.direction = vector()
        self.speed = 2500

        # sprite setup
        self.image = self.frames['down'][self.frames_indice]
        self.rect = self.image.get_frect(center = pos)

    def animation(self,dt):
        self.frames_indice += ANIMATION_SPEED * dt
        self.image = self.frames[self.get_etat()][int(self.frames_indice % len(self.frames[self.get_etat()]))]

    def get_etat(self):
        moving = bool(self.direction)
        if moving:
            if self.direction.x != 0:
                self.regard = 'right' if self.direction.x > 0 else 'left'
            if self.direction.y != 0:
                self.regard = 'down' if self.direction.y > 0 else 'up'
        return f"{self.regard}{'' if moving else '_idle'}"

class Dresseur(Entity):
    def __init__(self, pos, frames, groups, regard):
        super().__init__(pos, frames,groups, regard)

class Player(Entity):
    def __init__(self, pos, frames, groups, regard):
        super().__init__(pos, frames, groups, regard)


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
        self.rect.center += self.direction * self.speed * dt

    def update(self, dt):
        self.input()
        self.mouvement(dt)
        self.animation(dt)
