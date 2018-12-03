uncut = 'UNCUT'
cut_once = 'CUT_ONCE'
overlapped = 'OVERLAPPED'

class Claim:
    def __init__(self, identifier, left_offset, top_offset, width, height):
        self.identifier = identifier
        self.left_offset = left_offset
        self.top_offset = top_offset
        self.width = width
        self.height = height

def puzzle1():
    claims = get_claims()
    cloth = get_cloth()
    for claim in claims:
        cut_claim(cloth, claim)
    count = count_overlapped(cloth)
    print count

def cut_claim(cloth, claim):
    for i in range(claim.left_offset, claim.left_offset+claim.width):
        for j in range(claim.top_offset, claim.top_offset+claim.height):
            if cloth[i][j] == uncut:
                cloth[i][j] = cut_once
            elif cloth[i][j] == cut_once:
                cloth[i][j] = overlapped

def count_overlapped(cloth):
    count = 0
    for row in cloth:
        for val in row:
            if val == overlapped:
                count += 1
    return count

def puzzle2():
    claims = get_claims()
    for index, claim_under_test in enumerate(claims):
        overlapped = False
        print 'Attempt Claim #', claim_under_test.identifier
        for opposition in (claims[:index] + claims[index+1:]) :
            cloth = get_cloth()
            cut_claim(cloth, claim_under_test)
            cut_claim(cloth, opposition)
            if count_overlapped(cloth) > 0:
                overlapped = True
                break
            
        if not overlapped:
            print claim_under_test.identifier
            return


def main():
    puzzle1()
    puzzle2()

def get_cloth():
    cloth = []
    for i in range(1000):
        row = 1000 * [uncut]
        cloth.append(row)
    return cloth

def get_claims():
    claims = []
    with open('input.txt', 'r') as file:
        for line in file:
            first_space = line.index(' ')
            comma = line.index(',')
            colon = line.index(':')
            ex = line.index('x')

            identifier = int(line[1:first_space])
            left_offset = int(line[first_space+3:comma])
            top_offset = int(line[comma+1:colon])
            width =  int(line[colon+2: ex])
            height = int(line[ex+1:])
            next_claim = Claim(identifier, left_offset, top_offset, width, height)
            claims.append(next_claim)
    return claims

if __name__ == '__main__':
    main()
