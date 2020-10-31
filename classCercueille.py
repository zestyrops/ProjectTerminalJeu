import pygame

# Création d'une classe cercueille :
class Cercueille(pygame.sprite.Sprite):

    def __init__(self):
        super().__init__()
        self.image = pygame.image.load('Asset/Ancien Cercueil2.xcf')
        self.rect = self.image.get_rect()
        # Placement au milieu de l'écran :
        self.rect.x = 540
        self.rect.y = 378