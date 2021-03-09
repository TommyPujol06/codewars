word = sorted(input().lower())
letters = set(word)

if word == sorted(''.join(letters)):
    print("Isogram detected")
else:
    print("Not an isogram")