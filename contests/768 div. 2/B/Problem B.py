# https://codeforces.com/contest/768/problem/B
import sys

t = int(sys.stdin.readline())

for i in range(t):
    n = int(sys.stdin.readline())
    a = [int(x) for x in sys.stdin.readline().split()]

    if max(a) == min(a):
        print(0)
        continue

    a = [a[0]] + list(reversed(a[1:]))

    result = 0
    j = 0

    while j < n - 1:
        if a[j + 1] == a[0]:
            j += 1
            continue
        result += 1
        if j == 0:
            j = 2
        else:
            j *= 2

    print(result)
