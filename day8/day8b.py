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

            if not (i == 0 or i == len(board)-1 or j == 0 or j == len(board[i])-1):
                scenic_scores = []

                num = 0
                for ii in range(i+1, len(board)):
                    num += 1
                    if board[ii][j] >= height:
                        break
                scenic_scores.append(num)

                num = 0
                for ii in range(i-1, -1, -1):
                    num += 1
                    if board[ii][j] >= height:
                        break
                        
                scenic_scores.append(num)

                num = 0

                for jj in range(j+1, len(board[i])):
                    num += 1
                    if board[i][jj] >= height:
                        break
                
                scenic_scores.append(num)

                num = 0
                for jj in range(j-1, -1, -1):
                    num += 1
                    if board[i][jj] >= height:
                        break
                        
                scenic_scores.append(num)

                scenic = 1
                for score in scenic_scores:
                    scenic *= score

                ans = max(scenic, ans)
    
    print(ans)