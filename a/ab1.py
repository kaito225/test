import sys
input=sys.stdin.readline
N=input()
A=[]
for i  in range(0,len(N)-1,2):
    A.append(N[i+1])
    A.append(N[i])
result="".join(A)
print(result)