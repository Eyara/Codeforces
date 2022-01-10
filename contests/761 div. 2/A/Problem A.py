# https://codeforces.com/contest/1617/problem/A
import sys

n = int(sys.stdin.readline())

for i in range(n):
    S = sys.stdin.readline().replace('\n', '')
    T = sys.stdin.readline().replace('\n', '')
    sorted_S = ''.join(sorted(S))

    if 'a' not in S or 'b' not in S or 'c' not in S or T != "abc":
        print(sorted_S)
        continue

    result = ""

    a_count = S.count('a')
    c_count = S.count('c')
    b_count = S.count('b')

    result = 'a' * a_count + 'c' * c_count + 'b' * b_count + sorted_S[a_count + c_count + b_count:len(S)]
    print(result)
