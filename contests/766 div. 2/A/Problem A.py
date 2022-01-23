# https://codeforces.com/contest/1627/problem/A
import sys

t = int(sys.stdin.readline())

for i in range(t):
    n, m, r, c = [int(x) for x in sys.stdin.readline().split()]
    r, c = r - 1, c - 1
    arr = [[] * m] * n
    for i in range(n):
        arr[i] = [0 if x == 'W' else 1 for x in sys.stdin.readline().replace('\n', '')]

    black_idxs = []
    for row in range(n):
        for index, element in enumerate(arr[row]):
            if element == 1:
                black_idxs.append((row, index))

    if len(black_idxs) == 0:
        print(-1)
        continue

    if arr[r][c] == 1:
        print(0)
        continue

    target = (r, c)
    if target in black_idxs:
        print(1)
        continue

    has_black_row_or_col = False
    for idx in black_idxs:
        if idx[0] == target[0] or idx[1] == target[1]:
            has_black_row_or_col = True

    if has_black_row_or_col:
        print(1)
    else:
        print(2)
