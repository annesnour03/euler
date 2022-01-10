import time
import math
def calc_primes(max):
    max = int(max)
    primes = set()
    for i in range(2,max):
        if all(i % j != 0 for j in range(2,int(math.sqrt(i) + 1))):
            primes.add(i)
    return primes

def main():
    t0 = time.time()
    primes = calc_primes(2e6)
    print((list(primes)))
    t1=time.time()
    print("time = ","\x1b[6;30;42m",t1 - t0 , "\x1b[0m" )

if __name__ == "__main__":
    main()
