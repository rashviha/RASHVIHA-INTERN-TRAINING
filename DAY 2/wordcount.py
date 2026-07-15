import re
letters = ("The cat and dog are playing, The cat is going to dog house")
letters = re.sub(r'[^a-zA-Z\s]', '',letters)
arr=letters.split()
count = {}

for i in arr:
    count[i] = count.get(i, 0) + 1

print(count)