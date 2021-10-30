from typing import List
import pygame
from pygame.locals import *
from abc import ABC, abstractmethod
from game_data import GameData

class Entity(ABC):

    def __init__(self, game_data:GameData) -> None:
        super().__init__()
        self.game_data = game_data

    @abstractmethod
    def update(self):
        pass

    @abstractmethod
    def draw(self):
        pass