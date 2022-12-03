with open("input3.txt", "r") as f:
    data = f.read().splitlines()

    alphabet = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"

    s = 0

    for i in range(len(data)//3):
        for letter in alphabet:
            if (letter in data[3*i] and letter in data[3*i+1] and letter in data[3*i+2]):
                s += alphabet.index(letter)+1

    print(s)