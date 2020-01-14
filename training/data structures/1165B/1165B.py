import sys
pos = 1
length = int(sys.stdin.readline())
contest_counts = list(map(int, sys.stdin.readline().split()))
contest_counts.sort()
for i in range(0, length):
    if contest_counts[i] >= pos:
        pos += 1
print(pos - 1)