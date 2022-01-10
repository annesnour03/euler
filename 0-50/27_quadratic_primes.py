import time
import sys
import math


def isprime(x):
    for i in range(2, int(math.sqrt(abs(x))) + 1):
        if x % i == 0:
            return False
    return True


def solve(max_range):
    res = dict()
    max_streak = []
    all_res = []
    for i in range(-max_range + 1, max_range):
        print(i)
        for j in range(-max_range + 1, max_range + 1):
            streak = 0
            max_streak.clear()
            for n in range(0, 50):
                if(isprime(n*n + n * i + j)):
                    streak += 1
                    max_streak.append(streak)
                else:
                    streak = 0
            if max_streak == []:
                max_streak.append(0)
            tuple = (i, j, max(max_streak))
            all_res.append(tuple)
    return all_res


def main():
    t0 = time.time()
    max_range = 1000
    res = solve(max_range)

    print(max(res, key=lambda item: item[2]))
    t1 = time.time()

    print("time = ", "\x1b[6;30;42m", t1 - t0, "\x1b[0m")


if __name__ == "__main__":
    main()
