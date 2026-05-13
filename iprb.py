k = 23
m = 29
n = 24

t = k + m + n

ans = (k*((k-1) + 2*(m + n)) + 0.75 * (m*(m-1)) + m*n) / (t*(t - 1))

print(ans)