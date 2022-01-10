# https://codeforces.com/contest/1617/problem/B
import sys
import math
import random

n = int(sys.stdin.readline())

for i in range(n):
    N = int(sys.stdin.readline())
    while True:
        a = random.randint(2, N - 2)
        b = N - a - 1
        if a != b and b != 1 and math.gcd(a, b) == 1:
            print(a, b, 1, sep=' ')
            break
