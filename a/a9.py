while True:
    a=input()
    b=input()
    if len(a)<101 and len(b)<101 and len(a)>0 and len(b)>0:
        result=b in a
        if result==True:
            print("Yes")
            break
        else:
            print("No")
            break