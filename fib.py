# Given: n months and k reproduced

with open('.rosalind/fib-1778366769843.txt') as f:
    n, k = map(int, f.readline().split())

if n == 1 or n ==2:
    print(1)
else:
    ans = [0] * n
    ans[0] = 1
    ans[1] = 1

    for i in range(2, n):
        ans[i] = ans[i-1] + k * ans[i-2]

    print(ans[-1])