N,M = map(int, input().split())
A = []
for i in range(N):
    a = str(input())
    A.append(a)

B = []
C = []
for k in range(N):
    for j in range(M):
        if A[k][j] == "#":
            B.append([k,j])
        elif A[k][j].isdigit():
            C.append([k,j,int(A[k][j])])

# 各爆弾の爆発範囲内にある座標を取得する関数
def get_exploded_coords(center, power):
    coords = set()
    for i in range(center[0]-power, center[0]+power+1):
        if i < 0 or i >= N:
            continue
        for j in range(center[1]-power, center[1]+power+1):
            if j < 0 or j >= M:
                continue
            if abs(center[0]-i) + abs(center[1]-j) <= power:
                coords.add((i,j))
    return coords

# 各爆弾の爆発範囲内にあるブロックを変更する
for center in C:
    exploded_coords = get_exploded_coords(center[:2], center[2])
    for coord in B:
        if tuple(coord) in exploded_coords:
            A[coord[0]] = A[coord[0]][:coord[1]] + "." + A[coord[0]][coord[1]+1:]

# 結果を出力する
# 結果を出力する
for row in A:
    for char in row:
        if char.isdigit():
            print(".", end="")
        else:
            print(char, end="")
    print()

