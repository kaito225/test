n=int(input())
c=[]
for k in range(n):
    b=(n-2)*(1/2)**n
    c.append(float(b))
print(sum(c))