# https://codeforces.com/contest/1627/problem/A
import sys

t = int(sys.stdin.readline())

for i in range(t):
    n = int(input())
    graph = [[] for __ in range(n + 1)]
    ans = [-1] * (n - 1)
    for i in range(n - 1):
        x, y = map(int, input().split())
        graph[x] += [(y, i)]
        graph[y] += [(x, i)]
    if max(len(graph[i]) for i in range(n + 1)) > 2:
        print(-1)
        continue
    cur, prev = 1, None
    while len(graph[cur]) != 1: cur += 1
    for p in range(n - 1):
        for x, i in graph[cur]:
            if x != prev:
                ans[i] = [17, 2][p % 2]
                cur, prev = x, cur
                break
    print(*ans)
