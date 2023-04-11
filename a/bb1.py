N=int(input())
s=input()
i = 0
A=[0]*N
while i < N:
    if s[i] == "M":
        A[i]=1
        if A[i-1]==1  and i>0:
            print("No")
            break
    if s[i] == "F":
        A[i]=2
        if A[i-1]==2  and i>0:
            print("No")
            break
    
    if i==N-1:
        print("Yes")
    i+=1