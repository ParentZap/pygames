import pygame
from pygame.locals import *
from config import *
from game_data import GameData
from ball import Ball


class App:

    def __init__(self) -> None:
        pygame.init()
        dirty_rects = []
        entities = []
        display = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.game_data = GameData(display, dirty_rects, entities)
        self.quit = False

    def update(self) -> None:
        for entity in self.game_data.entities:
            entity.update()

    def draw(self) -> None:
        pygame.draw.rect(self.game_data.display, (0,0,0), (0, 0, SCREEN_WIDTH, SCREEN_HEIGHT))
        for entity in self.game_data.entities:
            entity.draw()

        # pygame.display.update()
        pygame.display.update(self.game_data.dirty_rects)
        self.game_data.dirty_rects.clear()

    def process_events(self) -> None:
        for event in pygame.event.get():
            if event.type == QUIT:
                self.quit = True

    def game_loop(self) -> None:
        self.clock = pygame.time.Clock()
        for _ in range(10):
            self.game_data.entities.append(Ball.random(self.game_data))

        while not self.quit:
            self.clock.tick(FPS)
            self.process_events()
            self.update()
            self.draw()

    def main(self) -> None:
        self.game_loop()


if __name__ == "__main__":
    app = App()
    app.main()
