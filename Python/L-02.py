# -*- coding: utf-8 -*-
import math
import time

def move(n,a,b,c):
    if n==1:
        print(a,'--→',c);  
    else:
        move(n-1,a,c,b)     #把上面的n-1个盘子借助c，从a移动到b
        move(1,a,b,c)       #再把下面的1个盘子借助b，从a移动到c
        move(n-1,b,a,c)     #最后把n-1个盘子借助a，从b移动到c

n = int(input('盘子数量:'))
t0 = time.clock()           #开始计时
print(move(n,'A','B','C'))
t1 = time.clock()           #停止计时
print('计算时间:',t1-t0,'s')

step = pow(2,n)-1
print('移动的步数为:',step,'步')