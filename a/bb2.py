from bisect import bisect_left
import numpy as np


def exists_pair_with_difference(a, x):
    a_sorted = sorted(a)
    for i in range(len(a_sorted) - 1):
        j = bisect_left(a_sorted, a_sorted[i] + x, i, len(a_sorted))
        if j < len(a_sorted) and a_sorted[j] == a_sorted[i] + x:
            return True
    return False

if __name__=='__main__':
    N,M=map(int,input().split())
    x = np.array(input().split(), dtype=np.int64)
    if exists_pair_with_difference(x, M):
        print("Yes")
    else:
        print("No")
