# https://codeforces.com/contest/102/problem/B
import sys

n = sys.stdin.readline().replace('\n', '')

result = 0
if len(n) == 1:
    print(0)
else:
    while len(n) > 1:
        sum_n = 0
        for ch in n:
            sum_n += int(ch)
        n = str(sum_n)
        result += 1

    print(result)
