# https://codeforces.com/contest/227/problem/B
import sys

n = int(sys.stdin.readline())

colors = ['R', 'O', 'Y', 'G', 'B', 'I', 'V']
offset_colors = colors
offset = n % 7
full_filled_num = n // 7
if offset < 4:
    off_new = 4 - offset
    offset_colors = offset_colors[off_new:] + offset_colors[:off_new]

result = colors * full_filled_num + offset_colors[:offset]

print(''.join(result))
