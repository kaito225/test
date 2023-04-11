import sys
input=sys.stdin.readline
import itertools
import numpy as np

def main(A,dp,a):
    for i in A:
        for j in range (a,-1,-1):
            if dp[j] and i+j<=a:
                dp[i+j]=True
    ans="Yes" if dp[a] else "No"
    print(ans)
if __name__ =='__main__':
    N,S=map(int,input().split())
    B=[True]+[False]*S;
    A=list(map(int,input().split()))
    main(A,B,S)
    
#for j in itertools.combinations(A,j+1):