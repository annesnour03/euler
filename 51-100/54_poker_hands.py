import time
from collections import Counter

# Spades, Diamonds, hearts, clover (S,D,H,C) 10 = T

SCORES = [0, 0, 2, 3, 4, 5, 6, 7, 8, 9, "T", "J", "Q", "K", "A"]
FULL_SCORES = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]


class poker:
    def __init__(self, hand):
        self.hand = hand

    def dis(self):
        print(self.hand)

    def extract_num(self):
        numbers = []
        for i in self.hand:
            if i[0] in SCORES:
                numbers.append(SCORES.index(i[0]))
            elif (int(i[0]) in SCORES):
                numbers.append(int(i[0]))
        return numbers

    def extract_type(self):
        types = []
        for i in self.hand:
            types.append((i[1]))
        return types

    def highest(self, values):
        filtered = filter(Counter(values), 1)
        if filtered != {}:
            return max(filtered)
        return max(values)

    def royal_flush(self, values):
        for i in range(10, 15):
            if i not in values:
                return False
        return True

    def flush(self, types):
        return len(Counter(types)) == 1

    def straight(self, values, increment):
        return sorted(values) in increment

    def straight_flush(self, values, increment, types):
        return sorted(values) in increment and len(Counter(types)) == 1

    def fullhouse(self, values):
        return check_kind(values, 3) and check_pairs(values) == 1


def check_pairs(values):
    score = 0
    for i in range(len(FULL_SCORES) + 2):
        c = Counter(values)[i]
        if(c % 2 == 0 and c != 4):
            score = score + (c // 2)
    return score

# Calculate overlapping
def check_kind(values, occur):
    for i in range(len(FULL_SCORES) + 2):
        if(Counter(values)[i] == occur):
            return True


# Generate a set that only includes incrementing sets [3,4,5,6,7],[2,3,4,5,6]
def increment_set(s, limit):
    master = []
    for i in range(len(s) - limit + 1):
        res = []
        for j in range(limit):
            res.append(s[i + j])
        master.append(res)
    return master


def filter(c, limit):
    for key, cnts in list(c.items()):
        if cnts > limit:
            del c[key]
    return c


def get_score(hand):
    increment = list(increment_set(FULL_SCORES, 5))

    p = poker(hand)
    nums = p.extract_num()
    types = p.extract_type()
    score = [0 for i in range(10)]
    pairs = check_pairs(nums)
    score[0] = p.highest(nums)

    if(pairs == 1):
        score[1] = list(Counter(nums).most_common())[0][0]
    if(pairs == 2):
        c = filter(Counter(nums), 2)
        score[2] = max(c)

    if(check_kind(nums, 3)):
        c = Counter(nums)
        score[3] = max(filter(c, 3))

    if(p.straight(nums, increment)):
        score[4] = max(nums)
        if(p.straight_flush(nums, increment, types)):
            score[8] = max(nums)

    if(p.flush(types)):
        score[5] = max(nums)
        if(p.royal_flush(nums)):
            score[8] = max(nums)

    if(p.fullhouse(nums)):
        score[6] = list(Counter(nums).most_common())[0][0]
    if(check_kind(nums, 4)):
        score[7] = list(Counter(nums).most_common())[0][0]

    return score


def solve():
    hands = list((line.split() for line in open('54_input.txt', 'r')))
    p1_wins = 0
    for i in range(1000):
        score_p1 = get_score(hands[i][:5])
        score_p2 = get_score(hands[i][5:])
        for j in range(9, -1, -1):
            if(score_p1[j] > score_p2[j]):
                p1_wins += 1
                break
            elif(score_p2[j] != score_p1[j]):
                break
    return p1_wins


def main():
    t0 = time.time()

    ans = solve()
    print(ans)
    print("time = ", "\x1b[6;30;42m", time.time() - t0, "\x1b[0m")


if __name__ == "__main__":
    main()