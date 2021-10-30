from typing import List
import pygame
from pygame.locals import *

class GameData:

    def __init__(self, display: pygame.Surface, dirty_rects: List[pygame.Rect], entities: List) -> None:
        self.display = display
        self.dirty_rects = dirty_rects
        self.entities = entities
