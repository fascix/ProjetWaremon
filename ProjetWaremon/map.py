import os
import pyscroll
import pytmx
from screen import Screen


class Map:
    def __init__(self, screen: Screen):
        self.screen = screen
        self.tmx_data = None
        self.map_layer = None
        self.group = None

        # Charge la carte initiale
        self.switch_map("map1 11.14.04")

    def switch_map(self, gamemap: str):
        try:
            # Chemin relatif vers le fichier de la carte
            map_path = os.path.join(os.path.dirname(__file__), "MAP", f"{gamemap}.tmx")
            print(f"Chemin de la carte : {map_path}")

            # Vérifie si le fichier existe
            if not os.path.exists(map_path):
                raise FileNotFoundError(f"Le fichier {map_path} est introuvable.")

            # Charge les données de la carte
            self.tmx_data = pytmx.load_pygame(map_path)
            map_data = pyscroll.data.TiledMapData(self.tmx_data)

            # Configure le rendu de la carte
            self.map_layer = pyscroll.BufferedRenderer(map_data, self.screen.get_size())
            self.group = pyscroll.PyscrollGroup(map_layer=self.map_layer, default_layer=7)
            print(f"Carte '{gamemap}' chargée avec succès.")
        except FileNotFoundError as e:
            print(f"Erreur : {e}")
        except Exception as e:
            print(f"Erreur inattendue : {e}")

    def update(self):
        if self.group:
            self.group.draw(self.screen.get_display())
        else:
            print("Aucun groupe de rendu n'est chargé.")