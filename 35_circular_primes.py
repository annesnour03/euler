import time
import sys
import math


def isprime(x):
    for i in range(2, int(math.sqrt(x)) + 1):
        if x % i == 0:
            return False
    return True


def rotate(x):
    x = list(str(x))
    x.insert(0, x.pop(-1))
    x = int("".join(x))
    return x


def solve():
    length = 0
    ans = [2]
    counter = 1
    for i in range(3,int(1e6),2):
        x = i
        c = 0
        length = int(math.log10(i)) + 1
        for j in range(length):
            if(isprime(x) != True):
                break
            x = rotate(x)
            c +=1
            if(c == length and isprime(x) ==  True):
                ans.append(i)
                counter+=1
    return ans,counter




def main():
    t0 = time.time()
    print(solve()) #2.3sec
    print("time = ", "\x1b[6;30;42m", time.time() - t0, "\x1b[0m")


if __name__ == "__main__":
    main()
