import sys
input=sys.stdin.readline    
N=int(input())
A=list(input())
B=list(input())
for i in range(N):
    f=str()
    p=str()
    e=str()
    d=str()
    for k in range(N):
        f+=A[k]
        p+=B[k]
    t=int(f)*int(p)
    c=A[i]
    A[i]=B[i]
    B[i]=c
    for j in range(N):
        e+=A[j]
        d+=B[j]
    if(t<int(e)*int(d)):
        c=B[i]
        B[i]=A[i]
        A[i]=c
        
o=str()
r=str()
for y in range(N):
        o+=A[y]
        r+=B[y]
print(int(o)*int(r)%998244353)