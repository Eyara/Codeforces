# https://codeforces.com/contest/16/problem/B
import sys

n, m = [int(x) for x in sys.stdin.readline().split()]
containers = []
for i in range(m):
    inp = [int(x) for x in sys.stdin.readline().split()]
    containers.append([inp[0], inp[1]])

containers = sorted(containers, key=lambda x: -x[1])

result = 0
capacity = 0
for container in containers:
    if capacity + container[0] <= n:
        result += container[0] * container[1]
        capacity += container[0]
        if capacity == n:
            break
    else:
        result += (n - capacity) * container[1]
        break

print(result)
