from functools import reduce


def base_to_int(s, b):
    return reduce(lambda out, i: out + int(s[i]) * b ** (len(s) - i - 1), range(len(s)), 0)


if __name__ == "__main__":
    s = '1111011'
    b = 2
    print(base_to_int(s, b))