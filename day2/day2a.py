with open("input2.txt", "r") as f:
    data = f.read().splitlines()

    scores = {"A X":4, "B Y":5, "C Z":6, "A Y":8, "B Z":9, "C X":7, "A Z":3, "B X":1, "C Y":2}

    score = 0
    for line in data:
        score += scores[line]

    print(score)