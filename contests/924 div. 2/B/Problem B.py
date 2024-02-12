# https://codeforces.com/contest/1928/problem/B
import sys

t = int(sys.stdin.readline())

for i in range(t):
    n = int(sys.stdin.readline())
    a = [int(x) for x in sys.stdin.readline().replace('\n', '').split()]
    a = list(set(a))
    a.sort()

    result = 0
    pnt = 0

    for j in range(len(a)):
        while a[j] - a[pnt] >= n:
            pnt += 1

        result = max(result, j - pnt + 1)

    print(result)
