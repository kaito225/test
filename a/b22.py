A=[]
a=0
b=0
B=["1","2","3","4","5","6","7","8"]
C=["a","b","c","d","e","f","g","h"]
flg=0
for i in  range(8):
    s=input()
    A.append(s)
for j in range(8):
    for k in range(8):
        if  A[j][k]=="*":
            a=j
            b=k
            flg=1
            break
    if flg==1:
        break 
print("".join(C[b]+B[7-a]))