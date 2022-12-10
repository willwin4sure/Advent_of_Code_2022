with open("input10.txt", "r") as f:
    data = f.read().splitlines()

    cycle = 0
    x = 1
    updates = {}
    signals = [20,60,100,140,180,220]
    ans = 0
    for line in data:
        if cycle in updates:
            x += updates[cycle]
        if "addx" in line:
            updates[cycle+2] = int(line.split(" ")[1])
            cycle += 1
            if cycle in signals:
                ans += cycle * x

            cycle += 1            
        else:
            cycle += 1
        
        if cycle in signals:
            ans += cycle * x

    print(ans)


        