# -*- coding: utf-8 -*-
import math
def quadratic(a,b,c):
    d = pow(b,2)-4*a*c
    if d < 0:
        print('此方程无解')
        return
    else:
        sqrtD = math.sqrt(d)
        x1 = -b+sqrtD/2*a
        x2 = -b-sqrtD/2*a
        return x1,x2
    
a = float(input('a:'))
b = float(input('b:'))
c = float(input('c:'))
result = quadratic(a,b,c)
if result is not None:
    print('此方程的解为:x1 = %f,x2 = %f'%(result))
