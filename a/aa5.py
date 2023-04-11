N,Q=map(int,input().split())
list=N*[0]
for i in range(Q):
    a,b=map(int,input().split())
    if a==3:
        if list[b-1]>1:
            print("Yes")
        else:
            print("No")
    elif a==2:
        list[b-1]+=2
    elif a==1:
        list[b-1]+=1