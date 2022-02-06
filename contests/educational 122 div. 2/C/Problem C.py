# https://codeforces.com/contest/1633/problem/B
import math
import sys

t = int(sys.stdin.readline())

for i in range(t):
    hc, dc = [int(x) for x in sys.stdin.readline().split()]
    hm, dm = [int(x) for x in sys.stdin.readline().split()]
    k, w, a = [int(x) for x in sys.stdin.readline().split()]

    if math.ceil(hc / dm) >= math.ceil(hm / dc):
        print("YES")
        continue

    has_win_option = False
    for j in range(k):
        if math.ceil((hc + j * a) / dm) >= math.ceil(hm / (dc + (k - j) * w)) or math.ceil(
                (hc + (k - j) * a) / dm) >= math.ceil(hm / (dc + j * w)):
            has_win_option = True
            break

    print("YES" if has_win_option else "NO")
