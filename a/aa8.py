import sys
input=sys.stdin.readline
N=int(input())
A=[]
for i  in range(9,-1,-1):
    if N>=pow(2,i):
        A.append(str(1))
        N=N-pow(2,i)
    else:
        A.append(str(0))
result="".join(A)
print(result)