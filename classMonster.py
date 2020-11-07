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

    # Création dégats du monstre :
    def damage(self, amount):
        # Infliger les dégats:
        self.health -= amount

    # Création d'une méthode qui permet d'afficher la barre de vie du monstre :
    def update_health_bar(self, surface):
        # Couleur pour jauge de vie (vert) :
        bar_color = (111, 210, 46)
        # Couleur pour l'arrière plan de la jauge :
        back_bar_color = (60, 63, 60)
        # Position de la jauge de vie ainsi sa largeur et son épesseur :
        bar_position = [self.rect.x - 20, self.rect.y - 10, self.health, 5]
        # Position de l'arrière plan de notre jauge de vie :
        back_bar_position = [self.rect.x - 20, self.rect.y - 10, self.max_health, 5]
        # Création barre de vie :
        pygame.draw.rect(surface, back_bar_color, back_bar_position)
        pygame.draw.rect(surface, bar_color, bar_position)

    # Création d'une méthode pour faire avancer le joueur :
    def foward(self):
        self.rect.x -= self.velocity