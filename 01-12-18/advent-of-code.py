with open('input.txt', 'r') as file:
    numbers = []
    cache = []
    for line in file:
        next = eval(line)
        numbers.append(next)

    total = 0
    while True:
        for num in numbers:
            total += num
            if total in cache:
                print total
                exit(0)
            cache.append(total)
