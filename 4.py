def SubRectangle(matrix):
    rows_with_zeros = []
    cols_with_zeros = []
    for i in range(0, len(matrix)):
        if 0 in matrix[i]:
            rows_with_zeros.append(i)
    for i in matrix:
        for j in range(0, len(i)):
            if i[j] == 0:
                cols_with_zeros.append(j)
    top = min(cols_with_zeros)
    bottom = max(cols_with_zeros)
    left = min(rows_with_zeros)
    right = max(rows_with_zeros)
    return (left, top), (left, bottom),  (right, top), (right, bottom)

print(SubRectangle([[1, 0, 0, 1, 1], [1, 0, 0, 0, 1], [1, 0, 0, 1, 1], [1, 1, 1, 1, 1]]))