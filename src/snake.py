import pygame as pg
import globals as g
from food import Food


class Snake:
    def __init__(self):
        self.__body = [(0, 2), (0, 1), (0, 0)]
        self.__direction = "right"
        self.__prev_direction = self.__direction

    def handle_event(self, event):
        if event.type != pg.KEYDOWN:
            return

        vertical = self.__prev_direction in ("up", "down")

        if vertical:
            if event.key == pg.K_a:
                self.__direction = "left"
            if event.key == pg.K_d:
                self.__direction = "right"
            return

        if event.key == pg.K_w:
            self.__direction = "up"
        if event.key == pg.K_s:
            self.__direction = "down"

    def update(self, food):
        DIRECTION_TO_OFFSET = {
            "up": (-1, 0),
            "right": (0, 1),
            "down": (1, 0),
            "left": (0, -1),
        }
        off = DIRECTION_TO_OFFSET[self.__direction]
        self.__prev_direction = self.__direction

        head = self.__body[0]
        new_head = (head[0] + off[0], head[1] + off[1])

        self.__body.insert(0, new_head)

        if new_head != food.get_track():
            self.__body.pop()
            return

        food.update_track(self.__body)

    def bound_to_window(self):
        (r, c) = self.__body[0]

        if r < 0 or r >= g.CELL_ROWS:
            return True
        if c < 0 or c >= g.CELL_COLS:
            return True
        return False

    def check_self_eating(self):
        for i, a in enumerate(self.__body):
            for b in self.__body[i + 1 :]:
                if a == b:
                    return True
        return False

    def draw(self, screen):
        (r, c) = self.__body[0]
        rect = pg.Rect(c * g.CELL_SIZE, r * g.CELL_SIZE, g.CELL_SIZE, g.CELL_SIZE)
        pg.draw.ellipse(screen, g.SNAKE_COLOR, rect)

        for r, c in self.__body[1:]:
            rect = pg.Rect(c * g.CELL_SIZE, r * g.CELL_SIZE, g.CELL_SIZE, g.CELL_SIZE)
            pg.draw.rect(screen, g.SNAKE_COLOR, rect, border_radius=5)

    def create_food(self):
        return Food(self.__body)
