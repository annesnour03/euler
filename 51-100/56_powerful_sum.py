import time

def solve(limit):
    digital_sum = lambda x: sum([int(i) for i in str(x)])
    largest = 0
    for a in range(limit):
        for b in range(limit):
            total_sum = digital_sum(a ** b)
            if( total_sum > largest):
                largest = total_sum
    return largest



def main():
    t0 = time.time()
    ans = solve(100)
    print(ans)
    print("time = ", "\x1b[2;30;42m", time.time() - t0, "\x1b[0m")


if __name__ == "__main__":
    main()
