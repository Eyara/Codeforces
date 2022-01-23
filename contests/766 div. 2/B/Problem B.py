# https://codeforces.com/contest/1627/problem/B
import sys

t = int(sys.stdin.readline())

for i in range(t):
    n, m = [int(x) for x in sys.stdin.readline().split()]
    distances = []


    def calc_dist(j, k):
        return max(
            j + k,
            abs(j) + abs(m - 1 - k),
            abs(n - 1 - j) + abs(m - 1 - k),
            abs(n - 1 - j) + k,
        )


    for j in range(n):
        for k in range(m):
            distances.append(calc_dist(j, k))

    result = sorted(distances)[:n * m]

    print(' '.join([str(x) for x in result]))
