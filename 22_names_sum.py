import time

def getscore(res,name):
    name_score = 0
    for j in range(0,len(name)):
        name_score = name_score + ord(name[j]) - 64
    return name_score * (res.index(name)  + 1)


def main():
    t0 = time.time()
    f = open("22_input.txt","r")
    final = list(f.readline().split('"'))
    names =  list()
    for i in final:
        names = [i.rstrip(',') for i in final]
    while '' in names:
        names.remove('')
    names =  sorted(names)

    result = list()
    for i in names:
        result.append(getscore(names,i))
    print(sum(result))
    t1 = time.time()
    print("time = ",t1-t0)
if __name__ == "__main__":
    main()