with open('input.txt', 'r') as file:
    ids = []
    for line in file:
        ids.append(line)

    for i in range(1, len(ids)):
        first  = ids[i-1]
        second = ids[i]
        difference_count = 0
        differences = []
        for chars in zip(first, second):
            if chars[0] != chars[1]:
                difference_count += 1
                differences.append(chars[0])
                differences.append(chars[1])
        if difference_count <= 1:
            print first, '\t', second
            print differences
