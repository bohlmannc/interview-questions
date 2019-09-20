'''

def string_pattern(string, pattern):
    string_count = []
    pattern_count = []


    string_letters = []
    pattern_letters = []

    a = len(string)
    b = len(pattern)
    pointer = max(a, b)
    print(pointer)

    for i in range(len(string)):
        letter = string[i]
        string_letters.append(letter)
        diff = ord(letter) - ord('a')
        string_count.append(diff)

    for j in range(len(pattern)):
        letter2 = pattern[j]
        pattern_letters.append(letter2)
        diff2 = ord(letter2) - ord('a')
        pattern_count.append(diff2)

    # return string_count, pattern_count
    print(string_count)
    print(pattern_count)

    print(string_letters)
    print(pattern_letters)
'''

def sort_string(string, pattern):
    s = string
    output = ''

    for char in pattern:
        for n in range(len(string)):
            if string[n] == char:
                output += string[n]
                s = s.replace(string[n],'')
    return output + s


def sort_string2(string, pattern):
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


'''
    index = 0
    while index < pointer:
        d = ord(letter) - ord(letter2)
        if d == 0:
            

    res = []
    for m in range(len(pattern_count)):
        p = pattern_count[m]
        for n in range(len(string_count)):
            s = string_count[n]
            if p == s:
                res.append(s)
                m += 1
            else:
                n += 1

    res.extend(string_count[m:-1])
    out = []
    for x in range(len(res)):
        temp = res[x] + 97
        out.append(temp)
    outs = ''
    for z in range(len(out)):
        tmp = chr(out[z])
        outs = outs + tmp

    return outs
'''

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