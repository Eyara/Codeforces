# https://codeforces.com/contest/1619/problem/C

import sys

n = int(sys.stdin.readline())

for i in range(n):
    a, s = [int(x) for x in sys.stdin.readline().split()]
    if a > s \
            or s > a > 10 and abs(s - a) < 10 \
            or s > a and a < 10 and abs(s - a) > 10:
        print(-1)
        continue
    a_str = str(a)
    s_str = str(s)
    a_str_offset = (len(s_str) - len(a_str))

    a_str = '0' * a_str_offset + a_str

    result = []
    index_a = len(a_str) - 1
    index_s = len(s_str) - 1

    while index_s >= 0:
        s_sub = s_str[index_s]
        a_sub = a_str[index_a]

        if int(s_sub) < int(a_sub):
            index_s -= 1
            s_sub = s_str[index_s] + s_sub

        result.append(str(int(s_sub) - int(a_sub)))

        index_s -= 1
        index_a -= 1

    print(''.join(result[::-1]).lstrip('0'))
