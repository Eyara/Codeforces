# https://codeforces.com/contest/1619/problem/B

import sys
import math

n = int(sys.stdin.readline())

for i in range(n):
    current_num = int(sys.stdin.readline())
    result = set()
    for j in range(1, int(math.floor(math.sqrt(current_num))) + 1):
        square_num = math.pow(j, 2)
        cubic_num = math.pow(j, 3)
        if square_num not in result and square_num <= current_num:
            result.add(square_num)
        if cubic_num not in result and cubic_num <= current_num:
            result.add(cubic_num)
    print(len(result))
