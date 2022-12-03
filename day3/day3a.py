with open("input3.txt", "r") as f:
    data = f.read().splitlines()

    alphabet = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"

    s = 0

    for line in data:
        n = len(line)

        for letter in alphabet:
            if (letter in line[:n//2]) and (letter in line[n//2:]):
                s += alphabet.index(letter)+1

    print(s)