
def counting(i, j, median):
    steps = 0
    count = 0
    flag = True
    while flag is True:
        if ships[i][j] == '#':
            sdvig = int(median) - j
            steps += abs(sdvig)
            i1 = 0
            if i - i1 != 0 and gameField[i][j + sdvig] != '#':
                while i - i1 - 1 >= 0 and gameField[i - i1 - 1][j + sdvig] != '#':
                    i1 += 1
                gameField[i - i1][j + sdvig] = '#'
                steps += i1
            else:
                while i + i1 + 1 < n and gameField[i + i1][j + sdvig] == '#':
                    i1 += 1
                gameField[i + i1][j + sdvig] = '#'
                steps += i1
            count += 1
        if count == n:
            break
        if j + 1 < n:
            j += 1
        else:
            if i + 1 < n:
                i += 1
                j = 0
            else:
                flag = False
    return steps


n = int(input())
steps = []
ships = [[''] * n for i in range(n)]
gameField = [[''] * n for j in range(n)]
js = []
iss = []
count_ships = [0 for _ in range(n)]
countShips = 0
for i in range(n):
    ship = input().split()
    ships[int(ship[0]) - 1][int(ship[1]) - 1] = '#'
    js.append(int(ship[1]) - 1)
    iss.append(int(ship[0]) - 1)
    count_ships[int(ship[1]) - 1] += 1
if n == 1 or (js.count(max(js)) == n and ships[0][max(js)] == ships[1][max(js)]):
    print('0')
else:
    it = 0
    jt = 0
    for i in range(n):
        steps.append(counting(it, jt, i))
    print(min(steps))
