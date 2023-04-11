import bisect

N,M=map(int,input().split())
A=list(map(int,input().split()))
B=list(map(int,input().split()))

C=A+B
C.sort()

D=[]
E=[]
for j in range(N):
    idx = bisect.bisect_left(C, A[j])
    D.append(str(idx+1))
for k in range(M):
    idx = bisect.bisect_left(C, B[k])
    E.append(str(idx+1))

print(" ".join(D))
print(" ".join(E))
