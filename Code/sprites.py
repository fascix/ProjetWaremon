from settings import *

class Sprite(pygame.sprite.Sprite):
    def __init__(self, pos, surf, groups):
        super().__init__(groups)
        self.image = surf
        self.rect = self.image.get_frect(topleft = pos)

class Animation(Sprite):
    def __init__(self, pos, frames, groups):
        self.frames_indice, self.frames = 0, frames
        super().__init__(pos, frames[self.frames_indice],groups)

    def animate(self, dt):
        self.frames_indice += ANIMATION_SPEED * dt
        self.image = self.frames[int(self.frames_indice % len(self.frames))]

    def update(self, dt):
        self.animate(dt)