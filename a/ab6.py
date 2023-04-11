N, Q = map(int, input().split())
B=[]
h=1
for i in range(Q):
    A=list(map(int, input().split()))
    if A[0]==1:
        B.append(h)
        h+=1
    if A[0]==3:
        print(min(B))
    if A[0]==2:
        if len(B)>0:
            B.remove(A[1])
                