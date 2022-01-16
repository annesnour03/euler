import time


def solve():
    i = 3
    while True:
        res = set()
        for j in range(1, 7):
            outcome = sorted(str(i * j))
            outcome = "".join(outcome)
            res.add(outcome)
            if(len(res) > 1):
                break
        if(len(res) == 1):
            break
        i += 3
    return i


def main():
    t0 = time.time()
    ans = solve()
    print(ans) # 0.05 s
    print("time = ", "\x1b[2;30;42m", time.time() - t0, "\x1b[0m")


if __name__ == "__main__":
    main()
