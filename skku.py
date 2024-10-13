import math
a,b,c,d = map(float,input("輸入N，D^3.sum，D^4.sum，s").split())
SK = (a/((a-1)*(a-2))) * (b/d**3)
KU = (((a*(a+1))/((a-1)*(a-2)*(a-3))) * (c/d**4))-((3*(a-1)*(a-1))/((a-2)*(a-3)))
print("偏態為 ",SK," 峰度為 ",KU)
