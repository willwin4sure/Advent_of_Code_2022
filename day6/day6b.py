with open("input6.txt", "r") as f:
    data = f.read().splitlines()

    last = []
    for i, c in enumerate(data[0]):
        if len(last) < 14:
            last.append(c)
        else:
            last.pop(0)
            last.append(c)
            
        if len(last) == 14:
            if len(set(last)) == 14:
                print(i+1)
                break