import re
import math
import numpy as np
while True:
    a=input()
    result=re.findall(r"\d+",a)
    g=1
    n=0
    if int(result[0])>0 and int(result[0])<10**18+1:
        if int(result[1])>0 and int(result[1])<10**18+1:
            b=int(result[1])
            while True:
                z=[]
                x=[]
                z.append(float(n*b+int(result[0])/math.sqrt(g+n)))
                n=1
                if n>0:
                    while True:    
                        x.append(float(n*b+int(result[0])/math.sqrt(g+n)))
                        if z[0]<x[0]:
                            break
                        else:
                            z=[]
                            z=x
                            x=[]
                            n+=1
                break
            print(min(z))
            break
                
            
            