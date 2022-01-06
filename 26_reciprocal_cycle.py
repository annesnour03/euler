import time
import decimal

def keywithmaxval(d):
     v=list(d.values())
     k=list(d.keys())
     return k[v.index(max(v))]

def determine_recur(frac):
    for i in range(1,(len(frac))):
        s = frac[:i]
        ratio = (len(frac) // len(s))
        if ratio * s == frac:
            return int(s)
        else:
            for i in range(1,len(frac)):
                if ratio * s == frac[:i - 1]:
                    return int(s)
    return 0
def get_frac(n):
    return (decimal.Decimal(1) / decimal.Decimal(n))

def find_real_max(res,prec):
    for i in range(len(res)):
        if(res.get(keywithmaxval(res)) == (prec // 2) + 1):
            res.pop(keywithmaxval(res))
def main():
    prec = decimal.getcontext().prec = 2000
    res  = {}
    t0 = time.time()
    for i in range(1,1000):
        print(i)
        frac = get_frac(i)
        if (i <= 10):
            frac = str(frac)[2:]
        elif (i <= 100):
            frac = str(frac)[3:]
        else:
            frac =  str(frac)[4:]
        res[i] = len(str(determine_recur(frac)))

    for i in res:
        if i != 1:
            print(i, '\x1b[6;30;42m',res[i],'\x1b[0m',str(get_frac(i))[:10])

    res = find_real_max(res,prec)


    print(keywithmaxval(res))
    t1 = time.time()
    print("time = ", t1 - t0)


if __name__ == "__main__":
    main()
