# https://codeforces.com/contest/1928/problem/A
import sys

n = int(sys.stdin.readline())

for i in range(n):
    a, b = [int(x) for x in sys.stdin.readline().replace('\n', '').split()]

    if a % 2 == 0 and b % 2 == 0:
        print('Yes')
        continue
    elif a % 2 != 0 and b % 2 != 0:
        print('No')
        continue
    elif a % 2 == 0:
        a /= 2
        print('Yes' if a != b else 'No')
        continue
    else:
        b /= 2
        print('Yes' if a != b else 'No')
        continue
