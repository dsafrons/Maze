import pygame
from math import ceil

from blob import Blob
from maze_generator import MazeGenerator
from maze_solver import Solver
from settings import *


class Maze:
    def __init__(self, maze_surface, maze_size, maze_solved_color=MAZE_SOLVED_TILE_COLOR):
        self.maze_generator = MazeGenerator(maze_size)
        self.maze = self.maze_generator.generate_maze()

        self.tile_size = MAZE_SURFACE_WIDTH / ((len(self.maze) + 1) / 2)
        self.line_thickness = ceil(self.tile_size/70)
        self.maze_surface = maze_surface
        self.maze_solved_color = maze_solved_color

        self.blob = Blob((len(self.maze) + 1) / 2 - 1, self.tile_size)
        self.solver = Solver(self.maze, (len(self.maze) - 1, len(self.maze) - 1))

    def generate_new_maze(self, new_size):
        self.__init__(self.maze_surface, new_size, self.maze_solved_color)

    def draw_borders(self):
        pygame.draw.line(self.maze_surface, LINE_COLOR, [0, 0], [MAZE_SURFACE_WIDTH, 0], 4)
        pygame.draw.line(self.maze_surface, LINE_COLOR, [0, 0], [0, MAZE_SURFACE_HEIGHT], 4)
        pygame.draw.line(self.maze_surface, LINE_COLOR, [MAZE_SURFACE_WIDTH - 2, 0], [MAZE_SURFACE_WIDTH - 2, MAZE_SURFACE_HEIGHT], 4)
        pygame.draw.line(self.maze_surface, LINE_COLOR, [0, MAZE_SURFACE_HEIGHT - 2], [MAZE_SURFACE_WIDTH, MAZE_SURFACE_HEIGHT - 2], 4)

    def draw_maze(self):
        lines = []
        dots = []
        
        for i in range(len(self.maze)):
            for j in range(len(self.maze[i])):
                
                if i % 2 == 0 and j % 2 == 1:
                    # vertical bar
                    if self.maze[i][j] == 1:
                        x = self.tile_size * ((j / 2) + 0.5)
                        y = self.tile_size * (i / 2)
                        lines.append([[x, y], [x, y + self.tile_size]])

                if i % 2 == 1:
                    # horizontal bar
                    if self.maze[i][j] == 1:
                        x = self.tile_size * (j / 2)
                        y = self.tile_size * ((i / 2) + 0.5)
                        lines.append([[x, y], [x + self.tile_size, y]])

                    # corner dot
                    elif self.maze[i][j] == -1:
                        # only drawing dot if maze is 10x10 or less
                        if (len(self.maze) + 1) / 2 <= 10:
                            x = self.tile_size * (j / 2) + (self.tile_size / 2)
                            y = self.tile_size * ((i / 2) + 0.5)
                            dots.append(pygame.Rect(x, y, 2, 2))

                if self.solver.show_solved:
                    if i % 2 == 0 and j % 2 == 0:
                        # only drawing on solved squares not on start
                        if self.solver.correct_path[int(i / 2)][int(j / 2)] not in [0, 1]:
                            x = self.tile_size * (j / 2)
                            y = self.tile_size * (i / 2)
                            pygame.draw.rect(self.maze_surface, self.maze_solved_color, pygame.Rect(x, y, self.tile_size+1, self.tile_size+1))

                if (i == len(self.maze) - 1 and j == len(self.maze) - 1) or (i == 0 and j == 0):
                    x = self.tile_size * (j / 2)
                    y = self.tile_size * (i / 2)
                    if i == 0:
                        # ending green square
                        pygame.draw.rect(self.maze_surface, END_SQUARE_COLOR, pygame.Rect(x+2, y+2, self.tile_size-1, self.tile_size-1))
                    else:
                        # starting red square
                        pygame.draw.rect(self.maze_surface, START_SQUARE_COLOR, pygame.Rect(x+1, y, self.tile_size, self.tile_size))

        for line in lines:
            pygame.draw.line(self.maze_surface, LINE_COLOR, line[0], line[1], self.line_thickness)

        for dot in dots:
            pygame.draw.rect(self.maze_surface, LINE_COLOR, dot)

    def check_win(self):
        if self.blob.pos == [0, 0]:
            print('win')

    def update_maze_surface(self, dt, events):
        self.blob.update(events, self.maze)
        self.check_win()

        self.maze_surface.fill(MAZE_BACKGROUND_COLOR)
        self.draw_maze()
        self.draw_borders()
        self.blob.display(self.maze_surface, dt)
