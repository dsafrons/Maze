import pygame
from sys import exit, setrecursionlimit

from maze import Maze
from ui import UI
from settings import *


class Game:
    def __init__(self, display_surface, clock):
        self.display_surface = display_surface
        self.clock = clock

        self.maze = Maze(pygame.Surface([MAZE_SURFACE_WIDTH, MAZE_SURFACE_HEIGHT]), INIT_MAZE_SIZE)
        self.ui = UI(pygame.Surface([UI_SURFACE_WIDTH, UI_SURFACE_HEIGHT]))

    def blit_surfaces(self):
        self.display_surface.blit(self.maze.maze_surface, (UI_SURFACE_WIDTH, 0))
        self.display_surface.blit(self.ui.ui_surface, (0, 0))

    def update_surfaces(self, dt, events):
        self.maze.update_maze_surface(dt, events)
        self.ui.update_ui_surface(dt, events, self.maze)

    def update(self, dt, events):
        self.update_surfaces(dt, events)
        self.blit_surfaces()


class Main:
    def __init__(self):
        setrecursionlimit(RECURSION_LIMIT)
        pygame.init()

        pygame.display.set_caption('Maze')
        self.display_surface = pygame.display.set_mode([SCREEN_WIDTH, SCREEN_HEIGHT])
        self.clock = pygame.time.Clock()

        self.game = Game(self.display_surface, self.clock)

    def run(self):
        while True:
            dt = self.clock.tick(FPS) / 1000
            ev = pygame.event.get()
            for event in ev:
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()

            self.game.update(dt, ev)

            pygame.display.update()


if __name__ == '__main__':
    main = Main()
    main.run()
