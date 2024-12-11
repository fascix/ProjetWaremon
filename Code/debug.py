import pygame #importation de pygame
pygame.init() #initialisation de pygame pour pouvoir l'utiliser
font = pygame.font.Font(None,30) #création d'un objet de police(font) avec une taille de 30, sans police spécifique

def debug(info,y = 10, x = 10):
	#fonction qui affiche un texte de débogage sur la surface d'affichage
	display_surface = pygame.display.get_surface() #récupere la surface d'affichage actuelle
	debug_surf = font.render(str(info),True,'White') #crée une surface contenant le texte de débogage, en blanc
	debug_rect = debug_surf.get_rect(topleft = (x,y)) # crée un rectangle autour du texte pour la positionner à (x,y)
	pygame.draw.rect(display_surface,'Black',debug_rect) #dessine un rectangle noir autour du texte pour le rendre lisibles dans tout les cas
	display_surface.blit(debug_surf,debug_rect) #affiche la surface contenant le texte sur l'ecran
