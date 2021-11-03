import math
n = int(input())
n=n+1
for a in range(n):
    for b in range(n):
        for c in range(n):
            if a!=0:
                if b!=0:
                    if c!=0:
                        if a*a+b*b==c*c:
                            print(a, b, c)