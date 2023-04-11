N = int(input())
count = 0
for A in range(1, N+1):
    for B in range(1, N+1):
        for C in range(1, N+1):
            D = (N - A * B ) // C
            if (N == A * B + C * D) and (1 <= D <= N):
                count += 1
print(count)

