def sort_string(string, pattern): # naive implementation
    s = string
    output = ''

    for char in pattern:
        for n in range(len(string)):
            if string[n] == char:
                output += string[n]
                s = s.replace(string[n],'')
    return output + s


def sort_string2(string, pattern): # better implementation using a dictionary (map)
    fmap = {}
    s = string
    for char in string:
        if char in set(pattern):
            fmap[char] = fmap[char] + 1 if char in fmap else 1
            s = s.replace(char, '')
    for char in pattern:
        if char in fmap:
            res = ''.join([char * fmap[char] for char in fmap])[::-1]
    return ''.join((res, s))


if __name__ == "__main__":
    s = 'googled'
    p = 'dog'
    s1 = 'first'
    p1 = 'try'
    print(sort_string2(s, p))


if __name__ == "__main__":
    string = 'googled'
    pattern = 'dog'
    out = 'dooggle'
    s = 'first'
    p = 'try'
    ss = 'avb'
    pp = 'abcdefghijklmnopqrstuvwxyz'
    print(sort_string(s, p))

'''

frequency map
iterate through string
count frequency of the letter
go through alphabet string
read the frequency map
out

put the frequency map in the right order then append the rest
'''
