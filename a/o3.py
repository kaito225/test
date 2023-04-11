a=input()
sum=0
count=0
list=["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
for i in range(len(a)):
        sum+=pow(26,len(a)-i-1)*(list.index(a[i])+1)
print(sum)
    