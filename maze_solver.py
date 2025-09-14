from pygame import Vector2


class Solver:
    def __init__(self, maze, end_pos):
        self.maze = maze
        self.visited = []
        self.correct_path = []
        self.init_list()

        self.end = Vector2(int(end_pos[0]), int(end_pos[1]))
        self.path_counter = 1
        self.show_solved = False

    def reformat_correct_path(self):
        reformat = []
        for i in range(len(self.correct_path)):
            if i % 2 == 0:
                temp = []
                for j in range(len(self.correct_path[i])):
                    if j % 2 == 0:
                        temp.append(self.correct_path[i][j])
                reformat.append(temp)

        self.correct_path = reformat

    def init_list(self):
        for i in range(len(self.maze)):
            temp_list = []
            for j in range(len(self.maze[i])):
                temp_list.append(0)
            self.correct_path.append(list(temp_list))

    def solve_maze(self):
        return self.recursive_solve(0, 0)

    def recursive_solve(self, x, y):
        if x == self.end.x and y == self.end.y:
            self.correct_path[y][x] = int(self.path_counter)
            self.path_counter += 0.5
            return True

        if [x, y] in self.visited or self.maze[y][x] in [1, -1]:
            return False

        self.visited.append([x, y])

        if x != 0:
            if self.recursive_solve(x-1, y):
                self.correct_path[y][x] = int(self.path_counter)
                self.path_counter += 0.5
                return True

        if x != len(self.maze)-1:
            if self.recursive_solve(x+1, y):
                self.correct_path[y][x] = int(self.path_counter)
                self.path_counter += 0.5
                return True

        if y != 0:
            if self.recursive_solve(x, y-1):
                self.correct_path[y][x] = int(self.path_counter)
                self.path_counter += 0.5
                return True

        if y != len(self.maze)-1:
            if self.recursive_solve(x, y+1):
                self.correct_path[y][x] = int(self.path_counter)
                self.path_counter += 0.5
                return True

        return False

