# https://codeforces.com/contest/433/problem/B
import sys

n, k = [int(x) for x in sys.stdin.readline().split()]
h = [int(x) for x in sys.stdin.readline().split()]

prefix_sums = [h[0]]

for i in range(1, n):
    prefix_sums.append(h[i] + prefix_sums[i - 1])

min_height = 150000 * 101
answer = -1

for i in range(n - k + 1):
    cur_sum = prefix_sums[i + k - 1] - prefix_sums[i - 1] if i > 0 else prefix_sums[i + k - 1]
    if cur_sum < min_height:
        min_height = cur_sum
        answer = i + 1

print(answer)
