from settings import *
from os.path import join
from os import walk
from pytmx.util_pygame import load_pygame

# Fonction pour importer une image depuis un chemin donné
def import_image(*path, alpha = True, format = 'png'):
	#charge une image avec ou sans transparence depuis un chemin donné
	full_path = join(*path) + f'.{format}'
	surf = pygame.image.load(full_path).convert_alpha() if alpha else pygame.image.load(full_path).convert()
	return surf

#fonction pour importer toutes les images d'un dossier
def import_folder(*path):
	#charge toutes les images d'unn dossier, triées par leur nom
	frames = []
	for folder_path, sub_folders, image_names in walk(join(*path)):
		for image_name in sorted(image_names, key = lambda name: int(name.split('.')[0])):
			full_path = join(folder_path, image_name)
			surf = pygame.image.load(full_path).convert_alpha()
			frames.append(surf)
	return frames

#fonction pour importer un dossier et créer un dictionnaire des images
def import_folder_dict(*path):
	#charge toutes les images d'un dossier dans un dictionnaire, avec les noms des fichiers comme clés
	frames = {}
	for folder_path, sub_folders, image_names in walk(join(*path)):
		for image_name in image_names:
			full_path = join(folder_path, image_name)
			surf = pygame.image.load(full_path).convert_alpha()
			frames[image_name.split('.')[0]] = surf
	return frames

#fonction pour importer les sous-dossiers
def import_sub_folders(*path):
	#charge les images contenues dans les sous-dossiers, organisées en dictionnaire.
	frames = {}
	for _, sub_folders, __ in walk(join(*path)):
		if sub_folders:
			for sub_folder in sub_folders:
				frames[sub_folder] = import_folder(*path, sub_folder)
	return frames

#fonction pour découper une sprite-sheet en tuiles
def import_tilemap(cols, rows, *path):
	#decoupe une image en une grille de tuiles
	frames = {}
	surf = import_image(*path)
	cell_width, cell_height = surf.get_width() / cols, surf.get_height() / rows
	for col in range(cols):
		for row in range(rows):
			cutout_rect = pygame.Rect(col * cell_width, row * cell_height,cell_width,cell_height)
			cutout_surf = pygame.Surface((cell_width, cell_height))
			cutout_surf.fill('green') #definir une couleur de fond pour le découpage
			cutout_surf.set_colorkey('green') #rendre le fond transparent
			cutout_surf.blit(surf, (0,0), cutout_rect)
			frames[(col, row)] = cutout_surf
	return frames

#fonction pour importer une sprite-sheet pour un personnage
def character_importer(rows, cols, *path, image_name):
	#découpe une sprite-sheet de personnage en animation par direction
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

def tmx_importer(*path):
	tmx_dict = {}
	for folder_path, sub_folders, file_names in walk(join(*path)):
		for file in file_names:
			tmx_dict[file.split('.')[0]] = load_pygame(join(folder_path, file))
	return tmx_dict


#fonction jeu
def check_connection(radius, entité, cible, tolerance = 30):
	relation = vector(cible.rect.center) - vector(entité.rect.center)
	if relation.length() < radius:
		if entité.regard == 'left' and relation.x <0 and abs(relation.y) < tolerance or\
			entité.regard == 'right' and relation.x > 0 and abs(relation.y) < tolerance or \
				entité.regard == 'up' and relation.y < 0 and abs(relation.x) < tolerance or \
				entité.regard == 'down' and relation.y > 0 and abs(relation.x) < tolerance:
				return True

def play_music(filepath, volume=0.5):
    """
    Charge et joue une musique en boucle.

    :param filepath: Le chemin vers le fichier audio (format supporté par pygame).
    :param volume: Volume de la musique (entre 0.0 et 1.0).
    """
    pygame.mixer.init()  # Initialisation du mixer
    pygame.mixer.music.load(filepath)  # Charger le fichier audio
    pygame.mixer.music.set_volume(volume)  # Régler le volume
    pygame.mixer.music.play(loops=-1)  # Lecture en boucle infinie

def pause_music():
    """Met en pause la musique actuelle."""
    pygame.mixer.music.pause()

def resume_music():
    """Reprend la musique après une pause."""
    pygame.mixer.music.unpause()

def stop_music():
    """Arrête complètement la musique."""
    pygame.mixer.music.stop()
