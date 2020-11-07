import pygame
from pygame import mixer

# Création de la classe Player :
class Player(pygame.sprite.Sprite):

    def __init__(self, game):
        super().__init__()
        self.game = game
        self._health = 100
        self._maxHealth = 100
        self.attack = 10
        self.velocity = 2
        self.marche = mixer.Sound('Asset/Bruitages/marcheParquet.wav')
        self.image = pygame.image.load('Asset/AidenLoaw1.xcf').convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.x = 540
        self.rect.y = 300

    # Méthode qui permet de faire bouger le joueur a droite :
    def moveRigth(self):
        # Si le joueur est en collision avec le cercueille :
        if not self.game.check_collision(self, self.game.all_objects):
            self.rect.x += self.velocity
            self.marche.play()
        else:
            self.rect.x -= self.velocity

    # Méthode qui permet de faire bouger le joueur a gauche :
    def moveLef(self):
        # Si le joueur est en collision avec le cercueille :
        if not self.game.check_collision(self, self.game.all_objects):
            self.rect.x -= self.velocity
            self.marche.play()
        '''else:
            self.rect.x += self.velocity'''

    # Méthode qui permet de faire bouger le joueur en haut :
    def moveUp(self):
        # Si le joueur est en collision avec le cercueille :
        if not self.game.check_collision(self, self.game.all_objects):
            self.rect.y -= self.velocity
            self.marche.play()
        else:
            self.rect.y += self.velocity

    # Méthode qui permet de faire bouger le joueur en bas:
    def moveDown(self):
        # Si le joueur est en collision avec le cercueille :
        if not self.game.check_collision(self, self.game.all_objects):
            self.rect.y += self.velocity
            self.marche.play()
        else:
            self.rect.y -= self.velocity

        # Création d'une méthode qui permet d'afficher la barre de vie du joueur :
    def update_health_bar(self, surface):
        # Couleur pour jauge de vie (vert) :
        bar_color = (111, 210, 46)
        # Couleur pour l'arrière plan de la jauge :
        back_bar_color = (60, 63, 60)
        # Position de la jauge de vie ainsi sa largeur et son épesseur :
        bar_position = [self.rect.x - 20, self.rect.y - 10, self._health, 5]
        # Position de l'arrière plan de notre jauge de vie :
        back_bar_position = [self.rect.x - 20, self.rect.y - 10, self._maxHealth, 5]
        # Création barre de vie :
        pygame.draw.rect(surface, back_bar_color, back_bar_position)
        pygame.draw.rect(surface, bar_color, bar_position)