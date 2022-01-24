# https://codeforces.com/contest/680/problem/B
import sys

n, a = [int(x) for x in sys.stdin.readline().split()]
t = [int(x) for x in sys.stdin.readline().split()]

min_dist = min(a-1, n - a)
equal_cities = t[a - 1 - min_dist:a + min_dist]
del t[a - 1 - min_dist:a + min_dist]
ec_len = len(equal_cities)

result = 0
for i in range(ec_len // 2 + 1):
    if equal_cities[i] == 1 and equal_cities[ec_len - i - 1] == 1:
        result += 2
        if i == ec_len - i - 1:
            result -= 1
for el in t:
    if el == 1:
        result += 1

print(result)
