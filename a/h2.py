N,M=map(int,input().split())
A=[]
C=[]
B=[]
count=0
flg=0
for j in range(N):
    P=input()
    A.append(P)
for k in range(M):
    L=input()
    C.append(L)
for g in C:
    if g not in B:
        B.append(g)
for p in range(N):
    for o in range(len(B)):
        if(A[p][3:6]==B[o][:]):
                count+=1
                break
print(count)
    