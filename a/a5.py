while True:
    a=input()
    if len(a)==3:
        if a.isdecimal()==True:
            y=int(a)*2
            print(y)
            break
        else:
            print("error")
            break