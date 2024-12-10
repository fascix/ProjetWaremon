import pygame.sprite

from settings import *

class Entity(pygame.sprite.Sprite):
    def __init__(self, pos, frames, groups, regard):
        super().__init__(groups)
        self.z = WORLD_LAYERS['main']



        #graphics
        self.frames_indice, self.frames = 0, frames
        self.regard = regard

        # Mouvemenent :
        self.direction = vector()
        self.speed = 1000
        self.blocked = False

        # sprite setup
        self.image = self.frames['down'][self.frames_indice]
        self.rect = self.image.get_frect(center = pos)
        self.hitbox = self.rect.inflate(-self.rect.width / 2, -60)
        self.y_sort = self.rect.centery

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



    def block(self):
        self.blocked = True
        self.direction = vector(0,0)

    def unblock(self):
        self.blocked = False

class Dresseur(Entity):
    def __init__(self, pos, frames, groups, regard):
        super().__init__(pos, frames,groups, regard)


class Player(Entity):
    def __init__(self, pos, frames, groups, regard, collision_sprites):
        super().__init__(pos, frames, groups, regard)
        self.collision_sprites = collision_sprites

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
        self.direction = input_vector.normalize() if input_vector else input_vector


    def mouvement(self, dt):
        self.rect.centerx += self.direction.x * self.speed * dt
        self.hitbox.centerx = self.rect.centerx
        self.collisions('horizontale')

        self.rect.centery += self.direction.y * self.speed * dt
        self.hitbox.centery = self.rect.centery
        self.collisions('verticale')

    def collisions(self, axis):
        for sprite in self.collision_sprites:
            if sprite.hitbox.colliderect(self.hitbox):
                if axis == 'horizontale':
                    if self.direction.x > 0:  # Déplacement à droite
                        self.hitbox.right = sprite.hitbox.left
                    if self.direction.x < 0:  # Déplacement à gauche
                        self.hitbox.left = sprite.hitbox.right
                    self.rect.centerx = self.hitbox.centerx  # Synchronisation
                else:
                    if self.direction.y > 0:  # Déplacement vers le bas
                        self.hitbox.bottom = sprite.hitbox.top
                    if self.direction.y < 0:  # Déplacement vers le haut
                        self.hitbox.top = sprite.hitbox.bottom
                    self.rect.centery = self.hitbox.centery  # Synchronisation

    def update(self, dt):
        self.y_sort = self.rect.centery
        if not self.blocked:
            self.input()
            self.mouvement(dt)
        self.animation(dt)
