t = int(input())

for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    count = 0
    first = -1

    for i in range(n-1):
        if a[i] != 0:
            first = i
            break

    if first == -1: 
        print(0)
        continue
    
    for i in range(first, n-1):
        if a[i] != 0:
            count += a[i]
        else:
            count += 1

    print(count)
