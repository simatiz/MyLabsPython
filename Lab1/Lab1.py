x1 = double(input())
y1 = double(input())
x2 = double(input())
y2 = double(input())
x3 = double(input())
y3 = double(input())
a = sqrt((x2 - x1) * (x2 - x1) + (y2 - y1) * (y2 - y1))
b = sqrt((x3 - x1) * (x3 - x1) + (y3 - y1) * (y3 - y1))
c = sqrt((x3 - x2) * (x3 - x2) + (y3 - y2) * (y3 - y2))
res1 = (acos((b * b + c * c - a * a) / (b * c * 2)) * 180) / math.pi
res2 = (acos((a * a + c * c - b * b) / (a * c * 2)) * 180) / math.pi
res3 = (acos((b * b + a * a - c * c) / (b * a * 2)) * 180) / math.pi