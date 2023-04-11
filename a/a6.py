import re
while True:
    n=int(input())
    a=input()
    result=re.findall(r"\d+",a)
    k=0
    for i in range(n):
        for k in range(6):
            s=[i][int(result[k])]
    x=[]
    n=0
    if d>0 and d<101:
        if b>0 and b<101:
            while True:    
                c=input()
                e=re.findall(r"\d+",c)
                if len(e)==d:
                    break
            for i in range(len(e)):
                if int(e[i])>0 and int(e[i])<101:
                    x.append(int(e[i]))
            break
if len(x)>0:
    while (range(len(x))): 
        if b==x[n]:
            print("Yes")
            break
        if n==len(x)-1:
            print("No")
            break
        n+=1