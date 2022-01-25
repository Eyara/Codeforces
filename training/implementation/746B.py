# https://codeforces.com/contest/746/problem/B
import sys

n = int(sys.stdin.readline())
s = sys.stdin.readline().replace('\n', '')

result = s[0]

for i in range(1, n):
    if n % 2 == 0:
        result = result + s[i] if i % 2 != 0 else s[i] + result
    else:
        result = result + s[i] if i % 2 == 0 else s[i] + result

print(result)
