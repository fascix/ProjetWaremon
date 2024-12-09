from Code.support import character_importer
from settings import *

class DialoguesArbre:
    def __init__(self, character, player, all_sprites, font):
        self.player = player
        self.character = character
        self.font = font
        self.all_sprites = all_sprites
