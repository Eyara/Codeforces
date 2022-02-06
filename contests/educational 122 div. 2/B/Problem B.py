# https://codeforces.com/contest/1633/problem/B
import sys

t = int(sys.stdin.readline())

for i in range(t):
    n = sys.stdin.readline().replace('\n', '')
    n = str(n)
    z_count = n.count('0')
    f_count = n.count('1')

    if z_count != f_count:
        print(min(z_count, f_count))
        continue

    print(min(n[:-1].count('0'), n[:-1].count('1')))
