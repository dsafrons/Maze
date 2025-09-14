# Maze (Python + PyGame)

A maze generation and solving program built in Python with **PyGame** and **pygame_gui**.  
It includes a visual UI, automatic maze generation, a solving algorithm, and a controllable “blob” character.

## Features

- **Maze generation** (`maze_generator.py`)  
  - Generates a randomized maze grid using a recursive backtracking approach  
  - Scales to different maze sizes  

- **Maze solver** (`maze_solver.py`)  
  - Finds a correct path through the maze to the exit  
  - Option to display the solved path  

- **Blob character** (`blob.py`)  
  - Sprite image (`blob.png`) scaled to maze tiles  
  - Represents the player within the maze  

- **UI controls** (`ui.py`)  
  - Built with `pygame_gui` and styled with `theme.json`  
  - Buttons for changing maze size, regenerating mazes, and toggling solver view  

- **Settings** (`settings.py`)  
  - Adjustable FPS, screen resolution, colors, and recursion limits  

- **Main game loop** (`main.py`)  
  - Initializes PyGame display and clock  
  - Runs the `Maze` object and the UI together  

## Requirements

- Python 3.8+
- [pygame](https://pypi.org/project/pygame/)
- [pygame_gui](https://pypi.org/project/pygame-gui/)

Install dependencies:
```
pip install pygame pygame-gui
```

## Project Structure
```
Maze/
├── main.py            # Game loop tying together Maze + UI
├── maze.py            # Maze class (generation, drawing, integration with solver/blob)
├── maze_generator.py  # MazeGenerator class (randomized generation logic)
├── maze_solver.py     # Solver class (pathfinding through maze)
├── blob.py            # Blob class (player character sprite)
├── ui.py              # UI class (pygame_gui buttons, text, dimensions)
├── settings.py        # Global settings (screen size, FPS, colors, etc.)
├── blob.png           # Blob sprite image
├── font.otf           # Font used for UI text
├── theme.json         # UI theme configuration
└── README.md
```

## How it Works
**1. Maze Generation**

- A `MazeGenerator` creates a randomized maze layout.
- Odd-sized grids ensure proper wall placement.

**2. Gameplay**

- The `Maze` class draws the maze and places a start (red) and end (green) square.
- A `Blob` sprite is scaled to tile size and displayed inside the maze.

**3. Solving**

- The `Solver` explores the maze recursively to find a path from start to end.
- The correct path can be highlighted in yellow when toggled.

**4. UI**

- Dimension buttons allow resizing the maze.
- Reset/regenerate options let players quickly test new mazes.

## Future Improvements

- Different solving algorithms (A*) for performance comparison
- Maze export (save to image or text)
- Difficulty levels (easy → very large mazes)
- Timer/scoring system for player challenge
