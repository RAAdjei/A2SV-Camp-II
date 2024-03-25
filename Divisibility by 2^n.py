def counter(num):
    if num % 2 != 0:
        return 0
    if num <= 0:
        return 0
        
    return 1 + counter(num / 2)

def solve():
    count_sum = 0
    ops = 0
    res = []

    for i in range(n):
        count = counter(arr[i])
        count_sum += count

    for i in range(1, n+1):
        num = counter(i)
        if num:
            res.append(num)

    res.sort(reverse=True)

    if count_sum >= n:
        return 0
    
    temp_sum = 0

    for k in res:
        temp_sum += k
        ops += 1
        if temp_sum >= n-count_sum:
            return ops
    
    return -1


t = int(input())

for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    print(solve())
