def validate(lst, row, col, val):
    for i in range(9):
        if lst[i][col] == val:
            return False
    for j in range(9):
        if lst[row][j] == val:
            return False
    i = row - row % 3
    j = col - col % 3
    for rowindex in range(3):
        for colindex in range(3):
            if lst[i + rowindex][j + colindex] == val:
                return False
    return True


def solverSudoku(arr, index):
    if index == 81:
        return True
    row = index // 9
    col = index % 9
    if arr[row][col] != 0:
        return solverSudoku(arr, index + 1)
    else:
        for val in range(1, 10):
            if validate(arr, row, col, val):
                arr[row][col] = val
                finished = solverSudoku(arr, index + 1)
                if finished:
                    return finished
                arr[row][col] = 0

arr = [
        [7, 0, 0, 0, 0, 0, 2, 0, 0],
        [4, 0, 2, 0, 0, 0, 0, 0, 3],
        [0, 0, 0, 2, 0, 1, 0, 0, 0],
        [3, 0, 0, 1, 8, 0, 0, 9, 7],
        [0, 0, 9, 0, 7, 0, 6, 0, 0],
        [6, 5, 0, 0, 3, 2, 0, 0, 1],
        [0, 0, 0, 4, 0, 9, 0, 0, 0],
        [5, 0, 0, 0, 0, 0, 1, 0, 6],
        [0, 0, 6, 0, 0, 0, 0, 0, 8]

       ]
solverSudoku(arr, 0)
for val in arr:
    print(val)