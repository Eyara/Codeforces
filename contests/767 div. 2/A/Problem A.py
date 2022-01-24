# https://codeforces.com/contest/1629/problem/0
import sys

t = int(sys.stdin.readline())

for i in range(t):
    n, k = [int(x) for x in sys.stdin.readline().split()]
    a = [int(x) for x in sys.stdin.readline().split()]
    b_input = sys.stdin.readline().split()
    merged_shops = []
    for j in range(len(b_input)):
        merged_shops.append((a[j], int(b_input[j])))

    merged_shops = sorted(merged_shops, key=lambda x: (x[0], x[1]))

    current_mem = k
    while True:
        max_idx = -1
        curr_max_mem = -1
        visited_idx = -1
        for j in range(len(merged_shops)):
            curr_shop = merged_shops[j]
            if curr_shop[0] <= current_mem:
                if curr_shop[1] > curr_max_mem:
                    max_idx = j
                    curr_max_mem = curr_shop[1]
                    visited_idx = j

        if max_idx == -1:
            break

        if visited_idx != -1:
            del merged_shops[visited_idx]

        current_mem += curr_max_mem

    print(current_mem)
