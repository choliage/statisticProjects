import math
def skku_calt(call):
    if call == True:
        a,b,c,d = map(float,input("輸入N，D^3.sum，D^4.sum，s").split())
        SK = float((a/((a-1)*(a-2))) * (b/d**3))
        KU = float((((a*(a+1))/((a-1)*(a-2)*(a-3))) * (c/d**4))-((3*(a-1)*(a-1))/((a-2)*(a-3))))
        
        print("偏態為 ",SK,"峰度為 ",KU)
        
        skewness_label = ["負偏", "常態分佈", "正偏"]
        kurtosis_label = ["低擴峰", "常態峰", "高狹峰"]

        if SK > 0:
            skewness_type = skewness_label[2]
        elif SK == 0:
            skewness_type = skewness_label[1]
        else:
            skewness_type = skewness_label[0]
        
        if KU > 0:
            kurtosis_type = kurtosis_label[2]
        elif KU == 0:
            kurtosis_type = kurtosis_label[1]
        else:
            kurtosis_type = kurtosis_label[0]
        print(f"該數值呈現 {skewness_type}，且峰度係數呈現該峰為 {kurtosis_type}")
