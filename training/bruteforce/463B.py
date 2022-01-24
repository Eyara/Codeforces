# https://codeforces.com/contest/463/problem/B
import sys

n = int(sys.stdin.readline())
h = [int(x) for x in sys.stdin.readline().split()]

print(max(h))

# Brute force solution
# result = h[0]
# energy = 0
# for i in range(len(h) - 1):
#     energy += h[i] - h[i + 1]
#     if energy < 0:
#         result += -1 * energy
#         energy = 0
#
# print(result)
