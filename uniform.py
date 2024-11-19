import math
def uniform(call):
    ul,ll =map(float,input("輸入均勻分布的上下界").split())
    mean = (ul + ll) /2
    ss = (ul-ll)**2 / 12
    print("期望值為",mean,"變異數為",ss)
