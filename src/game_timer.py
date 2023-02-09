import pygame as pg


class GameTimer:
    def __init__(self, tickPerSec):
        self.__frame_time = 1000 // tickPerSec
        self.__last_time = pg.time.get_ticks()

    def is_tick(self):
        current = pg.time.get_ticks()
        elapsed = current - self.__last_time

        if elapsed > self.__frame_time:
            self.__last_time = current
            return True
        return False
