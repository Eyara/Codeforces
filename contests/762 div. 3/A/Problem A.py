# https://codeforces.com/contest/1619/problem/A
# Alternative for approach below is an using stack but i havent enough time for this

import sys

n = int(sys.stdin.readline())
true_answer = "YES"
false_answer = "NO"

for i in range(n):
    current_str = sys.stdin.readline()
    len_str = len(current_str) - 1
    if len_str % 2 != 0:
        print(false_answer)
        continue
    print(true_answer if current_str[:len_str // 2].split() == current_str[len_str // 2:].split() else false_answer)
