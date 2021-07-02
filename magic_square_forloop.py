
square = [
    [8, 3, 4],
    [1, 5, 9],
    [6, 7, 2]
]

col_sum = 0
for y in range(len(square)):
    for x in range(len(square)):
        col_sum += square[x][y]
print(col_sum)



row_sum = 0
for y in range(len(square)):
    for x in range(len(square)):
        row_sum += square[y][x]
print(row_sum)

diagonal1_sum = 0
for x in range(len(square)):
    diagonal1_sum += square[x][x]
print(diagonal1_sum)



diagonal_sum = 0
for x in range(len(square)):
    diagonal_sum += square[len(square)-x-1][x]
print(diagonal_sum)

if diagonal1_sum==diagonal_sum and row_sum==col_sum:
    print("it is a magic square-",square)
else:
    print("Not magic square-",square)