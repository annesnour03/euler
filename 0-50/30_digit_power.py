import time
import sys
import math
def solve(power):
    ans = set()
    for i in range(2 ,int(1e6)):
        string = list(str(i))
        string = [int(j) for j in string]
        for j in range(len(string)):
            temp = string
            temp = [temp[k] ** power for k in range(len(temp))]
            if (sum(temp) == i):
                ans.add(sum(temp))
    return ans


def main():
    t0 = time.time()
    ans = solve(5)
    print(ans,sum(ans))
    t1 = time.time()

    print("time = ","\x1b[6;30;42m",t1 - t0 , "\x1b[0m" )


if __name__ == "__main__":
    main()
