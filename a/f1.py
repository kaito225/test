import math
a,b,c=map(int,input().split())
i=1
count=0
while True:
  if(b*i>a):
    break
  else:
    i+=1
    count+=1
j=1
while True:
  if(c*j>a):
    break
  else:
    j+=1
    count+=1
k=1
d=b*c/math.gcd(b,c)
while True:
  if(d*k>a):
    break
  else:
    k+=1
    count-=1
print(count)
    
    