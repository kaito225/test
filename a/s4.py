n, a, b = map(int, input().split())
s = input()
s += s
print(s)
ans = 1 << 60#1024ペタバイト数を持たせる、数値オーバー
for i in range(n):
    tmp = a * i
    
    for j in range(n // 2):
        if s[i + j] != s[i + n - 1 - j]:
            tmp += b
    ans = min(ans, tmp)
    
#いととしては文字列の先頭の文字をそれぞれ割り当てた後に、対象の値が異なっているときは、bを足していく。それぞれの最小値を比較することで最小値を計算することができる


print(ans)