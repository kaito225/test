import sys
input=sys.stdin.readline
N,M=map(int,input().split())
count=0
for i in range(1,N+1):
    for j in range(1,N+1):
        for k in range(1,N+1):
            if i+j+k==M:
                count+=1
            if i+j+k>M:
                break
print(count)