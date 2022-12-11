from random import randrange as rnd
import pygame
import os


def image_filling(direct):
    fill = []
    for filename in os.listdir(direct):
        image = pygame.image.load(direct + "\\" + filename)
        fill.append([image, image.get_size()])
    return fill


def main():
    fps = pygame.time.Clock()
    speed = 13  # скорость
    update_speed = 30

    pygame.init()

    size = (1024, 840)  # размеры экрана
    road_line = [60, 260, 460, 660, 860]
    font = pygame.font.SysFont('comicsans', 30, True)
    pygame.display.set_icon(pygame.image.load("Assets/gameicon.png"))
    pygame.display.set_caption("Racing game, Sergei Shukhov")
    screen = pygame.display.set_mode((size[0], size[1]))
    ctrl = 0

    machinery = image_filling("Assets\\cars")
    road = pygame.image.load("Assets/road.png")
    fi_road = pygame.image.load("Assets\\finish_road.png")
    blit_road = [-280, 0, 280, 560]
    player = [pygame.image.load("Assets\\player.png"), [[460, 630], 3]]  # player[1][1]
    # Какая дорога выбрана как начальная
    screen.blit(player[0], player[1][0])

    speed_cars = [rnd(7, 30), rnd(7, 30), rnd(7, 30), rnd(7, 30)]
    cars_pos = [[road_line[0], 630], [road_line[1], 630], [road_line[3], 630], [road_line[4], 630]]
    cars_data = [machinery[1], machinery[3], machinery[5], machinery[6]]

    game_end = False

    while True:
        if game_end:
            screen.fill((0, 0, 0))
            font = pygame.font.SysFont('comicsans', 30, True)
            finish_font = pygame.font.SysFont('comicsans', 60, True)
            Finish = finish_font.render('Finish!!!', True, (255, 255, 255))
            contin = font.render('Restart!? Press Space.', True, (255, 255, 255))
            game_quit = font.render('End!? Press Left Alt.', True, (255, 255, 255))
            screen.blit(contin, (340, 300))
            screen.blit(game_quit, (350, 400))
            screen.blit(Finish, (400, 200))
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
            position = 1
            if blit_road[0] >= 0:  # прорисовка дороги
                blit_road.insert(0, -280)
                del blit_road[-1]
            for pos in range(4):
                screen.blit(road, (0, blit_road[pos]))
                blit_road[pos] += speed
            screen.blit(player[0], player[1][0])

            for i in range(len(cars_pos)):
                if cars_pos[i][1] < player[1][0][1]:
                    position += 1
            position_text = font.render('Position: ' + str(position), True, (0, 0, 0))
            speed_bar = font.render('Speed: ' + str(int(speed)), True, (0, 0, 0))
            click_text = font.render('CLICK SPASE!!!', True, (0, 0, 0))
            Non_click_text = font.render('Ctrl = Reduct speed ', True, (0, 0, 0))
            screen.blit(speed_bar, (40, 10))
            screen.blit(click_text, (770, 770))
            screen.blit(Non_click_text, (700, 800))
            screen.blit(position_text, (40, 40))

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_LCTRL:
                        ctrl = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        speed += 2
                        for _ in range(len(cars_pos)):
                            cars_pos[_][1] += speed
                    if event.key == pygame.K_LCTRL:
                        ctrl = True

            if ctrl:
                speed -= 2
            if round(speed) > 0:
                speed -= 0.1
            else:
                speed = 0
            for _ in range(len(cars_pos)):
                screen.blit(cars_data[_][0], cars_pos[_])
                cars_pos[_][1] -= speed_cars[_]

            if int(speed) >= 300:
                game_end = True

        pygame.display.update()  # обновление
        fps.tick(update_speed)


if __name__ == "__main__":
    main()
