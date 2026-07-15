numbers=[4,10,10,0,2,1]
count = 0
for item in numbers:
    count+=1
    for i in range(count):
        for j in range(0,count-i-1):
            if numbers[j] > numbers[j+1]:
                numbers[j], numbers[j+1] = numbers[j+1], numbers[j]
print("sorted_array:",numbers)