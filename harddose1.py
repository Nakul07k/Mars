import os
from collections import deque

def parse_obstacles(filepath):
    obstacles = set()
    with open(filepath, 'r') as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            
            # Extract North, East, South, West distances
            n, e, s, w = map(int, line.split())
            
            # Logic: Start from opposite of direction which has 0 and draw the border
            if s == 0:
                y = n
                for x in range(-w, e + 1):
                    obstacles.add((x, y))
            elif n == 0:
                y = -s
                for x in range(-w, e + 1):
                    obstacles.add((x, y))
            elif w == 0:
                x = e
                for y in range(-s, n + 1):
                    obstacles.add((x, y))
            elif e == 0:
                x = -w
                for y in range(-s, n + 1):
                    obstacles.add((x, y))
                    
    return obstacles

def build_arena_and_find_path():
    filepath = input("Enter the path to the obstacle .txt file: ")
    
    if not os.path.exists(filepath):
        print(f"Error: The file '{filepath}' does not exist.")
        return

    obstacles = parse_obstacles(filepath)
    
    # Destination and Start points
    dest_x, dest_y = 10, 10
    start_x, start_y = 0, 0

    # Determine the boundaries of our grid
    obs_x = [pos[0] for pos in obstacles]
    obs_y = [pos[1] for pos in obstacles]
    
    min_x = min(start_x, dest_x, min(obs_x) if obs_x else 0)
    max_x = max(start_x, dest_x, max(obs_x) if obs_x else 10)
    min_y = min(start_y, dest_y, min(obs_y) if obs_y else 0)
    max_y = max(start_y, dest_y, max(obs_y) if obs_y else 10)

    # Make it an n x n square matrix
    width = max_x - min_x + 1
    height = max_y - min_y + 1
    n = max(width, height)
    
    # Adjust boundaries so the grid is perfectly n x n
    max_x = min_x + n - 1
    min_y = max_y - n + 1

    # Create the matrix (1 for safe, 0 for obstacle)
    matrix = [[1 for _ in range(n)] for _ in range(n)]
    
    for (x, y) in obstacles:
        # Mapping Cartesian (x,y) to Matrix (row, col)
        # row 0 is max_y, col 0 is min_x
        r = max_y - y
        c = x - min_x
        if 0 <= r < n and 0 <= c < n:
            matrix[r][c] = 0

    print(f"\n--- {n}x{n} Arena Matrix ---")
    for row in matrix:
        print(" ".join(str(cell) for cell in row))

    # Bonus Task: Shortest Path using BFS
    start_r = max_y - start_y
    start_c = start_x - min_x
    dest_r = max_y - dest_y
    dest_c = dest_x - min_x

    # Queue stores: (row, col, path_taken)
    queue = deque([(start_r, start_c, [(start_x, start_y)])])
    visited = set()
    visited.add((start_r, start_c))

    shortest_path = None

    while queue:
        r, c, path = queue.popleft()

        if r == dest_r and c == dest_c:
            shortest_path = path
            break

        # Move like a King, but NO diagonals (Up, Down, Left, Right)
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        for dr, dc in directions:
            nr, nc = r + dr, c + dc
            
            # Check bounds and safety
            if 0 <= nr < n and 0 <= nc < n:
                if matrix[nr][nc] == 1 and (nr, nc) not in visited:
                    visited.add((nr, nc))
                    
                    # Convert matrix row/col back to cartesian x/y for the path log
                    nx = nc + min_x
                    ny = max_y - nr
                    
                    queue.append((nr, nc, path + [(nx, ny)]))

    print("\n--- Mission Report ---")
    if shortest_path:
        print("Status: Destination Reachable!")
        print(f"Total Steps: {len(shortest_path) - 1} meters")
        print("Shortest Path (x, y):")
        
        path_str = " -> ".join([f"[{px},{py}]" for px, py in shortest_path])
        print(path_str)
    else:
        print("Status: FAILED. No safe path to the destination avoiding obstacles.")

if __name__ == "__main__":
    build_arena_and_find_path()