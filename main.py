"""
3D Maze Generator and Solver
A procedurally generated 3D maze with pathfinding visualization
"""

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from mpl_toolkits.mplot3d.art3d import Poly3DCollection
from collections import deque
import random


class Maze3D:
    def __init__(self, width=10, height=10, depth=5):
        """Initialize 3D maze with given dimensions"""
        self.width = width
        self.height = height
        self.depth = depth
        # 1 = wall, 0 = path
        self.grid = np.ones((depth, height, width), dtype=int)
        self.start = (0, 0, 0)
        self.end = (depth - 1, height - 1, width - 1)
        
    def generate_maze(self):
        """Generate maze using recursive backtracking algorithm"""
        # Use odd dimensions to ensure proper maze generation
        stack = [self.start]
        self.grid[self.start] = 0
        visited_cells = {self.start}
        
        directions = [
            (0, -1, 0), (0, 1, 0),  # up, down
            (0, 0, -1), (0, 0, 1),  # left, right
            (-1, 0, 0), (1, 0, 0)   # back, forward
        ]
        
        while stack:
            z, y, x = stack[-1]
            neighbors = []
            
            for dz, dy, dx in directions:
                nz, ny, nx = z + dz * 2, y + dy * 2, x + dx * 2
                
                if (0 <= nz < self.depth and 
                    0 <= ny < self.height and 
                    0 <= nx < self.width and 
                    (nz, ny, nx) not in visited_cells):
                    neighbors.append((nz, ny, nx, dz, dy, dx))
            
            if neighbors:
                nz, ny, nx, dz, dy, dx = random.choice(neighbors)
                # Carve path
                self.grid[z + dz, y + dy, x + dx] = 0
                self.grid[nz, ny, nx] = 0
                visited_cells.add((nz, ny, nx))
                stack.append((nz, ny, nx))
            else:
                stack.pop()
        
        # Ensure start and end are open
        self.grid[self.start] = 0
        self.grid[self.end] = 0
        
        # Add some random openings to make maze more interesting
        for _ in range(min(5, (self.width * self.height * self.depth) // 20)):
            z = random.randint(0, self.depth - 1)
            y = random.randint(0, self.height - 1)
            x = random.randint(0, self.width - 1)
            self.grid[z, y, x] = 0
        
    def solve_maze(self):
        """Solve maze using BFS and return the path"""
        queue = deque([self.start])
        visited = {self.start}
        parent = {self.start: None}
        
        directions = [
            (0, -1, 0), (0, 1, 0),
            (0, 0, -1), (0, 0, 1),
            (-1, 0, 0), (1, 0, 0)
        ]
        
        while queue:
            z, y, x = queue.popleft()
            
            if (z, y, x) == self.end:
                # Reconstruct path
                path = []
                current = self.end
                while current is not None:
                    path.append(current)
                    current = parent[current]
                return path[::-1]
            
            for dz, dy, dx in directions:
                nz, ny, nx = z + dz, y + dy, x + dx
                
                if (0 <= nz < self.depth and 
                    0 <= ny < self.height and 
                    0 <= nx < self.width and 
                    self.grid[nz, ny, nx] == 0 and
                    (nz, ny, nx) not in visited):
                    visited.add((nz, ny, nx))
                    parent[(nz, ny, nx)] = (z, y, x)
                    queue.append((nz, ny, nx))
        
        return []  # No path found
    
    def visualize(self, path=None):
        """Visualize the 3D maze with optional solution path"""
        fig = plt.figure(figsize=(12, 10))
        ax = fig.add_subplot(111, projection='3d')
        
        # Draw walls as cubes
        for z in range(self.depth):
            for y in range(self.height):
                for x in range(self.width):
                    if self.grid[z, y, x] == 1:
                        self._draw_cube(ax, x, y, z, color='gray', alpha=0.3)
        
        # Draw start and end points
        self._draw_cube(ax, self.start[2], self.start[1], self.start[0], 
                       color='green', alpha=0.8)
        self._draw_cube(ax, self.end[2], self.end[1], self.end[0], 
                       color='red', alpha=0.8)
        
        # Draw solution path
        if path:
            path_array = np.array(path)
            ax.plot(path_array[:, 2] + 0.5, 
                   path_array[:, 1] + 0.5, 
                   path_array[:, 0] + 0.5,
                   'b-', linewidth=3, label='Solution Path')
        
        ax.set_xlabel('X')
        ax.set_ylabel('Y')
        ax.set_zlabel('Z (Depth)')
        ax.set_title('3D Maze - Green: Start, Red: End')
        ax.legend()
        
        # Set equal aspect ratio
        max_range = max(self.width, self.height, self.depth)
        ax.set_xlim([0, max_range])
        ax.set_ylim([0, max_range])
        ax.set_zlim([0, max_range])
        
        plt.tight_layout()
        plt.show()
    
    def _draw_cube(self, ax, x, y, z, color='blue', alpha=0.3):
        """Helper function to draw a cube at given position"""
        vertices = [
            [x, y, z], [x+1, y, z], [x+1, y+1, z], [x, y+1, z],
            [x, y, z+1], [x+1, y, z+1], [x+1, y+1, z+1], [x, y+1, z+1]
        ]
        
        faces = [
            [vertices[0], vertices[1], vertices[5], vertices[4]],
            [vertices[7], vertices[6], vertices[2], vertices[3]],
            [vertices[0], vertices[3], vertices[7], vertices[4]],
            [vertices[1], vertices[2], vertices[6], vertices[5]],
            [vertices[0], vertices[1], vertices[2], vertices[3]],
            [vertices[4], vertices[5], vertices[6], vertices[7]]
        ]
        
        ax.add_collection3d(Poly3DCollection(faces, facecolors=color, 
                                            linewidths=0.5, edgecolors='black', 
                                            alpha=alpha))


def main():
    """Main function to generate and solve maze"""
    print("=" * 50)
    print("3D MAZE GENERATOR AND SOLVER")
    print("=" * 50)
    
    # Create maze - keep generating until we find a solvable one
    print("\n[1/4] Creating 3D maze structure...")
    
    max_attempts = 10
    for attempt in range(1, max_attempts + 1):
        maze = Maze3D(width=9, height=9, depth=5)
        
        # Generate maze
        if attempt == 1:
            print("[2/4] Generating maze using recursive backtracking...")
        else:
            print(f"[2/4] Regenerating maze (attempt {attempt})...")
        
        maze.generate_maze()
        
        # Try to solve
        if attempt == 1:
            print("[3/4] Solving maze using BFS pathfinding...")
        
        path = maze.solve_maze()
        
        if path:
            print(f"✓ Maze generated and solved successfully!")
            print(f"✓ Solution found! Path length: {len(path)} steps")
            break
    else:
        print("✗ Could not generate a solvable maze after multiple attempts!")
        return
    
    # Visualize
    print("[4/4] Generating 3D visualization...")
    print("\nControls:")
    print("  - Click and drag to rotate the view")
    print("  - Scroll to zoom in/out")
    print("  - Green cube = Start")
    print("  - Red cube = End")
    print("  - Blue line = Solution path")
    print("\nClose the window to exit.")
    
    maze.visualize(path)
    
    print("\n" + "=" * 50)
    print("Demo completed!")
    print("=" * 50)


if __name__ == "__main__":
    main()