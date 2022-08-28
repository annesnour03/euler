import time
from pynverse import inversefunc
from collections import deque
from math import sqrt


class Figurates:
    def __init__(self) -> None:
        self.methods = [i for i in dir(self) if not i.startswith(
            '__') and not i[0].isupper()]

    class Inverse:
        @staticmethod
        def inv_triangle(x):
            return (-1 + sqrt(8*x + 1))/2

        @staticmethod
        def inv_square(x):
            return sqrt(x)

        @staticmethod
        def inv_pentagonal(x):
            return (1 + sqrt(24*x + 1))/6

        @staticmethod
        def inv_hexagonal(x):
            return (1 + sqrt(8*x + 1))/4

        @staticmethod
        def inv_heptagonal(x):
            return (3 + sqrt(40*x + 9))/10

        @staticmethod
        def inv_octagonal(x):
            return (1 + sqrt(3*x + 1))/3

    @staticmethod
    def triangle(x):
        return x*(x+1)//2

    @staticmethod
    def square(x):
        return x**2

    @staticmethod
    def pentagonal(x):
        return x*(3*x-1)//2

    @staticmethod
    def hexagonal(x):
        return x*(2*x - 1)

    @staticmethod
    def heptagonal(x):
        return x*(5*x - 3)//2

    @staticmethod
    def octagonal(x):
        return x*(3*x-2)


def get_inverse_limit(value, func):
    return int(getattr(Figurates.Inverse, "inv_" + func.__name__)(int(value)))


def indivdual_figurate(limit, function):
    seq = set()
    inv_limit = get_inverse_limit(limit, function)
    for i in range(inv_limit):
        seq.add(function(i))
    return seq


def generate_seq(x):
    seq = set()
    # We need a reference to all the methods
    figurates = [getattr(Figurates, method) for method in Figurates().methods]
    for func in figurates:
        seq = seq.union(indivdual_figurate(x, func))
    return list(seq)


def filter_starts_with(to_be_filtered: list, start):
    return list(filter(lambda x: x.startswith(start), to_be_filtered))


def unique_figurates(figurates):
    methods = Figurates().methods
    for i in range(5):
        exit = False # The quick exits make the code around 25% faster (3s total)
        methods.insert(0,methods.pop())
        seen_map = dict(zip(methods, [False] * len(methods)))
        for i in figurates:
            if exit:
                break
            for method in methods:
                if getattr(Figurates.Inverse, "inv_" + method)(int(i)).is_integer():
                    if seen_map[method] == True:
                        exit = True
                        break
                    seen_map[method] = True
                    break # <- took me about 3 hours for this single break ouch
    return all(seen_map.values())


def solve(limit, length):
    seq = sorted(list(filter(lambda x: x >= limit//10, (generate_seq(limit)))))
    seq = deque([[str(i)] for i in seq])
    og = deque([str(*i) for i in seq])
    while seq:
        trace = seq.popleft()
        if len((trace)) == length:
            if not unique_figurates(trace):
                continue
            if trace[length-1][-2:] == trace[0][:2]:
                yield trace
            continue
        v = trace[-1]
        ending = v[-2:]
        candidates = filter_starts_with(og, ending)
        for candidate in candidates:
            seq.append([*trace, candidate])
    return []


def main():
    t0 = time.time()
    DIGITS = 4
    LENGTH_OF_SET = 6
    ans = list(solve(10 ** DIGITS,LENGTH_OF_SET))
    for i in ans:
        print(sorted(i),len(ans),sum(map(int,i)))

    print("time = ", "\x1b[2;30;42m", time.time() - t0, "\x1b[0m") # 3s


if __name__ == "__main__":
    main()
