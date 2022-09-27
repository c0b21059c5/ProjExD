from random import sample, randint, shuffle

alphalist=list("QWERTYUIOPASDFGHJKLZXCVBNM")
#num_taisyoumozi = randint(2, len(alphalist))
#num_hyouzi = randint(1, (num_taisyoumozi-1))
num_taisyoumozi=10
num_hyouzi=8
num_kessonmozi=num_taisyoumozi-num_hyouzi

taisyoulist=[]
kessonlist=[]
hyouzilist=[]

def shutudai():
    #num_taisyoumozi = randint(2, len(alphalist))
    #num_hyouzi = randint(1, (num_taisyoumozi-1))

    taisyoulist = sample(alphalist, num_taisyoumozi)
    hyouzilist = sample(taisyoulist, num_hyouzi)
    kessonlist = list(set(taisyoulist)-set(hyouzilist))

    print("対象文字")
    print(taisyoulist)
    print("表示文字")
    print(hyouzilist)
    print("欠損文字（デバック用）")
    print(kessonlist)


    a1=int(input("欠損文字はいくつあるでしょうか?:"))
    if num_kessonmozi == a1:
        print("正解です。それでは、具体的に欠損文字を１つずつ入力してください")
        for i in range(num_kessonmozi):
            a=input(str(i+1)+"つ目の文字を入力してください")
            if a not in kessonlist:
                print("不正解です")
                shutudai()
    else:
        print("不正解です。またチャレンジしてください")

    print("おめでとうございます！")
    

if __name__ == "__main__":
    shutudai()
