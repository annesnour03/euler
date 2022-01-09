import time

# Calculates triangle numbers up to given range
def gettriangle(region):
    res = []
    for i in range(1,region):
        res.append(int(0.5 * i * i + 0.5*i))

    return res

# Removes ' "" ' and ','
def parse(raw):
    raw = [i.replace(',', '') for i in raw]
    while '' in raw:
        raw.remove('')
    return raw

def solve(names):
    triangle = gettriangle(50)
    score = 0
    triangle_words = 0
    for i in names:
        for j in i:
            score = score + ord(j) - 64
        if(score in triangle):
            triangle_words +=1
        score = 0
    return triangle_words

def main():
    t0 = time.time()
    raw = parse(open('42_input.txt', 'r').readline().split('"'))

    ans = solve(parse(raw))
    print(ans)
    print("time = ", "\x1b[1;30;42m", time.time() - t0, "\x1b[0m")

if __name__ == "__main__":
    main()
