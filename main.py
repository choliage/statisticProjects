from skku import skku_calt
from normdist import normdist
from uniform import uniform
from exp import expd
from binominal import bion
from hypgeo import hypg
from poission import pois

def main():
    ansed = False
    while ansed == False:
        dist = ["1.偏態與峰度","2.常態分配平均數與變異數","3.均勻分配平均數與變異數","4.指數分配平均數與變異數","5.二項分配","6.超幾何分配","7.卜瓦松分配"]
        print(dist[0:len(dist)])
        ans = int(input("which calt u need to use? "))
        if ans == 1:
            skku_calt(True)
            ansed = True
        elif ans == 2:
            normdist(True)
            ansed = True
        elif ans == 3:
            uniform(True)
            ansed = True
        elif ans == 4:
            expd(True)
            ansed = True
        elif ans == 5:
            bion(True)
            ansed = True
        elif ans == 6:
            hypg(True)
            ansed = True
        elif ans == 7:
            pois(True)
            ansed = True
        else:
            print("try again")
main()
