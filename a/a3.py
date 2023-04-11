#アルゴリズムの問題
while True:
    n=int(input())
    x=[]
    i=0
    if n>1 and n<100001:
        for k in range(n):
            a=int(input())
            if a>=0 and a<1000000001:
                x.append(a)
        for i in range(len(x)-1):
            if x[i]<x[i+1]:
                print("up ",x[i+1]-x[i])
            if x[i]==x[i+1]:
                print("stay")
            if x[i]>x[i+1]:
                print("down ",x[i]-x[i+1])
        break