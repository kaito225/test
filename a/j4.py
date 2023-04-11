N,M=map(int,input().split())
C=[]
for i in range(1,N+1):
    C.append(i)
A=list(map(int,input().split()))
A.reverse()
for j in range(M):
    a=C[A[j]]
    print(a)
    count=0
    while True:
        if j==len(A)-1:
            break
        if A[j]-1==A[j+1]:
            count+=1
            j+=1
        else:
            j+=1
            break
    C.remove(a)
    C.insert(count,a)
print(C)
