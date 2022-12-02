with open("input1.txt", "r") as f:
    data = f.read().splitlines()
    s = 0
    ss = []
    for d in data:
        if d == "":
            ss.append(s)
            s = 0
        else:
            s += int(d)
    ss.sort()
    print(ss[-1])
    print(ss[-1] + ss[-2] + ss[-3])