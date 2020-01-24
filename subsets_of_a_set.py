from functools import reduce


def power_set(s):

    '''
    def go(i, out):
        if i == len(s):
            return out
        else:
            return go(i + 1, out + list(map(lambda x: x + s[i])))

    out = ['']
    for i in range(len(s)):
        out += list(map(lambda x: x + s[i]))
    return out
    '''

    return reduce(lambda out, i: out + list(map(lambda x: x + s[i],  out)), range(len(s)), [''])


def find_subsets(array):
    subsets = [[]]
    for value in array:
        subsets = subsets + [s + [value] for s in subsets]
    return subsets


"""
0: []
1: [], [1]
2: [], [1], [11], [1, 11]
3: [], [1], [11], [1, 11], [3], [1, 3], [11, 3], [1, 11, 3]
"""

"""
0: []
1: [], [1]
2: [], [1], [2], [1, 2]
3: [], [1], [2], [1, 2], [3], [1, 3], [2, 3], [1, 2, 3]
"""


def reduce_subsets(array):
    return reduce(lambda subsets, value: subsets + list(map(lambda s: s + [array[value]], subsets)),
                  range(len(array)), [[]])


if __name__ == '__main__':
    a = [1, 11, 3, 5]
    b = [1, 2, 3]
    find_subsets(a)
    # print(find_subsets(a))
    print('cheeky', reduce_subsets(b))
    # print([[] for _ in range(len(a))])
