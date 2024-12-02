from Code.sprites import Animation
from settings import *
from pytmx.util_pygame import load_pygame
from os.path import join
from sprites import Sprite, Animation
from entities import *
from group import AllSprites
from support import *

class Game:
    def __init__(self):
        pygame.init()
        self.display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
        pygame.display.set_caption('Waremon')
        self.clock = pygame.time.Clock()

        #groupes :
        self.all_sprites = AllSprites()

        self.import_assets()
        self.setup(self.tmx_maps['map3'], 'house')

    def import_assets(self):
        self.tmx_maps = {'map3': load_pygame(join('..', 'data', 'maps', 'map3.tmx'))}

        self.overwolrd_frames = {
            'water': import_folder(join('..', 'graphics', 'tilesets', 'water')),
            'cote' : cote_importer(24,12,join('..', 'graphics', 'tilesets', 'cote')),
            'characters': all_character_import('..', 'graphics', 'characters')
        }


    # noinspection PyTypeChecker
    def setup(self, tmx_map, player_start_pos):
        #map1 :
        '''
        for x,y, surf in tmx_map.get_layer_by_name('Herbe1').tiles():
            Sprite((x * TILE_SIZE, y * TILE_SIZE), surf, self.all_sprites)
        for x,y, surf in tmx_map.get_layer_by_name('Sable1').tiles():
            Sprite((x * TILE_SIZE, y * TILE_SIZE), surf, self.all_sprites)
        for x,y, surf in tmx_map.get_layer_by_name('Chemin1').tiles():
            Sprite((x * TILE_SIZE, y * TILE_SIZE), surf, self.all_sprites)
        for x,y, surf in tmx_map.get_layer_by_name('Hautes herbe1').tiles():
            Sprite((x * TILE_SIZE, y * TILE_SIZE), surf, self.all_sprites)
        for x,y, surf in tmx_map.get_layer_by_name('Eau1').tiles():
            Sprite((x * TILE_SIZE, y * TILE_SIZE), surf, self.all_sprites)
        for x,y, surf in tmx_map.get_layer_by_name('Pont2').tiles():
            Sprite((x * TILE_SIZE, y * TILE_SIZE), surf, self.all_sprites)
        for x,y, surf in tmx_map.get_layer_by_name("ilot2/caillou sur l'eau").tiles():
            Sprite((x * TILE_SIZE, y * TILE_SIZE), surf, self.all_sprites)
        for x,y, surf in tmx_map.get_layer_by_name('Milieu arbre2').tiles():
            Sprite((x * TILE_SIZE, y * TILE_SIZE), surf, self.all_sprites)
        for x,y, surf in tmx_map.get_layer_by_name('caillou_mer2').tiles():
            Sprite((x * TILE_SIZE, y * TILE_SIZE), surf, self.all_sprites)
        for x,y, surf in tmx_map.get_layer_by_name('Montagne-etage1_2').tiles():
            Sprite((x * TILE_SIZE, y * TILE_SIZE), surf, self.all_sprites)
        for x,y, surf in tmx_map.get_layer_by_name('Montagne-etage2_3').tiles():
            Sprite((x * TILE_SIZE, y * TILE_SIZE), surf, self.all_sprites)
        for x,y, surf in tmx_map.get_layer_by_name('Buisson_montagne3').tiles():
            Sprite((x * TILE_SIZE, y * TILE_SIZE), surf, self.all_sprites)
        for x,y, surf in tmx_map.get_layer_by_name('Bâteau3').tiles():
            Sprite((x * TILE_SIZE, y * TILE_SIZE), surf, self.all_sprites)
        for x,y, surf in tmx_map.get_layer_by_name('Haut arbre3').tiles():
            Sprite((x * TILE_SIZE, y * TILE_SIZE), surf, self.all_sprites)
        for x,y, surf in tmx_map.get_layer_by_name('Maison3').tiles():
            Sprite((x * TILE_SIZE, y * TILE_SIZE), surf, self.all_sprites)
        for x,y, surf in tmx_map.get_layer_by_name('Montagne-etage3_4').tiles():
            Sprite((x * TILE_SIZE, y * TILE_SIZE), surf, self.all_sprites)
        for x,y, surf in tmx_map.get_layer_by_name('Escaliers/Caillou_montagne4').tiles():
            Sprite((x * TILE_SIZE, y * TILE_SIZE), surf, self.all_sprites)
        for x,y, surf in tmx_map.get_layer_by_name('Arbre_montagne4').tiles():
            Sprite((x * TILE_SIZE, y * TILE_SIZE), surf, self.all_sprites)
        '''

        #map2 :
        '''
        for x, y, surf in tmx_map.get_layer_by_name('Terrain').tiles():
            Sprite((x * TILE_SIZE, y * TILE_SIZE), surf, self.all_sprites)
        for x, y, surf in tmx_map.get_layer_by_name('Terrain haut').tiles():
            Sprite((x * TILE_SIZE, y * TILE_SIZE), surf, self.all_sprites)
        for x, y, surf in tmx_map.get_layer_by_name('Terrain haut 2').tiles():
            Sprite((x * TILE_SIZE, y * TILE_SIZE), surf, self.all_sprites)

        for obj in tmx_map.get_layer_by_name('Objets'):
            Sprite((obj.x, obj.y), obj.image, self.all_sprites)

        for obj in tmx_map.get_layer_by_name('Entités'):
            if obj.name == 'Player' and 'pos' in obj.properties and obj.properties['pos'] == player_start_pos:
                self.player = Joueur((obj.x, obj.y), self.all_sprites)
        '''

        #map 3 :
        for layer in ['Terrain', 'Terrain haut']:
            for x, y, surf in tmx_map.get_layer_by_name(layer).tiles():
                Sprite((x * TILE_SIZE, y * TILE_SIZE), surf, self.all_sprites)

        for obj in tmx_map.get_layer_by_name('Objets'):
            Sprite((obj.x, obj.y), obj.image, self.all_sprites)

        for obj in tmx_map.get_layer_by_name('Entités'):
            if obj.name == 'Player':
                if obj.properties['pos']  == player_start_pos:
                    self.player = Player(
                        pos = (obj.x, obj.y),
                        frames = self.overwolrd_frames['characters']['playerbis'],
                        groups = self.all_sprites)
                

        for obj in tmx_map.get_layer_by_name('water'):
            for x in range(int(obj.x), int(obj.x+obj.width), TILE_SIZE):
                for y in range(int(obj.y), int(obj.y+obj.height), TILE_SIZE):
                    Animation((x,y), self.overwolrd_frames['water'], self.all_sprites)

        for obj in tmx_map.get_layer_by_name('Côtes'):
            terrain = obj.properties['terrain']
            side = obj.properties['side']
            Animation((obj.x, obj.y),self.overwolrd_frames['cote'][terrain][side], self.all_sprites)

    def run(self):
        while True:
            dt = self.clock.tick() / 1000
            #event boucle
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()

            #game logique
            self.all_sprites.update(dt)
            self.display_surface.fill('Black')
            self.all_sprites.draw(self.player.rect.center)
            pygame.display.update()

if __name__ == '__main__':
    game = Game()
    game.run()