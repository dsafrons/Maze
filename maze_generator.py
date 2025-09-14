from random import choice


class MazeGenerator:
    def __init__(self, tiles):
        self.tiles = tiles
        self.maze = self.format_maze()
        self.visited = []

    def format_maze(self):
        list_size = self.tiles * 2 - 1
        vertical_row = [i % 2 for i in range(list_size)]
        horizontal_row = [1 if i % 2 == 0 else -1 for i in range(list_size)]

        return [list(vertical_row) if i % 2 == 0 else list(horizontal_row) for i in range(list_size)]

    def get_unvisited_neighbors(self, cell):
        unvisited = []

        if cell[1] != 0 and [cell[0], cell[1]-1] not in self.visited:
            unvisited.append([cell[0], cell[1]-1])

        if cell[1] != self.tiles-1 and [cell[0], cell[1]+1] not in self.visited:
            unvisited.append([cell[0], cell[1]+1])

        if cell[0] != 0 and [cell[0]-1, cell[1]] not in self.visited:
            unvisited.append([cell[0]-1, cell[1]])

        if cell[0] != self.tiles-1 and [cell[0]+1, cell[1]] not in self.visited:
            unvisited.append([cell[0]+1, cell[1]])

        return unvisited

    def remove_wall_between(self, cell1, cell2):
        if cell1[0] != cell2[0]:
            # removing horizontal wall
            highest_y = max(cell1[0], cell2[0])
            self.maze[highest_y*2-1][cell1[1]*2] = 2

        elif cell1[1] != cell2[1]:
            # removing vertical wall
            highest_x = max(cell1[1], cell2[1])
            self.maze[cell1[0]*2][highest_x*2-1] = 2

    def recursive_maze(self, cell):
        self.visited.append(cell)

        while any(self.get_unvisited_neighbors(cell)):
            to_check = choice(self.get_unvisited_neighbors(cell))
            self.remove_wall_between(cell, to_check)
            self.recursive_maze(to_check)

    def generate_maze(self):
        self.recursive_maze([0, 0])

        return self.maze
