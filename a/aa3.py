import sys
input = lambda: sys.stdin.readline().rstrip()
n = int(input())
s = input()
#入力を一度に読み込んでいる 
A = [0, 0]
B = [(0, 0)]
#文字列に対して一つのループで処理をする。
for i in s:
    if i == "R":
        A[0] += 1
    elif i == "L":
        A[0] -= 1
    elif i == "U":
        A[1] += 1
    elif i == "D":
        A[1] -= 1
    B.append(tuple(A))
#重複が多いほど遅くなっていたので削除した場合,set()との値が異なる性質を利用する
if len(B) == len(set(B)):
    print("No")
else:
    print("Yes")
