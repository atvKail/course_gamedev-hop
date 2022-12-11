import time
import pygame
import os
from random import randrange


def image_filling(direct):
    fill = []
    for filename in os.listdir(direct):
        image = pygame.image.load(direct + "\\" + filename)
        fill.append([image, image.get_size()])
    return fill


def move(press, player, controls, r_line):
    if controls[press] == "r" and player[1][1] != 4:
        player[1][1] += 1
        player[1][0][0] = r_line[player[1][1]]
    if controls[press] == "l" and player[1][1] != 0:
        player[1][1] -= 1
        player[1][0][0] = r_line[player[1][1]]


def main():
    fps = pygame.time.Clock()
    speed = 15  # скорость
    update_speed = 30
    score = 0
    n_time = int(time.time())

    pygame.init()

    size = (1024, 840)  # размеры экрана
    road_line = [60, 260, 460, 660, 860]
    pygame.display.set_icon(pygame.image.load("Assets/gameicon.png"))
    pygame.display.set_caption("Racing game, Sergei Shukhov")
    screen = pygame.display.set_mode((size[0], size[1]))

    machinery = image_filling("Assets\\cars")
    moneys = [
        [x := pygame.image.load("Assets\\money\\one_money.png"), x.get_size(), 1],
        [x := pygame.image.load("Assets\\money\\five_money.png"), x.get_size(), 5],
        [x := pygame.image.load("Assets\\money\\ten_money.png"), x.get_size(), 10]
    ]
    road = pygame.image.load("Assets/road.png")
    blit_road = [-280, 0, 280, 560]
    player = [pygame.image.load("Assets\\player.png"), [[65, 630], 0]]  # player[1][1]
    # Какая дорога выбрана как начальная
    screen.blit(player[0], player[1][0])

    spawn_car = True
    spawnmoney_yes = True
    spawned = []
    spawnmoney = []
    controls = {  # контроль перемещений
        pygame.K_RIGHT: "r",
        pygame.K_LEFT: "l",
        pygame.K_UP: "u",
        pygame.K_DOWN: "d"
    }
    controls_if = controls.keys()

    con = 0
    game_end = False

    while True:
        if game_end:
            screen.fill((0, 0, 0))
            font = pygame.font.SysFont('comicsans', 30, True)
            finish_font = pygame.font.SysFont('comicsans', 60, True)
            Finish = finish_font.render(f'Score: {score}', True, (255, 255, 255))
            contin = font.render('Restart!? Press Space.', True, (255, 255, 255))
            game_quit = font.render('End!? Press Left Alt.', True, (255, 255, 255))
            screen.blit(contin, (340, 300))
            screen.blit(game_quit, (350, 400))
            screen.blit(Finish, (380, 200))
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LALT:
                        quit()
                    if event.key == pygame.K_SPACE:
                        main()
        else:
            if blit_road[0] >= 0:  # прорисовка дороги
                blit_road.insert(0, -280)
                del blit_road[-1]
            for pos in range(4):
                screen.blit(road, (0, blit_road[pos]))
                blit_road[pos] += speed
            screen.blit(player[0], player[1][0])

            if spawn_car:
                machin = machinery[randrange(len(machinery))]
                spawned = ["c", [road_line[randrange(0, 4)], -400], [pygame.transform.rotate(machin[0], 180), machin[1]]]
                spawn_car = False
            else:
                if spawned[1][1] >= 900:
                    spawn_car = True
                if spawned:
                    screen.blit(spawned[2][0], spawned[1])
                    spawned[1][1] += speed

            if spawnmoney_yes:
                spawnmoney = ["m", [road_line[randrange(0, 4)], -400], moneys[randrange(len(moneys))]]
                spawnmoney_yes = False
            else:
                if spawnmoney[1][1] >= 900:
                    spawnmoney_yes = True
                if spawnmoney:
                    screen.blit(spawnmoney[2][0], spawnmoney[1])
                    spawnmoney[1][1] += speed

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
                if event.type == pygame.KEYDOWN:
                    if event.key in controls_if:
                        move(event.key, player, controls, road_line)

            if (spawned[1][0] == player[1][0][0]) and \
            ((spawned[1][1] + spawned[2][1][1] - 15) >= player[1][0][1] and spawned[1][1] <= player[1][0][1] + 202):
                game_end = True

            if (spawnmoney[1][0] == player[1][0][0]) and \
            ((spawnmoney[1][1] + spawnmoney[2][1][1] - 15) >= player[1][0][1] and spawnmoney[1][1] <= player[1][0][1] + 202):
                score += spawnmoney[2][2]
                print(score)
                spawnmoney_yes = True

            if con % 100 == 0:
                speed += 1

        con += 1

        pygame.display.update()  # обновление
        fps.tick(update_speed)


if __name__ == "__main__":
    main()
