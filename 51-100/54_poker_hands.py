from inspect import getsource
import time
from collections import Counter

# Spades, Diamonds, hearts, clover (S,D,H,C) 10 = T

# Two Pairs: Two different pairs.
# Full House: Three of a kind and a pair.

SCORES = [0, 0, 2, 3, 4, 5, 6, 7, 8, 9]
SCORES_PIC = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, "T", "J", "Q", "K", "A"]
FULL_SCORES = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]


class poker:
    def __init__(self, hand):
        self.hand = hand

    def dis(self):
        print(self.hand)

    def extract_num(self):
        numbers = []
        for i in self.hand:
            if i[0] in SCORES_PIC:
                numbers.append(SCORES_PIC.index(i[0]))
            elif (int(i[0]) in SCORES):
                numbers.append(int(i[0]))
        return numbers

    def extract_type(self):
        types = []
        for i in self.hand:
            types.append((i[1]))
        return types

    def highest(self, values):
        filtered = filter2(Counter(values), 1)
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

    def fullhouse(self, values, types):
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
    print(values,occur)
    for i in range(len(FULL_SCORES) + 2):
        if(Counter(values)[i] == occur):
            return True


def increment_set(s, limit):
    master = []
    for i in range(len(s) - limit + 1):
        res = []
        for j in range(limit):
            res.append(s[i + j])
        master.append(res)
    return master

def filter(c,limit):
    for key, cnts in list(c.items()):
        if cnts != limit:
            del c[key]
    return c

def filter2(c,limit):
    for key, cnts in list(c.items()):
        if cnts > limit:
            del c[key]
    return c

def get_score(hand1):
    increment = list(increment_set(FULL_SCORES, 5))

    p1 = poker(hand1)
    nums = p1.extract_num()
    types = p1.extract_type()
    score = [0 for i in range(10)]
    for i in range(1):
        pairs = check_pairs(nums)
        score[0] =p1.highest(nums)
        if(pairs == 1):
            print("one pair ✅")
            score[1] = list(Counter(nums).most_common())[0][0]
        else:
            print("one pair ❌")
        if(pairs == 2):
            print("two pair ✅")
            c = filter(Counter(nums),2)
            score[2] = max(c)
        else:
            print("two pair ❌")

        if(check_kind(nums, 3)):
            print("three of a kind ✅")
            c = Counter(nums)
            score[3] = max(filter(c,3))
        else:
            print("three of a kind ❌")

        if(p1.straight(nums, increment)):
            print("straight ✅")
            score[4] = max(nums)
        else:
            print("straight ❌")

        if(p1.flush(types)):
            print("flush ✅")
            score[5] = max(nums)
        else:
            print("flush ❌")

        if(p1.fullhouse(nums, types)):
            print("full house ✅")
            score[6] = list(Counter(nums).most_common())[0][0]
        else:
            print("full house ❌")
        if(check_kind(nums, 4)):
            print("four of a kind ✅")
            score[7] = list(Counter(nums).most_common())[0][0]
        else:
            print("four of a kind ❌")

        if(p1.straight_flush(nums, increment, types)):
            print("straight flush ✅")
            score[8] = max(nums)

        else:
            print("straight flush ❌")

        if(p1.royal_flush(nums)):
            print("royal flush ✅")
            score[8] = max(nums)
        else:
            print("royal flush ❌")


    return score

def solve():
    file = (open('54_input.txt', 'r'))
    p1_wins = 0
    for i in range(1000):
        hands = list(file.readline().split())
        score_p1 = get_score(hands[:5])
        score_p2 = get_score(hands[5:])
        print(score_p1,score_p2)
        for j in range(9,-1,-1):
            print(score_p1[j],score_p2[j])
            if(score_p1[j] >  score_p2[j]):
                p1_wins += 1
                print("p1 win")
                break
            elif(score_p2[j] != score_p1[j]):
                print("p2 wins")
                break
    return p1_wins


def main():
    t0 = time.time()

    ans = solve()
    print(ans)
    print("time = ", "\x1b[6;30;42m", time.time() - t0, "\x1b[0m")


if __name__ == "__main__":
    main()

# 5H 5C 6S 7S KD 2C 3S 8S 8D TD
# 5D 8C 9S JS AC 2C 5C 7D 8S QH
# 2D 9C AS AH AC 3D 6D 7D TD QD
# 4D 6S 9H QH QC 3D 6D 7H QD QS
# 2H 2D 4C 4D 4S 3C 3D 3S 9S 9D
