import math
d=float(input())
a=float(input())
b=float(input())
c=float(input())
if d<=0:
    print("Error")
elif a==b:
    print("Error")
elif a==-b:
    print("Error")
elif math.sin(c)==0:
    print("Error")
else:
    res=math.log(d)/(math.fabs(b*b-a*a)*math.sin(c))
    print(int(res) if not res else res)