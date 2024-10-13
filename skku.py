import math
a,b,c,d = map(float,input("輸入N，D^3.sum，D^4.sum，s").split())
SK = (a/((a-1)*(a-2))) * (b/d**3)
KU = (((a*(a+1))/((a-1)*(a-2)*(a-3))) * (c/d**4))-((3*(a-1)*(a-1))/((a-2)*(a-3)))
print("偏態為 ",SK," 峰度為 ",KU)
skconfig = ["負偏","常態分佈","正偏"]
kuconfig = ["低擴峰","常態峰","高狹峰"]

if(SK > 0):
    if(KU >0):
        print("該數值呈現",skconfig[2],"且峰度係數呈現該峰為",kuconfig[2])
    if(KU ==0):
        print("該數值呈現",skconfig[2],"且峰度係數呈現該峰為",kuconfig[1])
    if(KU <0):
        print("該數值呈現",skconfig[2],"且峰度係數呈現該峰為",kuconfig[0])
elif(SK == 0):
    if(KU >0):
        print("該數值呈現",skconfig[1],"且峰度係數呈現該峰為",kuconfig[2])
    if(KU ==0):
        print("該數值呈現",skconfig[1],"且峰度係數呈現該峰為",kuconfig[1])
    if(KU <0):
        print("該數值呈現",skconfig[1],"且峰度係數呈現該峰為",kuconfig[0])
elif(SK <0):
    if(KU >0):
        print("該數值呈現",skconfig[0],"且峰度係數呈現該峰為",kuconfig[2])
    if(KU ==0):
        print("該數值呈現",skconfig[0],"且峰度係數呈現該峰為",kuconfig[1])
    if(KU <0):
        print("該數值呈現",skconfig[0],"且峰度係數呈現該峰為",kuconfig[0])

