alphabet = "abcdefghijklmnopqrstuvwxyz"
name = input("Enter the name: ")
total = 0
for ch in name:
    if ch in alphabet:
        num = alphabet.index(ch)+1
        print(ch,num)
        total = total + num
print("Sum =", total)
