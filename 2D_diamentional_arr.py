arr2 = np.array([[1, 2, 3, 4],
                 [5, 6, 7, 8],
                 [9, 10,11,12]])

print(arr2[0:2, 1:3])   # Rows 0–1, Columns 1–2
print(arr2[:, 2])      # All rows, 3rd column
print(arr2[1, :])      # 2nd row, all columns
