from collections import deque

def parse_obstacles(filepath):
    """Read obstacle file and return list of (N, E, S, W) tuples."""
    obstacles = []
    with open(filepath, 'r') as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            parts = list(map(int, line.split()))
            if len(parts) == 4:
                N, E, S, W = parts
                obstacles.append((N, E, S, W))
    return obstacles

def build_arena(obstacles, size=11):
    """
    Build n x n grid. 1 = safe, 0 = obstacle.
    
    Each obstacle (N, E, S, W) defines a rectangle:
      - N, S → row range: min(N,S) to max(N,S)
      - E, W → col range: min(E,W) to max(E,W)
    
    Start [0,0] and End [10,10] are always kept safe.
    """
    grid = [[1] * size for _ in range(size)]
    
    for (N, E, S, W) in obstacles:
        row_start = min(N, S)
        row_end   = max(N, S)
        col_start = min(E, W)
        col_end   = max(E, W)
        
        # Mark every cell in the rectangle as blocked
        for r in range(row_start, min(row_end + 1, size)):
            for c in range(col_start, min(col_end + 1, size)):
                grid[r][c] = 0
    
    # Guarantee start and end are never blocked
    grid[0][0] = 1
    grid[size-1][size-1] = 1
    return grid

def print_arena(grid):
    """Print the arena matrix with row and column indices."""
    size = len(grid)
    print("     " + "".join(f"{c:3}" for c in range(size)))  # column headers
    for r in range(size):
        row_str = "".join(f"  {grid[r][c]}" for c in range(size))
        print(f"{r:2}  |{row_str}")

def shortest_path(grid, start=(0, 0), end=(10, 10)):
    """
    BFS to find shortest path from start to end.
    Brick moves N/S/E/W only (no diagonals).
    Returns (path, steps) or (None, -1) if no path exists.
    """
    size = len(grid)
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # N, S, W, E
    
    queue = deque([(start, [start])])  # (current_position, path_so_far)
    visited = {start}
    
    while queue:
        (row, col), path = queue.popleft()
        
        # Reached destination
        if (row, col) == end:
            return path, len(path) - 1
        
        for dr, dc in directions:
            nr, nc = row + dr, col + dc
            # Check bounds, not visited, and not an obstacle
            if 0 <= nr < size and 0 <= nc < size:
                if (nr, nc) not in visited and grid[nr][nc] == 1:
                    visited.add((nr, nc))
                    queue.append(((nr, nc), path + [(nr, nc)]))
    
    return None, -1  # No path found

def print_path(grid, path):
    """
    Visualize path on the arena.
    S = Start, E = End, * = Path, 0 = Obstacle, . = Safe
    """
    size = len(grid)
    path_set = set(path)
    
    print("     " + "".join(f"{c:3}" for c in range(size)))  # column headers
    for r in range(size):
        row_chars = []
        for c in range(size):
            if (r, c) == path[0]:
                row_chars.append("  S")
            elif (r, c) == path[-1]:
                row_chars.append("  E")
            elif (r, c) in path_set:
                row_chars.append("  *")
            elif grid[r][c] == 0:
                row_chars.append("  0")
            else:
                row_chars.append("  .")
        print(f"{r:2}  |{''.join(row_chars)}")

def main():
    filepath = input("Enter file path: ").strip()
    
    obstacles = parse_obstacles(filepath)       # Step 1: Read obstacles
    grid = build_arena(obstacles, size=11)      # Step 2: Build 11x11 arena
    print_arena(grid)                           # Step 3: Print arena
    print()
    
    path, dist = shortest_path(grid)            # Step 4: shortest path
    if path:
        print(f"Shortest path: {dist} steps")
        print_path(grid, path)                  # Step 5: Visualize path
    else:
        print("No path found")

if __name__ == "__main__":
    main()