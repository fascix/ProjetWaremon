import pygame.sprite

from settings import * #importation de constantes et configurations
from support import import_image #importation de la fonction pour charger une image
from entities import * #importation des entités

#classe allsprites qui hérite de pygame.sprite.group
class AllSprites(pygame.sprite.Group):
    def __init__(self):
        super().__init__() #appel du constructeur parent pour initialiser un groupe d'entités
        self.display_surface = pygame.display.get_surface() #recuperation de la surface d'affichage de la fenêtre
        self.offset = vector() #initialisation de l'offset pour le déplacement de la vue
        self.ombre_surf = import_image('..', 'graphics', 'other', 'ombre') # chargement de l'image d'ombre

    #méthode pour dessiner les sprites à l'écran en fonction de la position du joueur
    def draw(self, player_center):
        #calcul de l'offset pour centrer l'écran sur le joueur
        self.offset.x = -(player_center[0] - WINDOW_WIDTH /2) #decalage x
        self.offset.y = -(player_center[1] - WINDOW_HEIGHT /2)#decalage y

        #séparation des sprites selon leur profondeur dans le monde (couches)
        bg_sprite = [sprite for sprite in self if sprite.z < WORLD_LAYERS['main']] #sprites d'arrière plan
        main_sprite = sorted([sprite for sprite in self if sprite.z == WORLD_LAYERS['main']], key=lambda sprite: sprite.y_sort) #sprites principaux triés par position verticale
        fg_sprite = [sprite for sprite in self if sprite.z > WORLD_LAYERS['main']] #sprites au premier plan

        #dessin des sprites par couche
        for layer in (bg_sprite, main_sprite, fg_sprite):
            for sprite in layer:
                #si le sprite est un joueur, on lui ajoute une ombre
                if isinstance(sprite, Player):
                    self.display_surface.blit(self.ombre_surf, sprite.rect.topleft + self.offset + vector(25, 120))
                #si le sprite est un dresseur, on lui ajoute aussi une ombre
                if isinstance(sprite, Dresseur):
                    self.display_surface.blit(self.ombre_surf, sprite.rect.topleft + self.offset + vector(40, 110))
                #dessine le sprite à l'ecran
                self.display_surface.blit(sprite.image, sprite.rect.topleft + self.offset)