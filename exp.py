import math
def expd(call):
    landa =float(input("輸入事件發生的頻率(次數/單位時間)"))
    landa = round(1/landa,4)
    print("期望值為",landa,"變異數為",round(landa**2,4))
