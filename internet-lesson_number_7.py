import time
import pygame
from random import randrange


def game_end(score):
    print(score)
    if input("continue? => Yes or NO | ").lower() == "yes":
        main()
    else:
        print("quit....")
        time.sleep(1)
        exit()


def main():
    fps = pygame.time.Clock()
    snake_speed = 15  # скорость
    score = 0

    pygame.init()
    size = [650, 500]  # размеры экрана
    pygame.display.set_caption("Snake game, Sergei Shukhov")
    screen = pygame.display.set_mode((size[0], size[1]))

    # Палитра
    BLACK = pygame.color.Color("black")  # цвет экрана
    RED = pygame.color.Color("red")  # цвет яблочка
    GREEN = pygame.color.Color("green")  # цвет змейки

    player_pos = [100, 50]  # начальная позиция игрока, изменяя её нужно изменять и snake_body со сдвигом 10
    snake_body = [[100, 50]]  # тело змейки, [[координаты квадрата x, y], [координаты квадрата x, y]...]
    fruit_pos = [randrange(1, size[0] // 10) * 10, randrange(1, size[1] // 10) * 10]  # 10px разделение

    fruit_spawn = True
    controls = {  # контроль перемещений
        pygame.K_RIGHT: (10, 0),
        pygame.K_LEFT: (-10, 0),
        pygame.K_UP: (0, -10),
        pygame.K_DOWN: (0, 10)
    }
    controls_if = controls.keys()
    condis = {  # Словарь, чтобы не дать игроку повернуть змейку "в себя", спасает от неприятных случайностей
        pygame.K_DOWN: pygame.K_UP,
        pygame.K_UP: pygame.K_DOWN,
        pygame.K_LEFT: pygame.K_RIGHT,
        pygame.K_RIGHT: pygame.K_LEFT
    }

    pressed = pygame.K_RIGHT  # можно задать начальное направление, по умолчанию движение направо
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.KEYDOWN:
                if event.key != condis[pressed]:
                    if event.key in controls_if:
                        pressed = event.key
        player_pos[0] += controls[pressed][0]
        player_pos[1] += controls[pressed][1]
        snake_body.insert(0, list(player_pos))

        if player_pos[0] == fruit_pos[0] and player_pos[1] == fruit_pos[1]:  # check pos fruit
            fruit_pos = [randrange(1, (size[0] // 10)) * 10, randrange(1, (size[1] // 10)) * 10]
            score += 5
        else:
            snake_body.pop()

        screen.fill(BLACK)  # Отрисовка
        for pos in snake_body:
            pygame.draw.rect(screen, GREEN, pygame.Rect(pos[0], pos[1], 10, 10))
        pygame.draw.rect(screen, RED, pygame.Rect(fruit_pos[0], fruit_pos[1], 10, 10))

        # Проверка на выход за границы и на пересечение своего тела
        if player_pos[0] < 0 or player_pos[0] > size[0] - 10 or player_pos[1] < 0 or player_pos[1] > size[1] - 10:
            game_end(score)
        for block in snake_body[1:]:
            if player_pos[0] == block[0] and player_pos[1] == block[1]:
                game_end(score)

        pygame.display.update()  # обновление
        fps.tick(snake_speed)


if __name__ == "__main__":
    main()
