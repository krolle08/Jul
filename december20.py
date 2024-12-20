from collections import deque  # Import deque for efficient queue operations

#Graphsøgning

def format_data():
    f = open('strings.txt', 'r')
    raw_data = f.read()
    f.close()
    listdata = [list(line) for line in raw_data.strip().split("\n")]    
    return listdata

def test ():
    findStartorEnd(listdata, "S")
    findStartorEnd(listdata, "E")

    findShortestpath(listdata, "S", "E")

    print("S")

def findStartorEnd(grid, char):
    for row in range(len(grid)):
          for col in range(len(grid[0])):
               if grid[row][col] == char:
                    print(f"Start {char} at row {row}, column {col}")
                    return row, col


def findShortestpath(grid, start, end):
    rows, cols = len(grid), len(grid[0])
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # right, down, left, up
    queue = deque([(start, 0)])  # ((row, col), distance)
    visited = set()
    visited.add(start)
    
    while queue:
        (x, y), dist = queue.popleft()
        
        # If we reach the end
        if (x, y) == end:
            return dist
        
        # Explore neighbors
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            
            if 0 <= nx < rows and 0 <= ny < cols and (nx, ny) not in visited:
                if grid[nx][ny] == '.' or grid[nx][ny] == 'E':
                    queue.append(((nx, ny), dist + 1))
                    visited.add((nx, ny))
    
    return -1  # No path found

def fastest_route():

    listdata = format_data()
    start = findStartorEnd(listdata, 'S')
    end = findStartorEnd(listdata, 'E')

    if start and end:
        shortest_path_length = findShortestpath(listdata, start, end)
        if shortest_path_length != -1:
            print(f"The shortest path from S to E is {shortest_path_length} steps.")
        else:
            print("No path exists from S to E.")
    else:
        print("Start (S) or End (E) not found in the grid.")
