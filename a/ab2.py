import math

N = int(input())
A = []
i = 2

while i <= math.sqrt(N):
  if N % i == 0:
    N //= i
    A.append(str(i))
  else:
    i += 1

if N > 1:
  A.append(str(N))

print(" ".join(A))