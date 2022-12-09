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

def update(h1, h2, t1, t2):
    if adjacent((h1, h2),(t1, t2)):
        return t1, t2
    elif two_away((h1, h2),(t1, t2)):
        return int((t1 + h1)/2), int((t2 + h2)/2)
    else:
        if abs(t1 - h1) == 1:
            return h1, int((t2 + h2)/2)
        elif abs(t2 - h2) == 1:
            return int((t1 + h1)/2), h2
        else:
            return int((t1 + h1)/2), int((t2 + h2)/2)

with open("input9.txt", "r") as f:
    data = f.read().splitlines()

    N = 1000

    grid = [['.' for i in range(N)] for j in range(N)]

    rope = [[N//2,N//2] for i in range(10)]

    grid[N//2][N//2] = '#'

    # for i in range(10):
    #     print(rope[i], end='')
    # print("--------------------------------")

    for line in data:
        instr = line.split(' ')
        delta = [0,0]
        if instr[0] == 'U':
            delta[0] = -1
        elif instr[0] == 'D':
            delta[0] = 1
        elif instr[0] == 'L':
            delta[1] = -1
        else:
            delta[1] = 1

        for i in range(int(instr[1])):
            rope[0][0] += delta[0]
            rope[0][1] += delta[1]

            for i in range(1,10):
                rope[i][0], rope[i][1] = update(rope[i-1][0], rope[i-1][1], rope[i][0], rope[i][1])

            grid[rope[10-1][0]][rope[10-1][1]] = '#'
        
        # for i in range(N):
        #     for j in range(N):
        #         print(grid[i][j], end='')
        #     print()
        # input()

        # for i in range(2):
        #     print(rope[i], end='')
        # input("--------------------------------")
                
    num = 0
    
    for i in range(N):
        for j in range(N):
            if grid[i][j] == '#':
                num += 1

    print(num)
