import pygame


class Ground(pygame.sprite.Sprite):
    def __init__(self, imagepath, position, **kwargs):
        pygame.sprite.Sprite.__init__(self)

        self.image_0 = pygame.image.load(imagepath)
        self.rect_0 = self.image_0.get_rect()
        self.rect_0.left, self.rect_0.bottom = position
        self.image_1 = pygame.image.load(imagepath)
        self.rect_1 = self.image_1.get_rect()
        self.rect_1.left, self.rect_1.bottom = self.rect_0.right, self.rect_0.bottom

        self.speed = -10

    def update(self):
        self.rect_0.left += self.speed
        self.rect_1.left += self.speed
        if self.rect_0.right < 0:
            self.rect_0.left = self.rect_1.right
        if self.rect_1.right < 0:
            self.rect_1.left = self.rect_0.right

    def draw(self, screen):
        screen.blit(self.image_0, self.rect_0)
        screen.blit(self.image_1, self.rect_1)


class Cloud(pygame.sprite.Sprite):
    def __init__(self, imagepath, position, **kwargs):
        pygame.sprite.Sprite.__init__(self)

        self.image = pygame.image.load(imagepath)
        self.image = pygame.transform.scale(self.image, (132, 45))
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.top = position

        self.speed = -1

    def draw(self, screen):
        screen.blit(self.image, self.rect)

    def update(self):
        self.rect = self.rect.move([self.speed, 0])
        if self.rect.right < 0:
            self.kill()


class Scoreboard(pygame.sprite.Sprite):
    def __init__(self, score, fontpath, position, is_highest=False):
        pygame.sprite.Sprite.__init__(self)

        self.text = []
        font = pygame.font.Font(fontpath, 24)
        self.score = str(score).zfill(5)
        if is_highest:
            self.text = font.render("HI " + self.score, True, (83, 83, 83))
        else:
            self.text = font.render(self.score, True, (83, 83, 83))
        self.rect = self.text.get_rect()
        self.rect.left, self.rect.top = position

    def draw(self, screen):
        screen.blit(self.text, self.rect)
