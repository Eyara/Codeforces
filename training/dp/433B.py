# https://codeforces.com/contest/433/problem/B
import sys

n = int(sys.stdin.readline())
v = [int(x) for x in sys.stdin.readline().split()]
m = int(sys.stdin.readline())

sorted_v = sorted(v, key=lambda x: x)

for i in range(1, n):
    v[i] = v[i] + v[i - 1]
    sorted_v[i] = sorted_v[i] + sorted_v[i - 1]

for i in range(m):
    q_type, l, r = [int(x) for x in sys.stdin.readline().split()]
    l, r = l - 2, r - 1
    if q_type == 1:
        if l < 0:
            print(v[r])
        else:
            print(v[r] - v[l])
    else:
        if l < 0:
            print(sorted_v[r])
        else:
            print(sorted_v[r] - sorted_v[l])
