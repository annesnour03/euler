import time
import math
import sympy
import copy

def is_prime_proof(x):
    """
    Number is prime proof if you can't change a single digit to make it a prime.
    """
    x_list = list(str(x))
    length = len(x_list)
    for index in range(length):
        for i in range(0,10):
            new =copy.deepcopy(x_list)
            new[index] = str(i)
            if(index == length - 1 and new[index] in ["0","2","4","6","8"]):
                continue
            if(sympy.isprime(int(''.join(new)))):
                return False
    return True


def getPrimes():
    arr = []
    for i in range(num + 1):
        arr.append(True)

    for i in range(2, int(math.sqrt(num))+1):
        if arr[i]:
            j = i*i
            while j <= num:
                arr[j] = False
                j += i

    l = []
    for i in range(2, num+1):
        if arr[i]:
            l.append(i)

    return l


num = 50000
def get_squbes():
    primes = getPrimes()
    print("got primes")

    res = []
    # check for size of sqube, if > biggest prime
    for i in primes:
        for j in primes:
            if i != j:
                x = i**2 * j**3
                res.append(x)
            # if(len(res )>=200 and x>= max(res)):
                # return x
    return res
def solve():
    res = []
    sq = sorted(get_squbes())
    print("done sorting")
    for i in sq:

        if("200" in str(i) and is_prime_proof(i)):
            print(i)
            res.append(i)
            if(len(res) >= 200):
                break
    return res

def main():
    t0 = time.time()
    ans = sorted(list(set(solve())))
    print(ans, len(ans))
    if(len(ans) >= 200):
        print(ans[199])
    print("time = ", "\x1b[2;30;42m", time.time() - t0, "\x1b[0m")


if __name__ == "__main__":
    main()
