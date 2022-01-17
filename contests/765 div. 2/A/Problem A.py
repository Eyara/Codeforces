# https://codeforces.com/contest/1625/problem/0
import sys

t = int(sys.stdin.readline())


for i in range(t):
    n, l = [int(x) for x in sys.stdin.readline().split()]
    forms = [int(x) for x in sys.stdin.readline().split()]
    binary_forms = [f"{x:0{l}b}" for x in forms]

    binary_result = ""

    for j in range(l):
        zero_count = 0
        one_count = 0
        for k in range(n):
            if binary_forms[k][j] == '0':
                zero_count += 1
            else:
                one_count += 1
        binary_result += '1' if zero_count < one_count else '0'

    print(int(binary_result, 2))
