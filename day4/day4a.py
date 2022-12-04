with open("input4.txt", "r") as f:
    data = f.read().splitlines()

    s = 0

    for line in data:
        ranges = line.split(',')
        nums = []
        for r in ranges:
            nums.extend(r.split('-'))

        nums = list(map(int, nums))

        if (nums[2] >= nums[0] and nums[3] <= nums[1]) or (nums[0] >= nums[2] and nums[1] <= nums[3]):
            s += 1 

    print(s)