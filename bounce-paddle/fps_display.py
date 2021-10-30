import pygame
from pygame.locals import *
import time
from entity import Entity
from game_data import GameData


class FpsDisplay(Entity):

    def __init__(self, game_data: GameData, x: int, y: int) -> None:
        super().__init__(game_data)
        self.x = x
        self.y = y
        self.font = pygame.font.SysFont(name="Helvetica", size=30)
        self.text_surface = None
        self.last_frame_time = None

    def top_left(game_data: GameData):
        return FpsDisplay(game_data, x=0, y=0)

    def add_dirty_rect(self):
        if self.text_surface:
            dirty_rect = pygame.Rect(
                self.x,
                self.y,
                self.x + self.text_surface.get_width(),
                self.y + self.text_surface.get_height())
            self.game_data.dirty_rects.append(dirty_rect)

    def update(self):
        self.add_dirty_rect()
        curr_time = time.time()
        if self.last_frame_time:
            time_since = curr_time - self.last_frame_time
            effective_fps = 1 / time_since
            self.text_surface = self.font.render(
                "{:2.2f}".format(effective_fps),
                False,
                (255, 255, 255))
        self.last_frame_time = curr_time
        self.add_dirty_rect()

    def draw(self):
        if self.text_surface:
            self.game_data.display.blit(self.text_surface, (self.x, self.y))
