import pygame
from pygame.locals import *
from config import *


class App:

    def __init__(self) -> None:
        pygame.init()
        self.dirty_rects = []
        self.display = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.quit = False

    def update(self) -> None:
        pass

    def draw(self) -> None:
        pygame.display.update(self.dirty_rects)
        self.dirty_rects.clear()

    def process_events(self) -> None:
        for event in pygame.event.get():
            if event.type == QUIT:
                self.quit = True

    def game_loop(self) -> None:
        while not self.quit:
            self.process_events()
            self.update()
            self.draw()

    def main(self) -> None:
        self.game_loop()


if __name__ == "__main__":
    app = App()
    app.main()
