import math
def hypg(call):
    S,N,n =map(float,input("事件的成功次數、母體次數與輸入抽樣次數").split())
    mean = n*S/N
    ss = n*S/N*(N-S)/N*(N-n)/N-1
    print("期望值為",round(mean,4),"變異數為",round(ss,4))
