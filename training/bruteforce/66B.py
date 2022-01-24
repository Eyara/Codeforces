# https://codeforces.com/contest/66/problem/B
import sys

n = int(sys.stdin.readline())
t = [int(x) for x in sys.stdin.readline().split()]

best_distance = -1
for i in range(n):
    cur_distance = 1
    l = r = i
    while l > 0:
        if t[l] >= t[l - 1]:
            cur_distance += 1
        else:
            break
        l -= 1

    while r < n - 1:
        if t[r] >= t[r + 1]:
            cur_distance += 1
        else:
            break
        r += 1

    best_distance = max(best_distance, cur_distance)

print(best_distance)
