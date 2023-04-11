import sys
input=sys.stdin.readline

def main(A,N,ANS):
    for i in range(N):
        ANS+=str(A[i])
        if A[i]=="n" and A[i+1]=="a":
            ANS+=str("y")
    print(ANS)
if __name__ =='__main__':
    N=int(input())
    A=input()
    ANS=str()
    main(A,N,ANS)
