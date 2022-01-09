# https://codeforces.com/contest/1618/problem/C
import sys
import math
from functools import reduce


def find_gcd(list):
    x = reduce(math.gcd, list)
    return x


n = int(sys.stdin.readline())

for i in range(n):
    target_len = int(sys.stdin.readline())
    seq = [int(x) for x in sys.stdin.readline().split()]
    gsd_even = find_gcd(seq[::2])
    gsd_odd = find_gcd(seq[1::2])
    odd_by_gsd_even = True in ([True if x % gsd_even == 0 else False for x in seq[1::2]])
    even_by_gsd_odd = True in ([True if x % gsd_odd == 0 else False for x in seq[::2]])

    if odd_by_gsd_even and even_by_gsd_odd:
        print(0)
        continue
    if not odd_by_gsd_even and even_by_gsd_odd:
        print(gsd_even)
        continue

    print(gsd_odd)
