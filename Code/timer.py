from pygame.time import get_ticks # Importation de la fonction get_ticks de Pygame qui retourne le nombre de millisecondes écoulées depuis le lancement du jeu

# Classe Timer permettant de gérer des minuteries (timers) avec des durées et des actions répétitives
class Timer:
	# Initialisation de la minuterie avec des paramètres de durée, répétition, démarrage automatique et fonction à exécuter
	def __init__(self, duration, repeat = False, autostart = False, func = None):
		self.duration = duration # Durée du timer en millisecondes
		self.start_time = 0 # Temps de début, initialisé à 0
		self.active = False # Le timer n'est pas actif au départ
		self.repeat = repeat # Si True, le timer redémarrera une fois expiré
		self.func = func # Fonction optionnelle à exécuter lorsque le timer expire
		if autostart: # Si autostart est True, le timer démarre immédiatement
			self.activate()

	# Activation de la minuterie : elle devient active et on enregistre l'heure de départ
	def activate(self):
		self.active = True # Le timer est maintenant actif
		self.start_time = get_ticks() # Enregistre le temps actuel (en millisecondes) comme le temps de début du timer

	# Désactivation de la minuterie : elle devient inactive et le temps de début est réinitialisé
	def deactivate(self):
		self.active = False # Le timer est désactivé
		self.start_time = 0 # Réinitialisation du temps de départ
		if self.repeat: # Si la minuterie est configurée pour se répéter, elle est réactivée
			self.activate()

	# Mise à jour de l'état de la minuterie à chaque frame
	def update(self):
		if self.active: # Si le timer est actif
			current_time = get_ticks()  # Récupère le temps actuel en millisecondes
			if current_time - self.start_time >= self.duration: # Si le temps écoulé depuis le début dépasse la durée du timer
				if self.func:# Si une fonction est définie pour être exécutée
					self.func() # Appelle la fonction
				self.deactivate() # Désactive le timer après avoir exécuté la fonction