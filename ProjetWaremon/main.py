import pygame
import pytmx
import os

# Initialisation de Pygame
pygame.init()

# Configuration de l'écran
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
clock = pygame.time.Clock()

# Obtenir le répertoire du fichier Python actuel (répertoire racine de ton projet)
base_dir = os.path.dirname(__file__)

# Chemin relatif vers la carte et les ressources
MAP_PATH = os.path.join(base_dir, "MAP", "map1 11.14.04.tmx")
TILESET_PATH = os.path.join(base_dir, "MAP", "tileset_by_evolina_d36bih3.png")

# Chargement de la map
tmx_data = pytmx.load_pygame(MAP_PATH, pixelalpha=True)

def draw_map(screen, tmx_data):
    """Affiche la map sur l'écran."""
    for layer in tmx_data.visible_layers:
        if isinstance(layer, pytmx.TiledTileLayer):
            for x, y, gid in layer:
                tile = tmx_data.get_tile_image_by_gid(gid)
                if tile:
                    screen.blit(tile, (x * tmx_data.tilewidth, y * tmx_data.tileheight))

# Boucle principale
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Dessin de la map
    screen.fill((0, 0, 0))  # Nettoyage de l'écran
    draw_map(screen, tmx_data)
    pygame.display.flip()
    clock.tick(60)

pygame.quit()