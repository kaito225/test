while True:
    a=int(input("整数の範囲で答えなさい"))
    if a>0:
        if a<101:
            y=a**2
            print("正方形の面積は",y,"です")
            break
        else:
            print("1以上100以内の値を入れてください")
    else:
        print("1以上100以内の整数で答えなさい")