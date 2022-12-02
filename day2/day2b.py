with open("input2.txt", "r") as f:
    data = f.read().splitlines()

    scores = {"A X":3, "B X":1, "C X":2, "A Y":4, "B Y":5, "C Y":6, "A Z":8, "B Z":9, "C Z":7}

    score = 0
    for line in data:
        score += scores[line]

    print(score)