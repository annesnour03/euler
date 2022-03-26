import time
import math as mt

def isprime(x):
    if(x % 2 == 0 or x < 2):
        return False
    for i in range(3, int(mt.sqrt(abs(x))) + 1, 2):
        if x % i == 0:
            return False
    return True

def solve(limit):
    i = 3
    nums, primes = 1,0
    while True:
        for j in range(1,4):
            if(isprime(i*i - j * i + j)):
                primes += 1
        nums +=4
        if(primes/nums < limit):
            return i
        i +=2



def main():
    t0 = time.time()
    ans = solve(0.10)
    print(ans) #1.8 s
    print("time = ", "\x1b[2;30;42m", time.time() - t0, "\x1b[0m")


if __name__ == "__main__":
    main()
