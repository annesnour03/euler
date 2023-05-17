import time
from pprint import pprint


def solve(passcodes: list[str]):
    possible = [str(i) for i in range(10)]
    result = {passcode: [False] * len(possible) for passcode in possible}

    def comesBeforeAll(a, b):
        for key in passcodes:
            leftIndex, rightIndex = key.find(a), key.find(b)
            if leftIndex == -1 or rightIndex == -1:
                continue
            if leftIndex > rightIndex:
                return False
        return True

    for first in possible:
        for second in possible:
            result[first][int(second) - 1] = comesBeforeAll(first, second)
    del result['4']
    del result['5']
    sor = sorted([(sum(value), key)
                  for key, value in result.items()], reverse=True)
    return "".join(list(map(lambda x: x[1], sor)))


def main():
    t0 = time.time()
    with open("79_input.txt") as f:
        lines = [line.rstrip() for line in f]
    print(solve(lines))
    print("time = ", "\x1b[2;30;42m", time.time() - t0, "\x1b[0m")


if __name__ == "__main__":
    main()
