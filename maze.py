from collections import deque

class Maze:
    def __init__(self, grid):
        self.grid = grid
        self.rows = len(grid)
        self.cols = len(grid[0])

    def get_neighbors(self, r, c):
        directions = [(1,0), (-1,0), (0,1), (0,-1)]
        neighbors = []

        for dr, dc in directions:
            nr, nc = r + dr, c + dc
            if 0 <= nr < self.rows and 0 <= nc < self.cols:
                if self.grid[nr][nc] != 1:  # not a wall
                    neighbors.append((nr, nc))

        return neighbors

    def bfs(self, start, goal):
        queue = deque([start])
        visited = set([start])
        parent = {}

        while queue:
            node = queue.popleft()

            if node == goal:
                return self.reconstruct_path(parent, start, goal)

            for neighbor in self.get_neighbors(*node):
                if neighbor not in visited:
                    visited.add(neighbor)
                    parent[neighbor] = node
                    queue.append(neighbor)

        return []

    def dfs(self, start, goal):
        stack = [start]
        visited = set([start])
        parent = {}

        while stack:
            node = stack.pop()

            if node == goal:
                return self.reconstruct_path(parent, start, goal)

            for neighbor in reversed(self.get_neighbors(*node)):
                if neighbor not in visited:
                    visited.add(neighbor)
                    parent[neighbor] = node
                    stack.append(neighbor)

        return []

    def reconstruct_path(self, parent, start, goal):
        path = []
        curr = goal

        while curr != start:
            path.append(curr)
            curr = parent[curr]

        path.append(start)
        path.reverse()
        return path

import random

def generate_random_maze(rows=10, cols=10):
    grid = [[0 for _ in range(cols)] for _ in range(rows)]

    # Add random walls
    for i in range(rows):
        for j in range(cols):
            if random.random() < 0.3:  # 30% walls
                grid[i][j] = 1

    # Ensure start and goal are open
    grid[0][0] = 0
    grid[rows-1][cols-1] = 0

    return grid