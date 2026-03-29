import matplotlib.pyplot as plt
import numpy as np

def visualize_comparison(grid, bfs_path, dfs_path):
    grid = np.array(grid)
    rows, cols = grid.shape

    fig, axes = plt.subplots(1, 2, figsize=(14, 7))
    fig.patch.set_facecolor('white')

    # Modern clean colors
    cmap = plt.cm.colors.ListedColormap([
            '#e6f2ff',  # light blue background
            '#1a1a1a',  # walls
            '#00cc66'   # path
        ])

    titles = ["BFS (Shortest Path)", "DFS (Not Optimal)"]
    paths = [bfs_path, dfs_path]

    max_steps = max(len(bfs_path), len(dfs_path))

    for step in range(max_steps):
        for ax, path, title in zip(axes, paths, titles):
            display = grid.copy()

            # draw path gradually
            if step < len(path):
                for i in range(step + 1):
                    r, c = path[i]
                    display[r][c] = 2
            else:
                for r, c in path:
                    display[r][c] = 2

            ax.clear()
            ax.set_facecolor('white')

            ax.imshow(display, cmap=cmap)

            # grid styling
            ax.set_xticks(np.arange(-0.5, cols, 1))
            ax.set_yticks(np.arange(-0.5, rows, 1))
            ax.grid(color="#000000", linewidth=0.5)

            ax.set_xticklabels([])
            ax.set_yticklabels([])

            # Start & Goal markers
            if path:
                start = path[0]
                goal = path[-1]

                ax.scatter(start[1], start[0], color='#ef4444', s=120, label='Start')  # red
                ax.scatter(goal[1], goal[0], color='#3b82f6', s=120, label='Goal')   # blue

            ax.set_title(f"{title}\nSteps: {len(path)}", fontsize=13, fontweight='bold', color='#111827')

        plt.pause(0.25)

    # ---- Add Legend (only once) ----
    handles = [
        plt.Line2D([0], [0], marker='s', color='w', label='Wall',
                   markerfacecolor='#1a1a1a', markersize=12),
        plt.Line2D([0], [0], marker='s', color='w', label='Path',
                   markerfacecolor='#22c55e', markersize=12),
        plt.Line2D([0], [0], marker='o', color='w', label='Start',
                   markerfacecolor='#ef4444', markersize=10),
        plt.Line2D([0], [0], marker='o', color='w', label='Goal',
                   markerfacecolor='#3b82f6', markersize=10)
    ]

    fig.legend(handles=handles, loc='lower center', ncol=4, frameon=False, fontsize=11)

    # ---- Main title ----
    fig.suptitle("Maze Solver: BFS vs DFS Comparison", fontsize=16, fontweight='bold')

    plt.tight_layout(rect=[0, 0.05, 1, 0.95])
    plt.show()