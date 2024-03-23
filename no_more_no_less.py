n = int(input())
for i in range(n):
    size = int(input())
    inp = list(map(int, input().split()))
    lenght = 0
    res = ''
    arr = []
    i = 0
    j = 0
    while j < size:
        if i == 0:
            i = inp[j]
        if inp[j] < i:
            tmp = i
            i = inp[j]
            if len(arr) + 1 > i:
                res += str(len(arr)) + ' '
                lenght += 1
                i = 0
                arr.clear()
            else:
                arr.append(inp[j])
                j += 1
        else:
            if len(arr) + 1 > i:
                res += str(len(arr)) + ' '
                lenght += 1
                i = 0
                arr.clear()
            else:
                arr.append(inp[j])
                j += 1
    res += str(len(arr)) + ' '
    lenght += 1
    print(lenght)
    print(res)