def print_grid(grid):
    for row in grid:
        print(' '.join(row))

def move(direction, i, j, grid, ypoints, xpoints):
    if direction == 'R' and j < n - 1:
        j += 1
    elif direction == 'L' and j > 0:
        j -= 1
    elif direction == 'B':
        i += 1
    grid[i][j] = '*'
    ypoints.append(i)
    xpoints.append(j)
    return i, j

def main():
    n = int(input())
    grid = [['.' for _ in range(n)] for _ in range(2)]
    ypoints = [0]
    xpoints = [0]

    grid[0][0] = '*'
    i, j = 0, 0

    directions = []
    direction = ''
    while direction != 'END':
        direction = input()
        if direction in {'R', 'L', 'B'}:
            i, j = move(direction, i, j, grid, ypoints, xpoints)
            directions.append(direction)

    h = len(directions)

    if h != ypoints.pop() or xpoints.pop() != n - 1:
        print('There\'s no way out!')
        return

    print_grid(grid)

if __name__ == "__main__":
    main()
