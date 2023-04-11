import re
while True:
    a=input()
    result=re.findall(r"\d+",a)
    if int(result[0])>0 and int(result[1])>0:
        if int(result[0])*int(result[1])>0 and int(result[0])*int(result[1])<4*10**5+1:
            for i in range(int(result[0])):
                    for k in range(int(result[0])):
                        for n in range(int(result[0])):
                            e=[i][n]
                            o=[k][n]
                            b=input()
                            c=input()
                            if len(b)==int(result[1]):
                                if len(c)==int(result[1]):
                                    e[i][n]=e[i][b]
                                    o[k][n]=o[k][c]
                                    if i==result[0]:
                                        for g in range(int(result[0])):
                                            kkk=e[g][:] in o[g][:]
                                            if kkk==True:
                                                print("Yes")
                                                break
                                            else:
                                                print("No")
                                                break