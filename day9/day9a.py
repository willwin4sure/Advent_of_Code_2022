def adjacent(x, y):
    if abs(x[0] - y[0]) <= 1 and abs(x[1] - y[1]) <= 1:
        return True
    return False
    
def two_away(x, y):
    if x[0] == y[0] and abs(x[1] - y[1]) == 2:
        return True
    if x[1] == y[1] and abs(x[0] - y[0]) == 2:
        return True
    return False

with open("input9.txt", "r") as f:
    data = f.read().splitlines()

    N = 1000

    grid = [['.' for i in range(N)] for j in range(N)]

    h = (0,0)
    t = (0,0)

    grid[0][0] = '#'

    for line in data:
        instr = line.split(' ')
        if instr[0] == 'U':
            for i in range(int(instr[1])):
                h = (h[0]+1, h[1])

                if adjacent(h,t):
                    continue
                elif two_away(h,t):
                    t = (int((t[0] + h[0])/2), int((t[1] + h[1])/2))
                    grid[t[0]][t[1]] = '#'
                else:
                    if abs(t[0] - h[0]) == 1:
                        t = (h[0], int((t[1] + h[1])/2))
                        grid[t[0]][t[1]] = '#'
                    else:
                        t = (int((t[0] + h[0])/2), h[1])
                        grid[t[0]][t[1]] = '#'

        elif instr[0] == 'D':
            for i in range(int(instr[1])):
                h = (h[0]-1, h[1])

                if adjacent(h,t):
                    continue
                elif two_away(h,t):
                    t = (int((t[0] + h[0])/2), int((t[1] + h[1])/2))
                    grid[t[0]][t[1]] = '#'
                else:
                    if abs(t[0] - h[0]) == 1:
                        t = (h[0], int((t[1] + h[1])/2))
                        grid[t[0]][t[1]] = '#'
                    else:
                        t = (int((t[0] + h[0])/2), h[1])
                        grid[t[0]][t[1]] = '#'    
            
        elif instr[0] == 'L':
            for i in range(int(instr[1])):
                h = (h[0], h[1]-1)

                if adjacent(h,t):
                    continue
                elif two_away(h,t):
                    t = (int((t[0] + h[0])/2), int((t[1] + h[1])/2))
                    grid[t[0]][t[1]] = '#'
                else:
                    if abs(t[0] - h[0]) == 1:
                        t = (h[0], int((t[1] + h[1])/2))
                        grid[t[0]][t[1]] = '#'
                    else:
                        t = (int((t[0] + h[0])/2), h[1])
                        grid[t[0]][t[1]] = '#'

        else:
            for i in range(int(instr[1])):
                h = (h[0], h[1]+1)

                if adjacent(h,t):
                    continue
                elif two_away(h,t):
                    t = (int((t[0] + h[0])/2), int((t[1] + h[1])/2))
                    grid[t[0]][t[1]] = '#'
                else:
                    if abs(t[0] - h[0]) == 1:
                        t = (h[0], int((t[1] + h[1])/2))
                        grid[t[0]][t[1]] = '#'
                    else:
                        t = (int((t[0] + h[0])/2), h[1])
                        grid[t[0]][t[1]] = '#'

    num = 0
    
    for i in range(N):
        for j in range(N):
            if grid[i][j] == '#':
                num += 1

    print(num)
