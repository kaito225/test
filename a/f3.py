import sys
input=sys.stdin.readline

def main(B,S,flg):
    
    for i in S:
        if(flg==0):
            if(i==','):
                B=B+"."
            else:
                B=B+i
        else:
            B=B+i
        if (i=='"'):
            flg+=1
            if(flg==2):
                flg=0
    print(B)
if __name__ =='__main__':
    N=input()
    S=input()
    B=str()
    flg=0
    main(B,S,flg)