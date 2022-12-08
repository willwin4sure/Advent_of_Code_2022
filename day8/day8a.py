with open("input8.txt", "r") as f:
    data = f.read().splitlines()

    board = []

    for line in data:
        row = []
        for c in line:
            row.append(c)
        board.append(list(map(int, row)))

    ans = 0

    for i in range(len(board)):
        for j in range(len(board[i])):
            # check in all four cardinal directions outward
            height = board[i][j]
            visible = False

            if i == 0 or i == len(board)-1 or j == 0 or j == len(board[i])-1:
                visible = True

            bad = False
            for ii in range(i+1, len(board)):
                if board[ii][j] >= height:
                    bad = True

            if not bad:
                visible = True

            bad = False
            for ii in range(i-1, -1, -1):
                if board[ii][j] >= height:
                    bad = True

            if not bad:
                visible = True

            bad = False
            for jj in range(j+1, len(board[i])):
                if board[i][jj] >= height:
                    bad = True

            if not bad:
                visible = True

            bad = False
            for jj in range(j-1, -1, -1):
                if board[i][jj] >= height:
                    bad = True
                    
            if not bad:
                visible = True

            if visible:
                ans += 1
    
    print(ans)