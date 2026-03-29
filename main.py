from maze import Maze, generate_random_maze
from visualizer import visualize_comparison

def main():
    start = (0, 0)
    goal = (9, 9)

    while True:
        grid = generate_random_maze(10, 10)
        maze = Maze(grid)
        bfs_path = maze.bfs(start, goal)

        if bfs_path:  # path exists
            break
    dfs_path = maze.dfs(start, goal)

    print("BFS Path:", bfs_path)
    print("DFS Path:", dfs_path)

    print("BFS length:", len(bfs_path))
    print("DFS length:", len(dfs_path))

    visualize_comparison(grid, bfs_path, dfs_path)

if __name__ == "__main__":
    main()