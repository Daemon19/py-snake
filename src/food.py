import pygame as pg
import globals as g
from random import randrange


class Food:
    def __init__(self, snake_body):
        self.update_track(snake_body)

    def draw(self, screen):
        r, c = self.__track
        rect = pg.Rect(c * g.CELL_SIZE, r * g.CELL_SIZE, g.CELL_SIZE, g.CELL_SIZE)
        pg.draw.ellipse(screen, g.FOOD_COLOR, rect)

    def update_track(self, snake_body):
        while True:
            self.__track = randrange(0, g.CELL_ROWS), randrange(0, g.CELL_COLS)

            if self.__track not in snake_body:
                break

    def get_track(self):
        return self.__track
