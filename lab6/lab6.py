import math
def sumofn(n, a, r):
    for i in range(n):
        r = r + a % 10
        a = a / 10
        return r

k = int(input())
n = int(input())
r = 0
res = 0
max = 0

for i in range(k):
    a = int(input())
    p=sumofn(n, a, r)
    if p > max:
        max = p
        res = a
print(res)