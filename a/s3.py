import sys
input=sys.stdin.readline

def main(A,N,B,S):
    for i in range(N):
        add=S//A[i]
        add=min(add,B[i])
        S-=A[i]*add
        print(S)
    if(S==0):
        print("Yes")
    else:
        print("No")
if __name__ =='__main__':
    N,S=map(int,input().split())
    A=[]
    B=[]
    res=0
    for i in range(N):
        a,b=map(int,input().split())
        A.append(a)
        B.append(b)
        
    main(A,N,B,S)