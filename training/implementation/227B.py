# https://codeforces.com/contest/227/problem/B
import sys

nums = {}

n = int(sys.stdin.readline())
a = []
a_inp = sys.stdin.readline().split()
for i in range(len(a_inp)):
    tmp = int(a_inp[i])
    a.append(tmp)
    nums[tmp] = i

m = int(sys.stdin.readline())
b = [int(x) for x in sys.stdin.readline().split()]

res_f = 0
res_s = 0

for case in b:
    idx = nums[case]
    res_f += idx + 1
    res_s += n - idx

print(res_f, res_s)
