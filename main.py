from skku import skku_calt
def main():
    ansed = False
    while ansed == False:
        print("1.Skewness Kurtosis")
        ans = int(input("which calt u need to use? "))
        if ans == 1:
            skku_calt(True)
            ansed = True
        else:
            print("try again")
main()
