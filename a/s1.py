import sys
input=sys.stdin.readline

def main(P,Q,S,T,A):
    c=A[(P-1):(Q)]
    A[(P-1):(Q)]=A[(S-1):(T)]
    A[(S-1):(T)]=c
if __name__ =='__main__':
    N,P,Q,S,T=map(int,input().split())
    A=list(map(int,input().split()))
    main(P,Q,S,T,A)
    ANS=str()
    for i in range(N):
        if i==N-1:
            ANS+=str(A[i])
            break
        ANS+=str(A[i])+" "
        
    print(ANS)