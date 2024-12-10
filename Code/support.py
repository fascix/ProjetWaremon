from settings import *
from os.path import join
from os import walk
from pytmx.util_pygame import load_pygame

# imports 
def import_image(*path, alpha = True, format = 'png'):
	full_path = join(*path) + f'.{format}'
	surf = pygame.image.load(full_path).convert_alpha() if alpha else pygame.image.load(full_path).convert()
	return surf

def import_folder(*path):
	frames = []
	for folder_path, sub_folders, image_names in walk(join(*path)):
		for image_name in sorted(image_names, key = lambda name: int(name.split('.')[0])):
			full_path = join(folder_path, image_name)
			surf = pygame.image.load(full_path).convert_alpha()
			frames.append(surf)
	return frames

def import_folder_dict(*path):
	frames = {}
	for folder_path, sub_folders, image_names in walk(join(*path)):
		for image_name in image_names:
			full_path = join(folder_path, image_name)
			surf = pygame.image.load(full_path).convert_alpha()
			frames[image_name.split('.')[0]] = surf
	return frames

def import_sub_folders(*path):
	frames = {}
	for _, sub_folders, __ in walk(join(*path)):
		if sub_folders:
			for sub_folder in sub_folders:
				frames[sub_folder] = import_folder(*path, sub_folder)
	return frames

def import_tilemap(cols, rows, *path):
	frames = {}
	surf = import_image(*path)
	cell_width, cell_height = surf.get_width() / cols, surf.get_height() / rows
	for col in range(cols):
		for row in range(rows):
			cutout_rect = pygame.Rect(col * cell_width, row * cell_height,cell_width,cell_height)
			cutout_surf = pygame.Surface((cell_width, cell_height))
			cutout_surf.fill('green')
			cutout_surf.set_colorkey('green')
			cutout_surf.blit(surf, (0,0), cutout_rect)
			frames[(col, row)] = cutout_surf
	return frames

def character_importer(rows, cols, *path, image_name):
    # Charger la sprite-sheet
    full_path = join(*path, f"{image_name}")
    sprite_sheet = pygame.image.load(full_path).convert_alpha()
    width, height = sprite_sheet.get_width() // cols, sprite_sheet.get_height() // rows

    # Définir les directions
    directions = ['down', 'left', 'right', 'up']  # Ordre des directions dans la sprite-sheet
    frames = {}

    # Découper les frames et ajouter les frames "idle"
    for row, direction in enumerate(directions):
        frames[direction] = []
        for col in range(cols):
            frame = sprite_sheet.subsurface((col * width, row * height, width, height))
            frames[direction].append(frame)

        # Ajouter le frame "idle" correspondant
        frames[f"{direction}_idle"] = [frames[direction][0]]

    return frames


def all_character_import(*path):
    new_dict = {}
    for _, __, image_names in walk(join(*path)):
        for image in image_names:
            if image.endswith(".png"):  # Vérifie que c'est une image PNG
                image_name = image.split('.')[0]
                # Appel de la fonction character_importer
                new_dict[image_name] = character_importer(4, 4, *path, image_name=image)
    return new_dict

def cote_importer(cols, rows, *path):
	frame_dict = import_tilemap(cols, rows, *path)
	new_dict = {}
	terrains = ['herbe', 'i_herbe', 'i_sable', 'sable', 'pierre', 'i_pierre', 'glace', 'i_glace' ]
	sides = {
		'topleft': (0,0), 'top': (1,0), 'topright': (2,0),
		'left': (0, 1), 'right': (2,1), 'bottomleft': (0,2),
		'bottom': (1, 2), 'bottomright': (2,2)
	}
	for index, terrain in enumerate(terrains):
		new_dict[terrain] = {}
		for key, pos in sides.items():
			new_dict[terrain][key] = [frame_dict[(pos[0] + index * 3, pos[1]+ row)] for row in range(0, rows, 3)]
	return new_dict

#fonction jeu
def check_connection(radius, entité, cible, tolerance = 30):
	relation = vector(cible.rect.center) - vector(entité.rect.center)
	if relation.length() < radius:
		if entité.regard == 'left' and relation.x <0 and abs(relation.y) < tolerance or\
			entité.regard == 'right' and relation.x > 0 and abs(relation.y) < tolerance or \
				entité.regard == 'up' and relation.y < 0 and abs(relation.x) < tolerance or \
				entité.regard == 'down' and relation.y > 0 and abs(relation.x) < tolerance:
				return True