import pygame.sprite #module pygame pour gérer les sprites

from settings import *  #importation des paramètres globaux du jeu

#classe de base pour toutes les entités interactives du jeu
class Entity(pygame.sprite.Sprite):
    def __init__(self, pos, frames, groups, regard):
        #initialise une entité génrérique
        super().__init__(groups) #ajoute l'entité dans le monde
        self.z = WORLD_LAYERS['main'] #niveau de profondeur pour le tri d'affichage

        #graphismes
        self.frames_indice, self.frames = 0, frames #animation(index actuel et frames disponibles)
        self.regard = regard #direction actuelle de l'entité

        # Mouvemenent :
        self.direction = vector() #direction de déplacement(vector2)
        self.speed = 500 #vitesse de déplacement
        self.blocked = False #indique si l'entité est bloquée (imobilisée)

        # configuration du sprite
        self.image = self.frames['down'][self.frames_indice] #image initiale (face vers le bas)
        self.rect = self.image.get_frect(center = pos) # rectangle de position basé sur l'image
        #ajuste la hitbox pour correspondre à la taille réelle de l'entité
        self.hitbox = self.rect.inflate(-self.rect.width / 2, -60)
        self.y_sort = self.rect.centery #utilisé pour trier les entités par profondeur

    def animation(self,dt):
        #anime l'entité en fonction de temps écoulé
        self.frames_indice += ANIMATION_SPEED * dt #avance dans l'animation
        #definit l'image actuelle en fonction de l'état et de l'animation en cours
        self.image = self.frames[self.get_etat()][int(self.frames_indice % len(self.frames[self.get_etat()]))]

    def get_etat(self):
        # Déterminez l'état actuel de l'entité en fonction de son mouvement et de sa direction
        #determine si l'entité est en mouvement
        moving = bool(self.direction)

        # Définissez la direction basée sur le mouvement
        if moving:
            if self.direction.x > 0:
                self.regard = 'right'
            elif self.direction.x < 0:
                self.regard = 'left'
            elif self.direction.y > 0:
                self.regard = 'down'
            elif self.direction.y < 0:
                self.regard = 'up'

        # Genere l'etat actuel
        etat = f"{self.regard}{'' if moving else '_idle'}"

        # Vérifiez si l'état est valide
        if etat not in self.frames:
            print(f"Warning: Invalid state '{etat}' for character.") #avertissement si l'état est invalide
            return f"{self.regard}_idle"  # Retournez un état par défaut valide

        return etat

    def block(self):
        #bloque l'entité, l'empêchant de bouger
        self.blocked = True
        self.direction = vector(0,0) #rénitialise la direction

    def unblock(self):
        #débloque l'entité, lui permetttant de bouger à nouveau
        self.blocked = False

#classe représentant un drésseur, nune entité spécialisée
class Dresseur(Entity):
    def __init__(self, pos, frames, groups, regard):
        #initialise un dresseur
        super().__init__(pos, frames,groups, regard)

#classe représentant le joueur  une entité CONTROLABLE
class Player(Entity):
    def __init__(self, pos, frames, groups, regard, collision_sprites):
        #initialise le joueur
        super().__init__(pos, frames, groups, regard)
        self.collision_sprites = collision_sprites #liste des objets avec lesquels le joueur peut entrer en collision

    def input(self):
        #gere les entrées utilisateur pour définir la direction de déplacement
        keys = pygame.key.get_pressed() #verifie les touches pressées
        input_vector = vector() #direction basée sur les entrées
        if keys[pygame.K_UP]:
            input_vector.y -= 1 #haut
        if keys[pygame.K_DOWN]:
            input_vector.y += 1 # bas
        if keys[pygame.K_LEFT]:
            input_vector.x -= 1 # gauche
        if keys[pygame.K_RIGHT]:
            input_vector.x += 1 #droite
        #normalise le vecteur de direction pour éviter les déplacements irréguliers
        self.direction = input_vector.normalize() if input_vector else input_vector


    def mouvement(self, dt):
        #gère le déplacement du joueur en prenant en compte le temps et les collisions
        #deplace horizontalement
        self.rect.centerx += self.direction.x * self.speed * dt
        self.hitbox.centerx = self.rect.centerx
        self.collisions('horizontale')

        #deplace verticalement
        self.rect.centery += self.direction.y * self.speed * dt
        self.hitbox.centery = self.rect.centery
        self.collisions('verticale')

    def collisions(self, axis):
        #gère les collisions entre le joueur et les objets de collisions
        for sprite in self.collision_sprites:
            if sprite.hitbox.colliderect(self.hitbox): #detecte une collision
                if axis == 'horizontale':
                    #corrige la position selon la direction horizontale
                    if self.direction.x > 0:  # Déplacement à droite
                        self.hitbox.right = sprite.hitbox.left
                    if self.direction.x < 0:  # Déplacement à gauche
                        self.hitbox.left = sprite.hitbox.right
                    self.rect.centerx = self.hitbox.centerx  # Synchronisation
                else:
                    #corrige la position selon la direction verticale
                    if self.direction.y > 0:  # Déplacement vers le bas
                        self.hitbox.bottom = sprite.hitbox.top
                    if self.direction.y < 0:  # Déplacement vers le haut
                        self.hitbox.top = sprite.hitbox.bottom
                    self.rect.centery = self.hitbox.centery  # Synchronisation

    def update(self, dt):
        #met a jour l'état du joueur à chaque frame
        self.y_sort = self.rect.centery #mise a jour du tri
        if not self.blocked: #si le joueur n'est pas bloqué
            self.input() #gestion des entrées
            self.mouvement(dt) #gestion des mouvements
        self.animation(dt) #mise a jour de l'animation
