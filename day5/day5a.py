with open("input5.txt", "r") as f:
    data = f.read().splitlines()

    #     [C]             [L]         [T]
    #     [V] [R] [M]     [T]         [B]
    #     [F] [G] [H] [Q] [Q]         [H]
    #     [W] [L] [P] [V] [M] [V]     [F]
    #     [P] [C] [W] [S] [Z] [B] [S] [P]
    # [G] [R] [M] [B] [F] [J] [S] [Z] [D]
    # [J] [L] [P] [F] [C] [H] [F] [J] [C]
    # [Z] [Q] [F] [L] [G] [W] [H] [F] [M]
    #  1   2   3   4   5   6   7   8   9 

    boxes = {1: 'ZJG', 2:'QLRPWFVC', 3:'FPMCLGR', 4:'LFBWPHM', 5:'GCFSVQ', 6: 'WHJZMQTL', 7: 'HFSBV', 8: 'FJZS', 9: 'MCDPFHBT'}

    for i in range(1, 10):
        boxes[i] = list(boxes[i])
    
    for line in data:
        l = line.split(' ')
        amt = int(l[1])
        f = int(l[3])
        t = int(l[5])

        for _ in range(amt):
            if len(boxes[f]) > 0:
                m = boxes[f][-1]
                boxes[f].pop()
                boxes[t].append(m)
            else:
                break

    for i in range(1,10):
        print(boxes[i][-1], end='')
