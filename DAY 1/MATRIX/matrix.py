matrix = [
    [1,2,3,4],
    [5,6,7,8],
    [9,7,8,6],
    [5,4,3,2]
    ]
    
n = len(matrix)

primary_diagonal_sum = 0
secondary_diagonal_sum = 0

for i in range(n):
    primary_diagonal_sum += matrix[i][i]
    secondary_diagonal_sum += matrix[i][n - 1 - i]

print("Sum of primary diagonal:", primary_diagonal_sum)
print("Sum of secondary diagonal:", secondary_diagonal_sum)
