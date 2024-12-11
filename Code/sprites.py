from settings import * #importations des parametres globaux depuis le module settings

#classe de base pour tous les sprites du jeu
class Sprite(pygame.sprite.Sprite):
    def __init__(self, pos, surf, groups, z = WORLD_LAYERS['main']):
        #initialise un sprite générique
        super().__init__(groups) #ajoute ce sprite aux groupes spécifiés
        self.image = surf #image ou surface graphique du sprite
        self.rect = self.image.get_frect(topleft = pos) # rectangle de position basé sur la surface
        self.z = z #niveau de profondeur pour le tri
        self.y_sort = self.rect.centery  # utilisé pour trier les sprites par leur position verticale
        self.hitbox = self.rect.copy() #hitbox par défaut identique au rectangle graphique

# sprite représentant une bordure, avec une hitbox par défaut
class BorderSprite(Sprite):
    def __init__(self, pos, surf, groups):
        #initialise un sprite de bordure.
        super().__init__(pos, surf, groups)
        self.hitbox = self.rect.copy()

#sprite utilisé pour représenter les transitions entre zones
class TransitionSprite(Sprite):
    #initialise un sprite de transition
    def __init__(self, pos, size, target, groups):
        #surface transparente utilisée comme placeholder
        surf = pygame.Surface(size)
        super().__init__(pos, surf, groups)
        self.target = target #destination de la transition (carte, position)

#sprite interactif ayant une hitbox ajusté pour detecter les collisions
class CollidableSprite(Sprite):
    def __init__(self, pos, surf, groups):
        #initialise un sprite avec une hitbox ajustée pour les collisions
        super().__init__(pos, surf, groups)
        #la hitbox est réduite verticalement pour mieux correspondre à la taille réelle de l'objet
        self.hitbox = self.rect.inflate(0, -self.rect.height * 0.4)

#sprite représentant une zone d'herbe où des Waremons peuvent apparaître
class Waremon_patch_Sprite(Sprite):
    #initialise une zone spéciale pour Waremons
    def __init__(self, pos, surf, groups):
        super().__init__(pos, surf, groups, WORLD_LAYERS['main'])
        self.y_sort -= 40 #ajuste la position de tri vertical pour cet objet spécifique

#sprite animé pouvant changer d'image à chaque frame
class Animation(Sprite):
    #initialise un spritte animé
    def __init__(self, pos, frames, groups, z = WORLD_LAYERS['main']):
        self.frames_indice, self.frames = 0, frames #initialisation de l'indice et des frames
        super().__init__(pos, frames[self.frames_indice],groups, z)

    def animate(self, dt):
        #met à jour l'image de l'animation en fonction du temps écoulé
        self.frames_indice += ANIMATION_SPEED * dt #incrémente l'indice en fonction de la vitesse
        self.image = self.frames[int(self.frames_indice % len(self.frames))] #change l'image active

    def update(self, dt):
        #appelle la méthode d'animation pour chaque mise à jour
        self.animate(dt) #met a jour l'animation