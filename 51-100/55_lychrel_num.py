import time


def ispalin(x):
    x = str(x)
    for i in range(len(x) // 2):
        c = 0
        if x[i] != x[len(x) - i - 1]:
            return False
        c += 1
        if c == len(x)//2:
            return True
    return True


def solve(range_limit, iterations):
    c = 0
    for i in range(range_limit + 1):
        a = i
        for j in range(iterations + 1):
            a += int(str(a)[::-1])
            if(ispalin(a)):
                c += 1
                break
    return c


def main():
    t0 = time.time()
    limit = 10000
    ans = solve(limit, 50)
    print("ans", limit - ans + 1)
    print("time = ", "\x1b[2;30;42m", time.time() - t0, "\x1b[0m")


if __name__ == "__main__":
    main()
