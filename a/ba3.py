def count_pairs(n, a):
    colors = {}
    for i in range(n):
        color = a[i]
        if color in colors:
            colors[color] += 1
        else:
            colors[color] = 1
    pairs = 0
    for color in colors:
        pairs += colors[color] // 2
    return pairs

if __name__ == '__main__':
    n=int(input())
    a=list(map(int,input().split()))
    pairs = count_pairs(n, a)
    if pairs == 0:
        print(0)
    else:
        print(pairs)
