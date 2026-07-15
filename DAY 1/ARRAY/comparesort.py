arr1 = [10, 'A', 1, 0, 'R', 2]
arr2 = [0, 1, 'B', 12, 'S', 2]

result = []

for i in range(len(arr1)):
    if str(arr1[i]) > str(arr2[i]):
        result.append(arr1[i])
    else:
        result.append(arr2[i])

print(arr3)
