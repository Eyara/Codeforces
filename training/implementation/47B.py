# https://codeforces.com/contest/47/problem/B
import sys

n = 3
letter_dict = {
    'A': 0,
    'B': 0,
    'C': 0
}
for i in range(3):
    f, z, s = sys.stdin.readline().replace('\n', '')
    isMore = True if z == '>' else False
    if isMore:
        letter_dict[f] += 1
    else:
        letter_dict[s] += 1

duplicates = [(i, j) for i in letter_dict for j in letter_dict if letter_dict[i] == letter_dict[j] and i != j]

if len(duplicates) > 0:
    print('Impossible')
else:
    result = ''
    letter_dict = {k: v for k, v in sorted(letter_dict.items(), key=lambda item: item[1])}

    for key in letter_dict:
        result += key

    print(result)
