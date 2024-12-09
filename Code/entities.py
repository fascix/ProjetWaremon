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
        self.speed = 250
        self.blocked = False

        # sprite setup
        self.image = self.frames['down'][self.frames_indice]
        self.rect = self.image.get_frect(center = pos)
        self.hitbox = self.rect.inflate(-self.rect.width / 2, -60)
        self.y_sort = self.rect.centery

    def animation(self, dt):
        print("Frames:", self.frames)  # Ajout pour débogage
        print("État actuel:", self.get_etat())  # Affiche l'état pour lequel on recherche les frames
        try:
            self.image = self.frames[self.get_etat()][int(self.frames_indice % len(self.frames[self.get_etat()]))]
        except KeyError as e:
            print(f"Erreur: Clé {e} introuvable dans self.frames")
            raise

    def get_etat(self):
        moving = bool(self.direction)
        if moving:
            if self.direction.x != 0:
                self.regard = 'right' if self.direction.x > 0 else 'left'
            if self.direction.y != 0:
                self.regard = 'down' if self.direction.y > 0 else 'up'
        return f"{self.regard}{'' if moving else '_idle'}"

    def change_regard(self, target_pos):
        relation = vector(target_pos) - vector(self.rect.center)
        if abs(relation.y) < 30:
            self.regard = 'right' if relation.x > 0 else 'left'
        else:
            self.regard = 'down' if relation.y > 0 else 'up'

    def block(self):
        self.blocked = True

    def unblock(self):
        self.blocked = False
        self.direction = vector(0,0)

class Dresseur(Entity):
    def __init__(self, pos, frames, groups, regard, character_data):
        super().__init__(pos, frames,groups, regard)
        self.character_data = character_data

    def get_dialogues(self):
        return self.character_data['dialogues'][f'{vaincu}' if self.character_data['vaincu'] else 'défaut']

    def update(self, dt):
        self.animation(dt)

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
