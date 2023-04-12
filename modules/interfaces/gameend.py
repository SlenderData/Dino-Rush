import sys
import pygame


def GameEndInterface(screen, cfg):
    replay_image = pygame.image.load(cfg.IMAGE_PATHS['replay'])
    replay_image = pygame.transform.scale(replay_image, (105, 93))
    replay_image_rect = replay_image.get_rect()
    replay_image_rect.centerx = cfg.SCREENSIZE[0] / 2
    replay_image_rect.top = cfg.SCREENSIZE[1] * 0.52
    font01 = pygame.font.Font(cfg.FONT_PATHS['joystix'], 36)
    gameover_text01 = font01.render("G A M E   O V E R", True, (83, 83, 83))
    gameover_text01_rect = gameover_text01.get_rect()
    gameover_text01_rect.centerx = cfg.SCREENSIZE[0] / 2
    gameover_text01_rect.centery = cfg.SCREENSIZE[1] * 0.35
    font02 = pygame.font.Font(cfg.FONT_PATHS['joystix'], 24)
    gameover_text02 = font02.render("PRESS [SPACE]/[ UP ] TO CONTINUE", True, (83, 83, 83))
    gameover_text02_rect = gameover_text02.get_rect()
    gameover_text02_rect.centerx = cfg.SCREENSIZE[0] / 2
    gameover_text02_rect.centery = cfg.SCREENSIZE[1] * 0.45
    clock = pygame.time.Clock()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE or event.key == pygame.K_UP:
                    return True
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                if replay_image_rect.collidepoint(mouse_pos):
                    return True
        screen.blit(replay_image, replay_image_rect)
        screen.blit(gameover_text01, gameover_text01_rect)
        screen.blit(gameover_text02, gameover_text02_rect)
        pygame.display.update()
        clock.tick(cfg.FPS)
