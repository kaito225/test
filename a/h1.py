N=int(input())
count=0
for i in range(N):
    s=input()
    if s=="For":
        count+=1
if count>=N/2:
    print("Yes")
else:
    print("No")