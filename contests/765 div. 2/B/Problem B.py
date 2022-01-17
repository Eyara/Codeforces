# https://codeforces.com/contest/1625/problem/B
import sys
from collections import defaultdict

t = int(sys.stdin.readline())

for i in range(t):
    n = int(sys.stdin.readline())
    items = [int(x) for x in sys.stdin.readline().split()]

    duplicates = defaultdict(list)
    for i, item in enumerate(items):
        duplicates[item].append(i)
    duplicates = {k: occurrence for k, occurrence in duplicates.items() if len(occurrence) > 1}

    if len(duplicates) == 0:
        print(-1)
    else:
        distance_list = []
        best__spaces = defaultdict(list)

        for duplicate in duplicates:
            best_idx = 0
            min_dist = 150000
            for j in range(0, len(duplicates[duplicate]) - 1):
                cur_dist = abs(duplicates[duplicate][j] - duplicates[duplicate][j + 1])
                if cur_dist < min_dist:
                    best_idx = j
                    min_dist = cur_dist
            best__spaces[duplicate].append(duplicates[duplicate][best_idx])
            best__spaces[duplicate].append(duplicates[duplicate][best_idx + 1])

        for duplicate in best__spaces:
            first_idx = best__spaces[duplicate][0]
            second_idx = best__spaces[duplicate][1]

            distance_list.append(n - (second_idx - first_idx))

        print(max(distance_list))
