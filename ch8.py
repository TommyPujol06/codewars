dob = input()
name = input()

while True:
    dob = str(sum([int(i) for i in dob]))
    if len(dob) == 1:
        break
    
fg = True
while True:
    if fg:
        name = str(sum([ord(i) for i in name]))
        fg = False
    else:
        name = str(sum([int(i) for i in name]))

    if len(name) == 1:
        break
    
texts = {
    1:  "You tend to be critical of yourself.",
    2: "You have a great deal of unused capacity which you have not turned to your advantage.",
    3: "While you have some personality weaknesses, you are generally able to compensate for them.",
    4: "At times you are extroverted, affable, sociable, while at other times you are introverted, wary, reserved.",
    5: "Disciplined and self-controlled outside, you tend to be worrisome and insecure inside.",
    6: "At times you have serious doubts as to whether you have made the right decision or done the right thing.",
    7: "You prefer a certain amount of change and variety and become dissatisfied when hemmed in by restrictions and limitations.",
    8: "You pride yourself as an independent thinker and do not accept others' statements without satisfactory proof.",
    9: "You have found it unwise to be too frank in revealing yourself to others.",
}

key = dob+name
while True:
    key = str(sum([int(i) for i in str(key)]))
    if len(key) == 1:
        break
    
print(texts[int(key)])
