# https://codeforces.com/contest/1618/problem/A
import sys

n = int(sys.stdin.readline())

for i in range(n):
    series = [int(x) for x in sys.stdin.readline().split()]
    result = series[:2]
    result.append(series[len(series) - 1] - sum(result))
    print(' '.join([str(x) for x in result]))