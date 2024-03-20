t = int(input())

for _ in range(t):
    n = int(input())
    arr = input()
    arr = list(map(str, str(arr)))

    count = arr.count(".")

    for i in range(len(arr)-2):
        if arr[i] == "." and arr[i+1] == "." and arr[i+2] == ".":
            print(2)
            break
    else:
        print(count)
