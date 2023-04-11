import sys
input=sys.stdin.readline
def fanction(b,c):
    for i in range(1,b):
        for j in range(1,b+1):
            if(i+j>b):
                print(j-1)
                break
            if(c[j-1]==c[i+j-1]):
                print(j-1)
                break
if __name__=='__main__':
    b=int(input())
    c=input()
    fanction(b,c)

    
    