A,B=map(int,input().split())
C=[]
for i in range(A):
    s=input()
    C.append(s)
D=C[0:B]
D=sorted(D)
for j in range(len(D)):
    print(D[j])