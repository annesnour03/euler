import time

def get_next(i):
    if i % 2 == 0:
        return int(i/2)
    else:
        return int(i* 3 +1)

def get_len(i):
    i,init = int(i),int(i)
    c = 1
    while(i != 1):
        i = get_next(i)
        if(i < init) and not i%2: break
        c += 1
    return c

def main():
    t0 = time.time()
    max_v =  {}
    for i in range(1,1000000):
        max_v[i] = get_len(i)

    print(list(max_v)[list(max_v.values()).index(max(max_v.values()))])
    t1 = time.time()
    print("time = ",t1-t0)
if __name__ == "__main__":
    main()