N = int(input())
a = list(map(str, input().split()))

for i in range(N):
    if a[i] in ["and", "not", "that", "the", "you"]:
        print("Yes")
        break
else:
    print("No")
