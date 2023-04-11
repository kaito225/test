N=int(input())
A=list(map(float,input().split()))
A.sort()
sum=0
K=0
for i in range(N,(len(A)-N)):
    sum+=A[i]
    K+=1
print(sum/K)