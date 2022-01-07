import time
import sys
import math
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]

def check_pandigital(x):
    x = str(x)
    combined = x
    if len(combined) < len(numbers):
        return False
    number = [str(i) for i in numbers]

    if len(set(combined)) != len(combined) or "0" in combined:
        return False
    for i in range(1, len(number) + 1):
        if str(i) not in combined:
            return False
    return True

def solve():
    res = []
    for i in range(2,10):
        com = ""
        print(i)
        for j in range(10000000,99999999):
            com = str(i) + str(j)
            if (check_pandigital(int(com))):
                res.append(int(com))

    return res

def main():
    t0 = time.time()
    ans = solve()
    print(ans,max(ans))

    print("time = ","\x1b[6;30;42m",time.time() - t0 , "\x1b[0m" )

if __name__ == "__main__":
    main()

