import pygame as pg

from snake import Snake
from game_timer import GameTimer
from food import Food
import globals as g

from game_board import draw_board_grid

def main():
    pg.init()

    screen = pg.display.set_mode(g.WINDOW_SIZE)

    game(screen)

def game(screen):
    clock = pg.time.Clock()
    timer = GameTimer(5)

    snake = Snake()
    food = snake.create_food()

    while True:
        for e in pg.event.get():
            if e.type == pg.QUIT:
                return
            snake.handle_event(e)

        if timer.is_tick():
            snake.update(food)

            if snake.bound_to_window() or snake.check_self_eating():
                game(screen)
                return

            screen.fill(g.BACKGROUND_COLOR)

            draw_board_grid(screen)
            food.draw(screen)
            snake.draw(screen)

            pg.display.update()

        clock.tick(60)

if __name__ == "__main__":
    main()