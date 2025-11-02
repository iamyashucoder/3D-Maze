# 3D Maze Generator and Solver

A Python project that creates procedurally generated 3D mazes and solves them using pathfinding algorithms.

## Features

- **Procedural Generation**: Creates unique 3D mazes using recursive backtracking
- **Pathfinding**: Solves mazes using Breadth-First Search (BFS) algorithm
- **3D Visualization**: Interactive 3D visualization with matplotlib
- **Simple Navigation**: View the maze from any angle with mouse controls

## Setup Instructions

### 1. Create Conda Environment

```bash
conda create -n maze3d python=3.9 -y
conda activate maze3d
```

### 2. Install Required Packages

```bash
pip install numpy matplotlib
```

That's it! Only two packages needed.

### 3. Run the Demo

```bash
python main.py
```

## How It Works

### Maze Generation
- Uses **recursive backtracking** algorithm
- Creates random paths through a 3D grid
- Ensures connected passages throughout the maze

### Pathfinding
- Uses **Breadth-First Search (BFS)** algorithm
- Finds the shortest path from start to end
- Guaranteed to find a solution if one exists

### Visualization
- **Green cube**: Start position (0, 0, 0)
- **Red cube**: End position (max coordinates)
- **Gray cubes**: Walls
- **Blue line**: Solution path

## Controls

When the visualization window opens:
- **Click and drag**: Rotate the 3D view
- **Scroll wheel**: Zoom in/out
- **Close window**: Exit the program

## Customization

Edit these parameters in `main.py` to change maze size:

```python
maze = Maze3D(width=8, height=8, depth=4)
```

- `width`: X-axis size (default: 8)
- `height`: Y-axis size (default: 8)
- `depth`: Z-axis size/layers (default: 4)

**Note**: Larger mazes take longer to generate and may be harder to visualize.

## Project Structure

```
├── main.py          # Complete implementation
└── README.md        # This file
```

## Example Output

```
==================================================
3D MAZE GENERATOR AND SOLVER
==================================================

[1/4] Creating 3D maze structure...
[2/4] Generating maze using recursive backtracking...
✓ Maze generated successfully!
[3/4] Solving maze using BFS pathfinding...
✓ Solution found! Path length: 45 steps
[4/4] Generating 3D visualization...

Controls:
  - Click and drag to rotate the view
  - Scroll to zoom in/out
  - Green cube = Start
  - Red cube = End
  - Blue line = Solution path

Close the window to exit.
```

## Requirements

- Python 3.9+
- numpy
- matplotlib

## Troubleshooting

**Issue**: Import errors
- **Solution**: Make sure conda environment is activated: `conda activate maze3d`

**Issue**: Visualization doesn't show
- **Solution**: Ensure you have a display. If running on a server, use `export MPLBACKEND=Agg` but note this won't show interactive windows.

**Issue**: Maze generation is slow
- **Solution**: Reduce maze dimensions in the code

## License

Free to use and modify for educational purposes.

## Author

Created as a demonstration of 3D maze generation and pathfinding algorithms.