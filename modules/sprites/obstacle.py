import random
import pygame


class Cactus(pygame.sprite.Sprite):
    def __init__(self, imagepaths, position=(1200, 545), sizes=[(204, 204), (153, 114)], **kwargs):
        pygame.sprite.Sprite.__init__(self)

        self.images = []
        image = pygame.image.load(imagepaths[0])
        for i in range(3):
            self.images.append(pygame.transform.scale(image.subsurface((i * 51, 0), (51, 51)), sizes[0]))
        image = pygame.image.load(imagepaths[1])
        for i in range(2):
            self.images.append(pygame.transform.scale(image.subsurface((i * 51, 0), (51, 38)), sizes[1]))
        self.image = random.choice(self.images)
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.bottom = position
        self.mask = pygame.mask.from_surface(self.image)

        self.speed = -10

    def draw(self, screen):
        screen.blit(self.image, self.rect)

    def update(self):
        self.rect = self.rect.move([self.speed, 0])
        if self.rect.right < 0:
            self.kill()


class Ptera(pygame.sprite.Sprite):
    # def __init__(self, imagepath, position, size=(46, 40), **kwargs):
    def __init__(self, imagepath, position, size=(138, 126), **kwargs):
        pygame.sprite.Sprite.__init__(self)

        self.images = []
        image = pygame.image.load(imagepath)
        for i in range(2):
            self.images.append(pygame.transform.scale(image.subsurface((i * 23, 0), (23, 21)), size))
        self.image_idx = 0
        self.image = self.images[self.image_idx]
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.centery = position
        self.mask = pygame.mask.from_surface(self.image)

        self.speed = -10
        self.refresh_rate = 10
        self.refresh_counter = 0

    def draw(self, screen):
        screen.blit(self.image, self.rect)

    def update(self):
        if self.refresh_counter % self.refresh_rate == 0:
            self.refresh_counter = 0
            self.image_idx = (self.image_idx + 1) % len(self.images)
            self.loadImage()
        self.rect = self.rect.move([self.speed, 0])
        if self.rect.right < 0:
            self.kill()
        self.refresh_counter += 1

    def loadImage(self):
        self.image = self.images[self.image_idx]
        rect = self.image.get_rect()
        rect.left, rect.top = self.rect.left, self.rect.top
        self.rect = rect
        self.mask = pygame.mask.from_surface(self.image)
