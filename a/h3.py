P=input()
L=input()
A=[]
B=[]
for h in range(len(L)):
    B.append(L[h])
for k in range(len(P)+1):
    if(k>0):
        for j in range(len(P)):
            if(j!=k-1):
                A.append(P[j])
        for g in range(len(B)):
            if(A[g]!=B[g] and A[g]!="?" and B[g]!="?" ):
                print("No")
                A=[]
                break
            if(g==len(B)-1):
                print("Yes")
                A=[]
