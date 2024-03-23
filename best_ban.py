n, m = map(int, input().split())
arr = []
max_elem = 0
max_elem2 = 0
max_elem3 = 0
for i in range(n):
    arr.append(list(map(int, input().split())))
for i in range(n):
    maximum = max(arr[i])
    index = arr[i].index(maximum)
    if maximum > max_elem:
        indx_i = i
        indx_j = index
        max_elem = maximum
maxi = 0
for i in range(n):
    if i == indx_i:
        continue
    else:
        maximum = max(arr[i])
        index = arr[i].index(maximum)
        if maximum > max_elem2:
            indx_i2 = i
            indx_j2 = index
            max_elem2 = maximum
for i in range(n):
    for j in range(m):
        if j == indx_j:
            continue
        else:
            if i != indx_i2 or j != indx_j2:
                if arr[i][j] > max_elem3:
                    indx_i3 = i
                    indx_j3 = j
                    max_elem3 = arr[i][j]
if indx_j2 == indx_j3 and indx_i2 == indx_i3:
    if sum(arr[indx_i]) > sum(arr[indx_i2]):
        print(indx_i + 1, indx_j2 + 1)
    else:
        print(indx_i2 + 1, indx_j + 1)
else:
    if indx_i3 == indx_i:
        print(indx_i + 1, indx_j2 + 1)
    elif indx_i2 == indx_i3:
        print(indx_i2 + 1, indx_j + 1)
    elif indx_j == indx_j2:
        print(indx_i3 + 1, indx_j + 1)
    elif indx_j2 == indx_j3:
        print(indx_i + 1, indx_j2 + 1)
    elif max_elem2 > max_elem3:
        print(indx_i + 1, indx_j2 + 1)
    else:
        print(indx_i3 + 1, indx_j + 1)