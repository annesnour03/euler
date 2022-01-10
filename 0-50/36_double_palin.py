import time
import sys
import math
def tobinary(x):
    result = list()
    while x > 0:
        if( x % 2 == 0):
            result.insert(0,"0")
        else:
            result.insert(0,"1")
        x = x // 2
    result = int("".join(result))
    return result

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


def solve(max):
    res = []
    for i in range(1,max,2):
        if(ispalin(i) and ispalin(tobinary(i))):
            res.append(i)
    return res

def main():
    t0 = time.time()
    ans = solve(int(1e6))
    print(ans,sum(ans)) #0.15 sec
    print("time = ","\x1b[6;30;42m",time.time() - t0 , "\x1b[0m" )

if __name__ == "__main__":
    main()

