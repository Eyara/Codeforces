# https://codeforces.com/contest/768/problem/A
import sys

t = int(sys.stdin.readline())

for i in range(t):
    n = int(sys.stdin.readline())
    a = [int(x) for x in sys.stdin.readline().split()]
    b = [int(x) for x in sys.stdin.readline().split()]

    max_a = max(a)
    max_b = max(b)

    new_arr_min = []
    a_is_max = max_a > max_b

    for j in range(n):
        new_arr_min.append(min(a[j], b[j]))

    if a_is_max:
        print(max_a * max(new_arr_min))
    else:
        print(max_b * max(new_arr_min))
