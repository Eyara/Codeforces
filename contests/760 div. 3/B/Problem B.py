# https://codeforces.com/contest/1618/problem/B
import sys

n = int(sys.stdin.readline())

for i in range(n):
    target_len = int(sys.stdin.readline())
    bigramms = sys.stdin.readline().split()
    for j in range(0, len(bigramms) - 1):
        if bigramms[j][1] != bigramms[j + 1][0]:
            bigramms.insert(j + 1, bigramms[j][1] + bigramms[j + 1][0])
            j += 1
    result = [bigramms[0]]
    for x in bigramms[1:len(bigramms) - 1]:
        result.append(x[1])
    result.append(bigramms[len(bigramms) - 1][1])
    result_str = ''.join(result)
    if len(result_str) < target_len:
        result_str += result_str[len(result_str) - 1]
    print(result_str)
