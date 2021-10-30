import pygame
from pygame.locals import *
from config import *
from events import *
from game_data import GameData
from ball import Ball
from fps_display import FpsDisplay


class App:

    def __init__(self) -> None:
        pygame.init()
        pygame.font.init()
        dirty_rects = []
        entities = []
        display = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.game_data = GameData(display, dirty_rects, entities)
        self.fps_display = None
        self.quit = False

    def update(self) -> None:
        for entity in self.game_data.entities:
            entity.update()

    def draw(self) -> None:
        pygame.draw.rect(self.game_data.display, (0, 0, 0),
                         (0, 0, SCREEN_WIDTH, SCREEN_HEIGHT))
        for entity in self.game_data.entities:
            entity.draw()

        pygame.display.update(self.game_data.dirty_rects)
        self.game_data.dirty_rects.clear()

    def handle_events(self) -> None:
        for event in pygame.event.get():
            if event.type == QUIT:
                self.quit = True
            if event.type == DISPLAY_FPS_EVENT:
                self.fps_display.set_should_update()

    def game_loop(self) -> None:
        while not self.quit:
            self.clock.tick(FPS)
            self.handle_events()
            self.update()
            self.draw()

    def setup(self) -> None:
        self.clock = pygame.time.Clock()
        if DISPLAY_FPS:
            self.fps_display = FpsDisplay.top_left(self.game_data)
            self.game_data.entities.append(self.fps_display)

        for _ in range(10):
            self.game_data.entities.append(Ball.random(self.game_data))

    def main(self) -> None:
        self.setup()
        self.game_loop()


if __name__ == "__main__":
    app = App()
    app.main()
