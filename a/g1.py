import numpy as np
from scipy.sparse.csgraph import connected_components
from scipy.sparse import csr_matrix
N,M=map(int,input().split())
count=N
dp=[[0 for i3 in range(N+1)] for i2 in range(N+1)]
for j in range(M):
    V,W=map(int,input().split())
    if(dp[V][W]==False):
        dp[V][W]=1
for i in range(1,N+1):
    b=0
a=np.array(dp)
n,labels=connected_components(a)
print(a)
print(labels)
print(n)
    

    