with open('input.txt', 'r') as file:
    ids = []
    for line in file:
        ids.append(line)

    count_of_2s = 0
    count_of_3s = 0

    for id in ids:
        contains_2 = False
        contains_3 = False
        for char in id:
            if id.count(char) == 2:
                contains_2 = True
            if id.count(char) == 3:
                contains_3 = True

        if contains_2:
            count_of_2s += 1
        if contains_3:
            count_of_3s += 1

    print count_of_2s * count_of_3s
