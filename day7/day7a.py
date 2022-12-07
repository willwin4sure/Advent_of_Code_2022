def dfs(tree, node, values, answers):
    if node not in tree:
        v = 0
        if node in values:
            v = values[node]
        answers[node] = v
        return answers[node]
    else:
        v = 0
        if node in values:
            v = values[node]
        answers[node] = v + sum(dfs(tree, child, values, answers) for child in tree[node])
        return answers[node]

with open("input7.txt", "r") as f:
    data = f.read().splitlines()

    tree = {}
    values = {}
    current_path = []
    for line in data:
        if "$" in line:
            if "cd" in line:
                if ".." in line:
                    current_path.pop()
                else:
                    current_path.append(line.split(" ")[2])

        else:
            if "dir" in line:
                if '/'.join(current_path) not in tree:
                    tree['/'.join(current_path)] = set()
                tree['/'.join(current_path)].add('/'.join(current_path) + '/' + line.split(" ")[1])

            else:
                if '/'.join(current_path) not in values:
                    values['/'.join(current_path)] = 0
                values['/'.join(current_path)] += int(line.split(" ")[0])

    answers = {}
    dfs(tree, "/", values, answers)
    
    ans = 0
    for v in answers.values():
        if v <= 100000:
            ans += v

    print(ans)
    
