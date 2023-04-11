def main(lines):
    # このコードは標準入力と標準出力を用いたサンプルコードです。
    # このコードは好きなように編集・削除してもらって構いません。
    # ---
    # This is a sample code to use stdin and stdout.
    # Edit and remove this code as you like.
    print(lines)

if __name__ == '__main__':
    N,M=map(int,input().split())
    list1=[]
    list2=[]
    for i in range(N):
        x,y,z=map(int,input().split())
        list1.append([x,y,z])
    for i in range(M):
        x,y,z,v=map(int,input().split())
        list2.append([x,y,z,v])
    main(M)
    print(list1)
    print(list2)