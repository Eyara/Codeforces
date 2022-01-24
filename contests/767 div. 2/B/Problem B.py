# https://codeforces.com/contest/1629/problem/B

import math
import sys


def is_almost_prime(num):
    if num == 1:
        return True
    a = 2
    while a <= math.sqrt(num):
        if num % a < 1:
            return False
        a = a + 1
    return num > 1


t = int(sys.stdin.readline())

for i in range(t):
    l, r, k = [int(x) for x in sys.stdin.readline().split()]
    almost_prime_num = 0
    start_iter = l
    while start_iter <= r:
        if is_almost_prime(start_iter):
            almost_prime_num += 1
        start_iter += 1

    if l == r and l == 1:
        print("NO")
        continue

    if k == 0:
        if almost_prime_num == 0:
            print("YES")
            continue
        elif almost_prime_num == 1 and l - r == 0 and l != 1:
            print("YES")
            continue

    additional_add = 0 if l > 1 else 1

    if l > 1:
        if almost_prime_num // 2 + additional_add < k:
            print("YES")
        else:
            print("NO")
    else:
        if r / 2 < k:
            print("YES")
        else:
            print("NO")
