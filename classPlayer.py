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

    # Méthode qui permet de faire bouger le joueur a gauche :
    def moveLef(self):
        # Si le joueur est en collision avec le cercueille :
        if not self.game.check_collision(self, self.game.all_objects):
            self.rect.x -= self.velocity
            self.marche.play()

    # Méthode qui permet de faire bouger le joueur en haut :
    def moveUp(self):
        # Si le joueur est en collision avec le cercueille :
        if not self.game.check_collision(self, self.game.all_objects):
            self.rect.y -= self.velocity
            self.marche.play()

    # Méthode qui permet de faire bouger le joueur en bas:
    def moveDown(self):
        # Si le joueur est en collision avec le cercueille :
        if not self.game.check_collision(self, self.game.all_objects):
            self.rect.y += self.velocity
            self.marche.play()