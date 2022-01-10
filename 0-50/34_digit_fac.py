import time
import sys
import math

def split(num):
    num = list(str(num))
    num = [int(i) for i in num]
    return num
def solve():
    result = 0
    ans = set()
    for i in range(3,100000):
        spliced = split(i)
        for j in spliced:
            result = result + math.factorial(j)
        if(result == i):
            ans.add(i)
        result = 0
    return ans
    


def main():
    t0 = time.time()
    print(sum(solve()))
    print("time = ","\x1b[6;30;42m",time.time() - t0 , "\x1b[0m" )

if __name__ == "__main__":
    main()

