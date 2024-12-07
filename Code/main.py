from Code.sprites import Waremon_patch_Sprite
from settings import *
from pytmx.util_pygame import load_pygame
from os.path import join
from sprites import *
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
        self.collision_sprites = pygame.sprite.Group()

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
        # map 3 :
        for layer in ['Terrain', 'Terrain haut']:
            for x, y, surf in tmx_map.get_layer_by_name(layer).tiles():
                Sprite((x * TILE_SIZE, y * TILE_SIZE), surf, self.all_sprites, WORLD_LAYERS['bg'])

        for obj in tmx_map.get_layer_by_name('water'):
            for x in range(int(obj.x), int(obj.x+obj.width), TILE_SIZE):
                for y in range(int(obj.y), int(obj.y+obj.height), TILE_SIZE):
                    Animation((x,y), self.overwolrd_frames['water'], self.all_sprites, WORLD_LAYERS['water'])

        for obj in tmx_map.get_layer_by_name('Côtes'):
            terrain = obj.properties['terrain']
            side = obj.properties['side']
            Animation((obj.x, obj.y),self.overwolrd_frames['cote'][terrain][side], self.all_sprites, WORLD_LAYERS['bg'])

        for obj in tmx_map.get_layer_by_name('Objets'):
            CollidableSprite((obj.x, obj.y), obj.image, (self.all_sprites, self.collision_sprites))

        for obj in tmx_map.get_layer_by_name('Herbe_ware'):
            Waremon_patch_Sprite((obj.x, obj.y), obj.image, self.all_sprites)

        for obj in tmx_map.get_layer_by_name('Collisions'):
            BorderSprite((obj.x, obj.y), pygame.Surface((obj.width, obj.height)), self.collision_sprites)

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
                    groups=( self.all_sprites, self.collision_sprites),
                    regard = obj.properties['direction']
                )



    def run(self):
        while True:
            for sprite in self.collision_sprites:
                pygame.draw.rect(self.display_surface, (255, 0, 0), sprite.hitbox, 2)
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