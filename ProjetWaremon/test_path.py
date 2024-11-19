import os

# Test du fichier .tmx
map_path = os.path.join(os.path.dirname(__file__), "MAP", "map1 11.14.04.tmx")
if os.path.exists(map_path):
    print(f"Fichier trouvé : {map_path}")
else:
    print(f"Fichier introuvable : {map_path}")

# Test d'une image de tileset
tileset_path = os.path.join(os.path.dirname(__file__), "Tileset", "4g tileset_interieur.png")
if os.path.exists(tileset_path):
    print(f"Tileset trouvé : {tileset_path}")
else:
    print(f"Tileset introuvable : {tileset_path}")