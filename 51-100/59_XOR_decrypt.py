import time


def possible_keys():
    possible_keys = []
    start, end = ord('a'), ord('z')
    for i in range(start, end):
        for j in range(start, end):
            for k in range(start, end):
                possible_keys.append([i, j, k])
    return possible_keys


def xor_lists(x, y):
    return [a ^ b for a, b in zip(x, y)]


def generate_candidates(input):
    keys = possible_keys()
    for key in keys:
        res = []
        begin, end = 0, 3
        while end <= len(input):
            encrypted = input[begin:end]
            res.extend(xor_lists(encrypted, key))
            begin += 3
            end += 3
        to_ascii = "".join([chr(i) for i in res])
        yield to_ascii


def percentage_vowels(string):
    return sum(map(string.lower().count, "aeiou"))/len(string)


def solve(input):
    candidates = generate_candidates(input)
    vowels = []
    # We will check if the % vowels is very low, that gives off garbage text.
    for candidate in candidates:
        vowels.append((percentage_vowels(candidate), candidate))
    text = sorted(vowels, reverse=True)[0]
    return sum([ord(i) for i in text[1]])


def main():
    t0 = time.time()
    file = open('59_input.txt', 'r').readline().split(',')
    ans = solve(list(map(int, file)))
    print(ans)
    print("time = ", "\x1b[2;30;42m", time.time() - t0, "\x1b[0m")


if __name__ == "__main__":
    main()
