# https://codeforces.com/contest/1633/problem/A
import sys

t = int(sys.stdin.readline())

for i in range(t):
    n = int(sys.stdin.readline())

    if n % 7 == 0:
        print(n)
        continue

    n_l = [x for x in str(n)]
    l_n = len(n_l)

    ans = 0
    ans_found = False

    for j in range(l_n):
        for k in range(1, 10):
            tmp = n_l
            tmp[j] = k
            tmp_int = int(''.join([str(x) for x in tmp]))

            if tmp_int % 7 == 0:
                ans = tmp_int
                ans_found = True

        if ans_found:
            break

    print(ans)
