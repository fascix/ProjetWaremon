from support import play_music
from sprites import Waremon_patch_Sprite
from settings import *
from pytmx.util_pygame import load_pygame
from os.path import join
from sprites import *
from entities import *
from group import AllSprites
from support import *

class Game:
    def __init__(self):
        #initialisation de pygame et configuration de la fenêtre principale
        pygame.init()
        self.display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
        pygame.display.set_caption('Waremon')
        self.clock = pygame.time.Clock()

        #groupes de sprites pour organiser les entités du jeu:
        self.all_sprites = AllSprites() # tous les sprites
        self.collision_sprites = pygame.sprite.Group() #sprites avec collision
        self.character_sprites = pygame.sprite.Group() #sprites de personnages
        self.transition_sprites = pygame.sprite.Group() #sprites de transition

        #paramètres pour les transitions entre zones
        self.transition_target = None #cible de la transition
        self.tint_surf = pygame.Surface((WINDOW_WIDTH, WINDOW_HEIGHT)) #surface pour le fondu
        self.tint_mode = 'untint' # mode de fondu
        self.tint_progress = 0 #progression du fondu
        self.tint_direction= -1 #direction du fondu(-1 pour retirer, +1 pour ajouter)
        self.tint_speed = 600 # vitesse du fondu

        #chargement des ressources et configuration initiales
        self.import_assets()
        self.setup(self.tmx_maps['map3'], 'house')

        #lecture de la musique de fond
        play_music("Mijn.mp3", volume=1)

    def import_assets(self): #charge les cartes, animations

        #chargement des cartes au format TMX
        self.tmx_maps = {
            'map3' : load_pygame(join('..', 'data', 'maps', 'map3.tmx')),
            'plant' : load_pygame(join('..', 'data', 'maps', 'house.tmx')),
        }

        #chargement des frames pour les animations
        self.overwolrd_frames = {
            'water': import_folder(join('..', 'graphics', 'tilesets', 'water')),
            'cote' : cote_importer(24,12,join('..', 'graphics', 'tilesets', 'cote')),
            'characters': all_character_import('..', 'graphics', 'characters')
        }


    # noinspection PyTypeChecker
    def setup(self, tmx_map, player_start_pos): #configure les sprites et entités pour une nouvelle carte
        #réinitialisation des groupes de sprites
        for group in (self.all_sprites, self.collision_sprites, self.transition_sprites, self.character_sprites):
            group.empty()

        # map 3 :
        #chargement des différentes couches de la carte
        for layer in ['Terrain', 'Terrain haut']:
            for x, y, surf in tmx_map.get_layer_by_name(layer).tiles():
                Sprite((x * TILE_SIZE, y * TILE_SIZE), surf, self.all_sprites, WORLD_LAYERS['bg'])

        #ajout des animations pour les zones d'eau
        for obj in tmx_map.get_layer_by_name('water'):
            for x in range(int(obj.x), int(obj.x+obj.width), TILE_SIZE):
                for y in range(int(obj.y), int(obj.y+obj.height), TILE_SIZE):
                    Animation((x,y), self.overwolrd_frames['water'], self.all_sprites, WORLD_LAYERS['water'])

        #ajout des animations pour les côtes
        for obj in tmx_map.get_layer_by_name('Côtes'):
            terrain = obj.properties['terrain']
            side = obj.properties['side']
            Animation((obj.x, obj.y),self.overwolrd_frames['cote'][terrain][side], self.all_sprites, WORLD_LAYERS['bg'])

        #création des objets avec collision
        for obj in tmx_map.get_layer_by_name('Objets'):
            CollidableSprite((obj.x, obj.y), obj.image, (self.all_sprites, self.collision_sprites))

        #création des transitions entre zones
        for obj in tmx_map.get_layer_by_name('Transitions'):
            TransitionSprite((obj.x, obj.y),(obj.width,obj.height), (obj.properties['target'], obj.properties['pos']),self.transition_sprites)

        #ajout des patches Waremon
        for obj in tmx_map.get_layer_by_name('Herbe_ware'):
            Waremon_patch_Sprite((obj.x, obj.y), obj.image, self.all_sprites)

        #ajout des collisions pour les bordures
        for obj in tmx_map.get_layer_by_name('Collisions'):
            BorderSprite((obj.x, obj.y), pygame.Surface((obj.width, obj.height)), self.collision_sprites)

        #création des entités (joueur et PNJ)
        for obj in tmx_map.get_layer_by_name('Entités'):
            if obj.name == 'Player':
                if obj.properties['pos']  == player_start_pos:
                    self.player = Player(
                        pos = (obj.x, obj.y),
                        frames = self.overwolrd_frames['characters']['Player'],
                        groups = self.all_sprites,
                        regard = obj.properties['direction'],
                        collision_sprites = self.collision_sprites
                    )
            else:
                Dresseur(
                    pos=(obj.x, obj.y),
                    frames=self.overwolrd_frames['characters'][obj.properties['graphic']],
                    groups=( self.all_sprites, self.collision_sprites,self.character_sprites),
                    regard = obj.properties['direction']
                )

    def input(self):#gère les entrées clavier du joueur, notamment l'interaction avec les persos
        keys = pygame.key.get_just_pressed()
        if keys[pygame.K_SPACE]:
            for character in self.character_sprites:
                if check_connection(100, self.player, character):
                    self.player.block()
                    #perso qui se regarde pendant dialogues
                    #character.change_facing_direction(self.player.rect.center)
                    #crée les dialogue
                    print('dialog')

    #transition systeme
    def transition_check(self):#verifie si le joueur entre dans une zone de transition
        sprites = [sprite for sprite in self.transition_sprites if sprite.rect.colliderect(self.player.hitbox)]
        if sprites:
            self.player.block()
            self.transition_target = sprites[0].target
            self.tint_mode = 'tint'

    def tint_screen(self,dt): #gère l'effet de fondu de l'écran lors des transitions.
        if self.tint_mode == 'untint':
            self.tint_progress -= self.tint_speed * dt
        if self.tint_mode == 'tint' :
            self.tint_progress += self.tint_speed * dt
            if self.tint_progress >= 255:
                #charger la nouvelle carte lorsque le fondu est terminé
                self.setup(self.tmx_maps[self.transition_target[0]], self.transition_target[1])
                self.tint_mode = 'untint'
                self.transition_target = None

        #limiter la progression du fondu entre 0 et 255
        self.tint_progress = max(0, min(self.tint_progress, 255))
        self.tint_surf.set_alpha(self.tint_progress)
        self.display_surface.blit(self.tint_surf,(0,0))


    def run(self): #boucle principale du jeu
        while True:
            #dessin des hitboxes de collision (debugging)
            for sprite in self.collision_sprites:
                pygame.draw.rect(self.display_surface, (255, 0, 0), sprite.hitbox, 2)
            dt = self.clock.tick() / 1000 #calcul du temps écoulé
            #print(f"Available maps: {list(self.tmx_maps.keys())}") #debugging des cartes disponibles
            #event boucle
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()


            #game logique
            self.input()
            self.transition_check()
            self.all_sprites.update(dt)
            #affichage des éléments du jeu
            self.display_surface.fill('Black')
            self.all_sprites.draw(self.player.rect.center)

            self.tint_screen(dt)
            pygame.display.update()

if __name__ == '__main__':
    game = Game()
    game.run()