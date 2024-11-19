import math
def bion(call):
    freq, pi =map(float,input("輸入檢定事件的次數與機率").split())
    mean = freq*pi
    ss = freq*pi*(1-pi)
    print("期望值為",round(mean,4),"變異數為",round(ss,4))
