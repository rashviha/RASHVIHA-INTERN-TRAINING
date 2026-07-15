alphabet="abcdefghijklmnopqrstuvwxyz"
number="01010101010101010101010101"
total=0
name = input("Enter the name: ")
for ch in name:
    if ch in alphabet:
        index= alphabet.index(ch)
        print(ch,number[index])
        total=total+index
print("sum=",total)