# https://codeforces.com/contest/769/problem/A
import sys

t = int(sys.stdin.readline())

for i in range(t):
    a = int(sys.stdin.readline())
    b = [x for x in sys.stdin.readline().replace('\n', '')]

    if len(b) > 2:
        print("NO")
        continue
    elif len(b) == 1:
        print("YES")
        continue

    isDiff = b[0] != b[1]

    print("YES" if isDiff else "NO")
