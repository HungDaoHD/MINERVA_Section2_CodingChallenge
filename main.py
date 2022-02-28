# II. Section 2: Coding Challenge
# 1. A pair (i, j) is called good if nums[i] == nums[j] and i < j.
def good_pairs(lstNum):
    lstPairs = list()

    for i in range(len(lstNum)):
        if not isinstance(lstNum[i], int):
            return 'Invalid list.'

        for j in range(i+1, len(lstNum)):
            if lstNum[i] == lstNum[j]:
                lstPairs.append((i, j))

    return f'{lstPairs} \nThere are {len(lstPairs)} good pairs'


# 2. is_beautiful_string
import re


def is_beautiful_string(strInput):
    if not re.findall('^[a-z]{3,50}$', strInput):
        return 'Invalid string'
    if 'a' not in strInput:
        return False

    dict_alphabet = {
        'a': 0,
        'b': 0,
        'c': 0,
        'd': 0,
        'e': 0,
        'f': 0,
        'g': 0,
        'h': 0,
        'i': 0,
        'j': 0,
        'k': 0,
        'l': 0,
        'm': 0,
        'n': 0,
        'o': 0,
        'p': 0,
        'q': 0,
        'r': 0,
        's': 0,
        't': 0,
        'u': 0,
        'v': 0,
        'w': 0,
        'x': 0,
        'y': 0,
        'z': 0
    }

    for c in strInput:
        dict_alphabet[c] = strInput.count(c)

    lstKeys = list(dict_alphabet.keys())
    lstKeys.sort()

    for i, v in enumerate(lstKeys):
        if v != 'z' and dict_alphabet[v] < dict_alphabet[lstKeys[i+1]]:
            return False

    return True



if __name__ == '__main__':
    # lst_num = [1, 2, 3, 1, 1, 3]
    # lst_num = [1, 1, 1, 1]
    # lst_num = [1, 2, 3]
    # lst_num = [7, 2, 3, 4, 6, 8, 7, 1, 2, 3, 5, 8, 7, 4, 6, 3, 7, 8, 1, 6, 8, 7, 4, 6, 1]
    # lst_num = [98, 79, 98, 17, 52, 98, 25, 30, 96, 20, 39, 58, 21, 67, 86, 38, 97, 21, 65, 89, 47, 23, 65, 87, 23, 64, 98, 75, 63, 21]
    # lst_num = ['a', 1, 98, 'y', 4, 9, 8, 2, 1, 7, 'a', 3, 'd', 9, 'y', 8, 4, 'a', 7, 2]
    # lst_num = [1.5, .6, 1.5, .7, .6, .8, 1, 2, 3, 4, 5, 4, 4, 5]
    lst_num = [0, 2, 9, 5, 7, 0, 1, 9, 2, 8, 3, 7, 0, 9, 1, 8, 3, 8, 9, 1, 2, 4, 0, 1, 8, 2, 0, 9, 8, 1, 8, 9, 3, 4, 1, 0, 2, 3]

    print(good_pairs(lst_num), '\n\n\n')


    # str_input = 'bbbaacdafe'
    # str_input = 'aabbb'
    # str_input = 'bbbbcbaacdafe'
    # str_input = 'bbbbcbaacdafaeacccdef'
    # str_input = 'aaaa'
    # str_input = 'aaayy'
    str_input = 'aaazz'

    print(f'is_beautiful_string({str_input}) = {is_beautiful_string(str_input)}')




