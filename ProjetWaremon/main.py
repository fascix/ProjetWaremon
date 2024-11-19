import pygame
import pytmx

# Initialisation de Pygame
pygame.init()

# Configuration de l'écran
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
clock = pygame.time.Clock()

# Chargement de la map
MAP_PATH = "/Users/lucaspavone/PycharmProjects/ProjetWaremon/MAP/map1 11.14.04.tmx"
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