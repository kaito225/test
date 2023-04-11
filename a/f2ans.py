n,s = map(int,input().split())
a = list(map(int,input().split()))
dp = [True] + [False] * s;
for i in a:
  for j in range(s,-1,-1):
    if dp[j] and j+i <= s:
      dp[i+j] = True
ans = "Yes" if dp[s] else "No"
print(ans)