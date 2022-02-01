# https://codeforces.com/contest/769/problem/B
import sys

t = int(sys.stdin.readline())


def highest_power_of_2(n):
    res = 0
    for i in range(n, 0, -1):
        # If i is a power of 2
        if (i & (i - 1)) == 0:
            res = i
            break

    return res


for i in range(t):
    N = int(sys.stdin.readline())
    power_of_two = highest_power_of_2(N - 1)
    left_part = [i for i in range(1, power_of_two)]
    right_part = [i for i in range(power_of_two, N)]
    result = left_part + [0] + right_part
    print(" ".join(str(item) for item in result))
