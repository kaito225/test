import sys
input = sys.stdin.readline

N, Q = map(int, input().split())
B = set()
S = set(range(1, N+1))
h = 1

for i in range(Q):
    A = list(map(int, input().split()))
    if A[0] == 1:
        B.add(h)
        h += 1
    elif A[0] == 3:
        if B:
            print(next(iter(B)))
        else:
            print(next(iter(S)))
    else:
        if A[1] in B:
            B.remove(A[1])
        else:
            S.remove(A[1])
            B.add(A[1])
