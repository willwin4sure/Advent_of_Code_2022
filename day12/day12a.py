with open("input12.txt", "r") as f:
    data = f.read().splitlines()

    data = [list(x) for x in data]

    for i in range(len(data)):
        for j in range(len(data[0])):
            if data[i][j] == 'S':
                start = (i, j)
                data[i][j] = 'a'
            if data[i][j] == 'E':
                end = (i, j)
                data[i][j] = 'z'
    
    q = []
    q.append((start, 0))
    visited = set()
    visited.add(start)
    while q:
        (x, y), steps = q.pop(0)
        if (x, y) == end:
            print(steps)
            break
        for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            nx, ny = x + dx, y + dy
            if 0 <= nx < len(data) and 0 <= ny < len(data[0]) and (nx, ny) not in visited and ord(data[nx][ny]) - ord(data[x][y]) <= 1:
                visited.add((nx, ny))
                q.append(((nx, ny), steps + 1))

