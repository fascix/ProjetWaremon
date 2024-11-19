import pygame
from map import Map
from screen import Screen


class Game:
    def __init__(self):
        self.running = True
        self.screen = Screen()
        self.map = Map(self.screen)

    def run(self):
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                    print("Fermeture du jeu.")
            self.map.update()
            self.screen.update()