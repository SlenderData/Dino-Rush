import core
import sys
import time
import random
import pygame
import sqlite3
from modules import *


def main(highest_score):
    pygame.init()
    screen = pygame.display.set_mode(core.SCREENSIZE)
    pygame.display.set_caption('毕业设计_马云骥_12042034')

    sounds = {}
    for key, value in core.AUDIO_PATHS.items():
        sounds[key] = pygame.mixer.Sound(value)

    GameStartInterface(screen, sounds, core)

    score = 0
    highest_score = highest_score
    dino = Dinosaur(core.IMAGE_PATHS['dino'])
    ground = Ground(core.IMAGE_PATHS['ground'], position=(0, core.SCREENSIZE[1] * 0.93))
    cloud_sprites_group = pygame.sprite.Group()
    cactus_sprites_group = pygame.sprite.Group()
    ptera_sprites_group = pygame.sprite.Group()
    add_obstacle_timer = 0
    score_timer = 0

    clock = pygame.time.Clock()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE or event.key == pygame.K_UP:
                    dino.jump(sounds)
                elif event.key == pygame.K_DOWN:
                    dino.duck()
            elif event.type == pygame.KEYUP and event.key == pygame.K_DOWN:
                dino.unduck()
        screen.fill(core.BACKGROUND_COLOR)

        if len(cloud_sprites_group) < 5 and random.randrange(0, 300) == 10:
            cloud_sprites_group.add(
                Cloud(core.IMAGE_PATHS['cloud'], position=(core.SCREENSIZE[0], random.randrange(30, 200))))

        add_obstacle_timer += 1
        if add_obstacle_timer > random.randrange(80, 130):
            add_obstacle_timer = 0
            random_value = random.randrange(0, 10)
            if random_value >= 0 and random_value <= 7:
                cactus_sprites_group.add(Cactus(core.IMAGE_PATHS['cacti']))
            else:
                position_ys = [core.SCREENSIZE[1] * 0.82, core.SCREENSIZE[1] * 0.63, core.SCREENSIZE[1] * 0.30]
                ptera_sprites_group.add(
                    Ptera(core.IMAGE_PATHS['ptera'], position=(core.SCREENSIZE[0], random.choice(position_ys))))

        dino.update()
        ground.update()
        cloud_sprites_group.update()
        cactus_sprites_group.update()
        ptera_sprites_group.update()
        score_timer += 1
        if score_timer > (core.FPS // 12):
            score_timer = 0
            score += 1
            score = min(score, 99999)
            if score > highest_score:
                highest_score = score
            if score % 100 == 0:
                sounds['point'].play()
            if score % 1000 == 0:
                ground.speed -= 1
                for item in cloud_sprites_group:
                    item.speed -= 1
                for item in cactus_sprites_group:
                    item.speed -= 1
                for item in ptera_sprites_group:
                    item.speed -= 1

        for item in cactus_sprites_group:
            if pygame.sprite.collide_mask(dino, item):
                dino.die(sounds)
        for item in ptera_sprites_group:
            if pygame.sprite.collide_mask(dino, item):
                dino.die(sounds)

        cloud_sprites_group.draw(screen)
        dino.draw(screen)
        ground.draw(screen)
        cactus_sprites_group.draw(screen)
        ptera_sprites_group.draw(screen)

        score_board = Scoreboard(score, core.FONT_PATHS['joystix'],
                                 position=(core.SCREENSIZE[0] * 0.88, core.SCREENSIZE[1] * 0.05))
        highest_score_board = Scoreboard(highest_score, core.FONT_PATHS['joystix'],
                                         position=(core.SCREENSIZE[0] * 0.72, core.SCREENSIZE[1] * 0.05),
                                         is_highest=True)
        score_board.draw(screen)
        highest_score_board.draw(screen)

        pygame.display.update()
        clock.tick(core.FPS)

        if dino.is_dead:
            localtime = time.time()
            c.execute("INSERT INTO record (unix_timestamp, score) VALUES (?,?);", (localtime, score))
            conn.commit()
            break

    return GameEndInterface(screen, core), highest_score


if __name__ == '__main__':
    conn = sqlite3.connect('history.db')
    c = conn.cursor()
    c.execute("CREATE TABLE IF NOT EXISTS record (unix_timestamp INT PRIMARY KEY, score SMALLINT NOT NULL);")
    c.execute("SELECT MAX(score) FROM record;")
    rows = c.fetchall()
    for row in rows:
        highest_score = row[0]
    if not str(highest_score).isdigit():
        highest_score = 0
    while True:
        flag, highest_score = main(highest_score)
        if not flag: break
    conn.commit()
    conn.close()
