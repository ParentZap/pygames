import pygame
from pygame.locals import *
import random
from entity import Entity
from game_data import GameData


class Ball(Entity):

    def __init__(self, game_data: GameData, rad: int,
                 x: int, y: int, dx: int, dy: int) -> None:
        super().__init__(game_data)
        self.rad = rad
        self.x = x
        self.y = y
        self.dx = dx
        self.dy = dy

    def random(game_data: GameData):
        return Ball(
            game_data,
            rad=random.uniform(5, 30),
            x=random.uniform(0, game_data.display.get_width()),
            y=random.uniform(0, game_data.display.get_height()),
            dx=random.uniform(-5, 5),
            dy=random.uniform(-5, 5)
        )

    def add_dirty_rect(self):
        rad_plus = self.rad * 1.1
        dirty_rect = pygame.Rect(
            self.x - rad_plus, self.y - rad_plus, rad_plus * 2, rad_plus * 2)
        self.game_data.dirty_rects.append(dirty_rect)

    def update(self):
        self.add_dirty_rect()
        self.x += self.dx
        self.y += self.dy
        self.add_dirty_rect()

    def draw(self):
        pygame.draw.circle(
            self.game_data.display,
            (120, 0, 0),
            (int(self.x), int(self.y)),
            int(self.rad))
