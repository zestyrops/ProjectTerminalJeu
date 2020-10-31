import pygame

# Création de la classe monstre :
class Monster(pygame.sprite.Sprite):

    def __init__(self):
        super().__init__()
        self.health = 100
        self.max_health = 100
        self.attack = 5
        self.velocity = 2
        self.image = pygame.image.load('Asset/Pers_Face_Static1.png')
        self.rect = self.image.get_rect()
        self.rect.x = 1000
        self.rect.y = 500

    # Création d'une méthode pour faire avancer le joueur :
    def foward(self):
        self.rect.x -= self.velocity