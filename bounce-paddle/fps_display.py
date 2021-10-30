import pygame
from pygame.locals import *
import time
from events import *
from entity import Entity
from game_data import GameData


class FpsDisplay(Entity):

    def __init__(self, game_data: GameData, clock: pygame.time.Clock, x: int, y: int) -> None:
        super().__init__(game_data)
        self.clock = clock
        self.x = x
        self.y = y
        self.font = pygame.font.SysFont(name="Helvetica", size=30)
        self.text_surface = None
        self.should_update = True

    def top_left(game_data: GameData, clock: pygame.time.Clock):
        return FpsDisplay(game_data, clock, x=0, y=0)

    def add_dirty_rect(self):
        if self.text_surface:
            dirty_rect = pygame.Rect(
                self.x,
                self.y,
                self.x + self.text_surface.get_width(),
                self.y + self.text_surface.get_height())
            self.game_data.dirty_rects.append(dirty_rect)

    def set_should_update(self):
        self.should_update = True

    def __update(self):
        self.add_dirty_rect()
        self.text_surface = self.font.render(
            "{:2.2f}".format(self.clock.get_fps()),
            False,
            (255, 255, 255))
        self.add_dirty_rect()

    def update(self):
        if self.should_update:
            self.should_update = False
            self.__update()
            pygame.time.set_timer(DISPLAY_FPS_EVENT, 100)

    def draw(self):
        if self.text_surface:
            self.game_data.display.blit(self.text_surface, (self.x, self.y))
