# https://codeforces.com/contest/492/problem/B
import sys

n, l = [int(x) for x in sys.stdin.readline().split()]
a = [int(x) for x in sys.stdin.readline().split()]
a = sorted(a)

min_dist = 0

for i in range(n - 1):
    min_dist = max(min_dist, (a[i + 1] - a[i]) / 2)

min_dist = max(min_dist, (a[0] - 0))
min_dist = max(min_dist, (l - a[n - 1]))

print(min_dist)
