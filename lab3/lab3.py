import math
a = float(input())
if a <= 1:
    x0 = min(2 * a, 0.95)
elif a < 25:
    x0 = a / 5
else:
    x0 = a / 25
xn = x0
xn1 = 0.8 * xn + a / (5 * xn**4)
while 1.25 * a * math.fabs(xn1 - xn) >= 10**(-6):
    xn = xn1
    xn1 = 0.8 * xn1 + a / (5 * xn1**4)
res = a - xn**5
print(xn)
print(res)