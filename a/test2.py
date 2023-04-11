import sys
input=sys.stdin.readline

def main(C,N):
    for i in range(N-1,-1,-1):
        print(C[i])
if __name__ =='__main__':
    N=int(input())
    C=[]
    for j in range(N):
        c=str(input())
        C.append(c)
    main(C,N)