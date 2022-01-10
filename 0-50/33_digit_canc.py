import time
import sys
import math


def gcd(a, b):
    while a != b:
        if a > b:
            a -= b
        else:
            b -= a
    return a


def new(x, y):
    x = list(str(x))
    y = list(str(y))
    for i in range(len(min(x, y))):
        if x[i] in y:
            if x[i] == "0":
                continue
            y.remove(x[i])
            x.remove(x[i])
            break
    if not y or not x:
        return -1, -1
    x = [str(i) for i in x]
    temp = "".join(x)
    x = int(temp)

    y = [str(i) for i in y]
    temp = "".join(y)
    y = int(temp)
    return x, y


def solve():
    ans = set()
    for i in range(10, 100):
        for j in range(10, 100):
            if i >= j:
                continue
            f = i / j
            ogi = i
            ogj = j
            i, j = new(i, j)
            if j != 0 and i / j == f and i != ogi:
                ans.add((ogi, ogj))
            i = ogi
    return ans


def main():
    t0 = time.time()
    ans_set = list(solve())
    tellers = [] * 100
    noemers = [] * 100
    teller = 1
    noemer = 1
    for i in range(len(ans_set)):
        var = ans_set[i]
        teller, noemer = var
        tellers.append(teller)
        noemers.append(noemer)

    teller, noemer = 1, 1
    for i in range(len(tellers)):
        teller *= tellers[i]
        noemer *= noemers[i]
    print(noemer // gcd(teller, noemer))  # 38729600
    print("time = ", "\x1b[6;30;42m", time.time() - t0, "\x1b[0m")


if __name__ == "__main__":
    main()
