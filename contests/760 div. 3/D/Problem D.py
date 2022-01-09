# https://codeforces.com/contest/1618/problem/D
import sys

n = int(sys.stdin.readline())

for i in range(n):
    l, k = [int(x) for x in sys.stdin.readline().split()]
    seq = [int(x) for x in sys.stdin.readline().split()]
    seq = sorted(seq)
    cost = sum(seq[0:l - 2 * k]) + sum(map(lambda x: seq[x + l - 2 * k] // seq[x + l - k], range(0, k)))
    print(cost)
