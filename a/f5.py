n=int(input())
for i in range(n):
    s=int(input())
    A=list(map(int,input().split()))
    B=list(map(int,input().split()))
    j=0
    count=0
    while True:
            
            if(j==s-1):
                if(A[j]!=B[j] and B[j]==A[0]):
                    A[j]=A[0]
                    count=1
                if(count>1):
                    j=0
                    count=0
                else:
                    break
            if(A[j]!=B[j] and B[j]==A[j+1]):
                A[j]=A[j+1]
                count=0
            j+=1
                    
    if(A==B):
            print("Yes")
    else:
            print("No")