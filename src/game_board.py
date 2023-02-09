import pygame as pg
import globals as g


def draw_board_grid(screen):
    for y in range(0, g.WINDOW_H, g.CELL_SIZE):
        for x in range(0, g.WINDOW_W, g.CELL_SIZE):
            rect = pg.Rect(x, y, g.CELL_SIZE, g.CELL_SIZE)
            pg.draw.rect(screen, g.GAMEBOARD_GRID_COLOR, rect, 1, 5)
