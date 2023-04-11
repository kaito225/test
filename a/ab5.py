import string

A = list(string.ascii_uppercase)
A.insert(0, ".")
N,M=map(int,input().split())
for j in range(N):
    B=list(map(int,input().split()))
    C=[]
    for i in range(M):
        C.append(A[B[i]])
    C="".join(C)
    print(C)