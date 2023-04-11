from collections import Counter

S = input().rstrip()
N = len(S)

# 0~9の各数字の出現回数を数える
count = Counter(S)

# 各数字の出現回数が偶数である場合には、嬉しい列に含まれることができる
happy = [all(c % 2 == 0 for c in count.values())]
a=0
# 各文字列の l 文字目から r 文字目までの部分文字列が嬉しい列であるかどうかを判定する
for l in range(N):
    count = Counter(S[l])
    if all(c % 2 == 0 for c in count.values()):
        a+=1
    for r in range(l + 1, N):
        count[S[r]] += 1
        if all(c % 2 == 0 for c in count.values()):
            a+=1

# 嬉しい列である部分文字列の個数を数える
print(a)

