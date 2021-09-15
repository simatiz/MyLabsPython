import math
x1 = int(input())
y1 = int(input())
x2 = int(input())
y2 = int(input())
x3 = int(input())
y3 = int(input())
a = math.sqrt((x2 - x1) * (x2 - x1) + (y2 - y1) * (y2 - y1))
b = math.sqrt((x3 - x1) * (x3 - x1) + (y3 - y1) * (y3 - y1))
c = math.sqrt((x3 - x2) * (x3 - x2) + (y3 - y2) * (y3 - y2))
res1 = (math.acos((b * b + c * c - a * a) / (b * c * 2)) * 180) / math.pi
res2 = (math.acos((a * a + c * c - b * b) / (a * c * 2)) * 180) / math.pi
res3 = (math.acos((b * b + a * a - c * c) / (b * a * 2)) * 180) / math.pi
print(a)
print(b)
print(c)
print(res1)
print(res2)
print(res3)