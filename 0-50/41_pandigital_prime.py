import time
import math

def check_pandigital(x,numbers):
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

def isprime(x):
    if(x % 2 == 0):
        return False
    for i in range(3, int(math.sqrt(abs(x))) + 1,2):
        if x % i == 0:
            return False
    return True


def solve():
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    # 8 and 9 digit pandigitals' sum add up to 36 and 45 --> %3 == 0, so skipped.
    for i in range(7654321,1,-2):
        length = int(math.log10(i)) + 1
        if(check_pandigital(i, numbers[:length]) and isprime(i)):
            return i



def main():
    t0 = time.time()
    ans = solve()
    print(ans)
    print("time = ","\x1b[6;30;42m",time.time() - t0 , "\x1b[0m" )

if __name__ == "__main__":
    main()

