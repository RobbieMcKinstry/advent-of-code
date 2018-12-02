with open('input.txt', 'r') as file:
    ids = []
    for line in file:
        ids.append(line.strip())

    for index, first in enumerate(ids):
        for second in ids[index+1:]:
            difference_count = 0
            differences = []
            for i, chars in enumerate(zip(first, second)):
                if chars[0] != chars[1]:
                    difference_count += 1
                    differences.append(i)
            if difference_count <= 1:
                print first[:differences[0]] + first[differences[0]+1:]
