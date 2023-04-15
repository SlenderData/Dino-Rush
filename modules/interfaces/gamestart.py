import sys
import pygame
from ..sprites import Dinosaur


def GameStartInterface(screen, sounds, cfg):
    font01 = pygame.font.Font(cfg.FONT_PATHS['joystix'], 48)
    gamestart_text01 = font01.render("D I N O  R U S H", True, (83, 83, 83))
    gamestart_text01_rect = gamestart_text01.get_rect()
    gamestart_text01_rect.centerx = cfg.SCREENSIZE[0] / 2
    gamestart_text01_rect.centery = cfg.SCREENSIZE[1] * 0.35
    font02 = pygame.font.Font(cfg.FONT_PATHS['joystix'], 18)
    gamestart_text02 = font02.render("DESIGNED BY SLENDERDATA", True, (83, 83, 83))
    gamestart_text02_rect = gamestart_text02.get_rect()
    gamestart_text02_rect.centerx = cfg.SCREENSIZE[0] / 2
    gamestart_text02_rect.centery = cfg.SCREENSIZE[1] * 0.45
    dino = Dinosaur(cfg.IMAGE_PATHS['dino'])
    ground = pygame.image.load(cfg.IMAGE_PATHS['ground']).subsurface((0, 0), (1200, 48))
    rect = ground.get_rect()
    rect.left = 0
    rect.bottom = cfg.SCREENSIZE[1] * 0.93
    clock = pygame.time.Clock()
    press_flag = False
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE or event.key == pygame.K_UP:
                    press_flag = True
                    dino.jump(sounds)
        dino.update()
        screen.fill(cfg.BACKGROUND_COLOR)
        screen.blit(ground, rect)
        screen.blit(gamestart_text01, gamestart_text01_rect)
        screen.blit(gamestart_text02, gamestart_text02_rect)
        dino.draw(screen)
        pygame.display.update()
        clock.tick(cfg.FPS)
        if (not dino.is_jumping) and press_flag:
            return True
