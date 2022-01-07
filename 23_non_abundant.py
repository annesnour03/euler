import time

max_range = 28123
def divisors(x):
    res  = []
    for i in range(1,x):
        if (x % i) == 0:
            res.append(i)
    return res

def subset(abundant):
    r =  set()
    final = set()
    for i in abundant:
        for j in abundant:
            if(i + j > max_range):
                break
            else:
                r.add(i + j)
    final = [int (p) for p in range(1,max_range) if p not in r]
    return final

def main():
    t0 = time.time()
    abundant = []
    for i in range(1,max_range):
        if(sum(divisors(i)) > i):
            abundant.append(i)
    print((abundant))
    print(sum(subset(abundant)))
    t1 = time.time()
    print("time = ",t1-t0)
if __name__ == "__main__":
    main()